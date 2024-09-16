import json
import xml.dom.minidom
import re
import uiautomator2 as u2

class _AndroidDevice():
    def __init__(self, device_url, package_name):
        d = u2.connect(device_url)
        self._d = d
        self.current = self._d.app_current()
        self.package = package_name
        # print("device connected ...")
        # print("current package: "+self.package)

    def dump_hierarchy(self):
        return get_android_hierarchy(self._d, self.package)

    def dump_hierarchy2(self):
        current = self._d.app_current()
        page_xml = self._d.dump_hierarchy(pretty=True)
        page_json = android_hierarchy_to_json(
            page_xml.encode('utf-8'), self.package)
        return {
            "xmlHierarchy": page_xml,
            "jsonHierarchy": page_json,
            "activity": current['activity'],
            "packageName": current['package'],
            "windowSize": self._d.window_size(),
        }

    @property
    def d(self):
        return self._d


def parse_bounds(text):
    m = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', text)
    if m is None:
        return None
    (lx, ly, rx, ry) = map(int, m.groups())
    return dict(x=lx, y=ly, width=rx - lx, height=ry - ly)

def safe_xmlstr(s):
    return s.replace("$", "-")


def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")


def str2int(v):
    return int(v)


def convstr(v):
    return v

__alias = {
    'class': '_type',
    'resource-id': 'resourceId',
    'content-desc': 'description',
    'long-clickable': 'longClickable',
    'bounds': 'rect',
}

__parsers = {
    '_type': safe_xmlstr,  # node className
    # Android
    'rect': parse_bounds,
    'text': convstr,
    'resourceId': convstr,
    'package': convstr,

    'checkable': str2bool,
    'selected': str2bool,

    'scrollable': str2bool,

    'clickable': str2bool,
    'longClickable': str2bool,

    'password': str2bool,

    'index': int,
    'description': convstr,
}

def get_android_hierarchy(d, package):
    page_xml = d.dump_hierarchy(compressed=False, pretty=False).encode('utf-8')
    return android_hierarchy_to_json(page_xml, package)


def android_hierarchy_to_json(page_xml: bytes, package):
    """
    Returns:
        JSON object
    """
    dom = xml.dom.minidom.parseString(page_xml)
    root = dom.documentElement

    def travel(node, package):
        """ return current node info """
        if node.attributes is None:
            return
        json_node = _parse_uiautomator_node(node)

        # json_node['_id'] = str(uuid.uuid4())
        if 'description' not in json_node:
            json_node['description'] = ''
        if 'text' not in json_node:
            json_node['text'] = ''
        if node.childNodes:
            children = []
            for n in node.childNodes:
                child = travel(n, package)
                if child is not None:
                    if child['package'] == package:
                        children.append(child)
            json_node['children'] = children
        return json_node

    return travel(root, package)


def _parse_uiautomator_node(node):
    ks = {}
    for key, value in node.attributes.items():
        key = __alias.get(key, key)
        f = __parsers.get(key)
        if value is None:
            ks[key] = None
        elif f:
            ks[key] = f(value)
    if 'bounds' in ks:
        lx, ly, rx, ry = map(int, ks.pop('bounds'))
        ks['rect'] = dict(x=lx, y=ly, width=rx - lx, height=ry - ly)
    return ks


control_attributes = ["clickable", "longClickable", "scrollable", "password", "selected", "checkable"]

def simplify_json(data):
    # data = json.loads(json_str)
    def simplify_element(element):
        text = element.get("text", "")

        simplified_element = {
            "text": text,
            "desc": element.get("description", ""),
            "id": element.get("resourceId", ""),
            "type": element.get("_type",""),
            "index": element.get("index", ""),
            "x": element.get("rect", {}).get("x", ""),
            "y": element.get("rect", {}).get("y", ""),
            "width": element.get("rect", {}).get("width", ""),
            "height": element.get("rect", {}).get("height", ""),
            # "coord": str(element.get("rect", {}).get("x", "")) +","+str(element.get("rect", {}).get("y", "")),
            "control": [],
            "children": []
        }
        
        # id = simplified_element["id"]
        
        # if id:
        #     pattern = r'([^/]+)/([^/]+)'
        #     simplified_element["id"] = re.search(pattern, id)[2]
        
        for attr in control_attributes:
            if element.get(attr, False):
                simplified_element["control"].append(attr)
            
        children = element.get("children",[])
        
        if not (simplified_element["control"] or simplified_element["text"] or simplified_element["desc"]):
            # print(simplified_element)
            return_array = []
            for e in children:
                s_e = simplify_element(e)
                if s_e == []: continue
                return_array.append(s_e)
            if len(return_array) == 1:
                return return_array[0]
            else: return return_array
        
        for e in children:
            s_e = simplify_element(e)
            if(s_e and s_e !=[]):
                simplified_element["children"].append(s_e)        
        return simplified_element
    simplified_data = simplify_element(data)
    simplified_json = json.dumps(simplified_data, ensure_ascii=False)
    return simplified_json

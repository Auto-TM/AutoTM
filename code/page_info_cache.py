"""
for caching page's widget contextual information
"""
widget_dict = {}


def put(json, nex_page_json, previous_page, widget_info, contextual_info):
    key = json + nex_page_json + previous_page + widget_info
    widget_dict[key] = contextual_info


def get(json, nex_page_json, previous_page, widget_info):
    key = json + nex_page_json + previous_page + widget_info
    if key not in widget_dict:
        return ""
    return widget_dict[key]


def clear():
    widget_dict.clear()

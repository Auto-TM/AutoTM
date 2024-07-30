"""
for caching page's widget contextual information
"""
widget_dict = {}

import json
file_path = '/home/testmigration/文档/fse2024/AutoTM/code/cache.json'
with open(file_path, 'r', encoding='utf-8') as file:
    widget_dict = json.load(file)


def put(current_page_json, nex_page_json, previous_page, widget_info, contextual_info):
    key = current_page_json + nex_page_json + previous_page + widget_info
    widget_dict[key] = contextual_info

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(widget_dict, file, ensure_ascii=False, indent=4)


def get(current_page_json, nex_page_json, previous_page, widget_info):
    key = current_page_json + nex_page_json + previous_page + widget_info
    if key not in widget_dict:
        return ""
    return widget_dict[key]


def clear():
    widget_dict.clear()

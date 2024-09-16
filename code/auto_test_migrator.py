import os
import re
import json as j

from json_extractor import simplify_json
import time
import config
import glob
import traceback
import text_processor
import task_dispatcher
import page_reproducer
import device_operator
from run_logger import logger


def get_page_json():
    """
    Retrieves and simplifies the JSON hierarchy of the Android device.
    """
    for i in range(0, config.MAX_RETRY_TIMES):
        json_page = device_operator.device.dump_hierarchy()
        if len(json_page['children']) > 0:
            break
    return simplify_json(json_page)


def get_test_intents(test_file_dir):
    """
    Reads and returns the test intent from a text file.
    """
    test_file = open(test_file_dir, "r")
    test_intents = test_file.read()

    return test_intents


def extract_widgets(json_data):
    results = []

    def recurse(items):
        if isinstance(items, list):
            for item in items:
                recurse(item)
        elif isinstance(items, dict):
            if all(k in items for k in ['id', 'x', 'y', 'desc']):
                control_funs = items['control']
                results.append({
                    'id': items['id'],
                    'text': items['text'],
                    'type': items['type'],
                    'index': items['index'],
                    'x': items['x'],
                    'y': items['y'],
                    'width': items['width'],
                    'height': items['height'],
                    'desc': items['desc'],
                    'control': control_funs
                })
            if 'children' in items and items['children']:
                recurse(items['children'])

    recurse(json_data)
    return results


def remove_duplicates(dict_list):
    unique_list = []

    seen = set()

    for item in dict_list:
        key = (
            item['id'],
            item['text'],
            item['type'],
            item['width'],
            item['height'],
            item['desc'],
            tuple(item['control'])
        )

        if key not in seen:
            seen.add(key)
            unique_list.append(item)

    return unique_list


def get_pages_intentions(previous_page_json):
    global d
    d = device_operator.d
    current_page_json = '[]'
    for cnt in range(config.MAX_RETRY_TIMES):
        current_page_json = get_page_json()
        if current_page_json == '[]':
            if cnt == config.MAX_RETRY_TIMES - 2:
                page_reproducer.recover()
            if cnt == config.MAX_RETRY_TIMES - 1:
                raise RuntimeError("dump hierarchy empty")
            logger.info("dump hierarchy empty, begin to reproduce current page")
            page_reproducer.reproduce(d)
        else:
            break
    current_page_data = j.loads(current_page_json)

    current_page_widgets = remove_duplicates(extract_widgets(current_page_data))
    logger.info("-----------")
    logger.info(
        "begin to extract context information for all widgets in the GUI interface: {}".format(current_page_widgets))
    logger.info("widgets number: {}".format(len(current_page_widgets)))
    json_intent = ""
    for i in range(len(current_page_widgets)):
        item = current_page_widgets[i]
        id = item['id']

        if id == '':
            widget_info = item['desc']
            if widget_info == "":
                widget_info = item['text']
            if widget_info == "":
                widget_info = "widget id empty, type:{} coordinates:({}, {})" \
                    .format(item['type'], str(item['x']), str(item['y']))
        else:
            widget_info = "id:{}".format(id)
            if item['desc'] != "":
                widget_info += ", desc:{}".format(item['desc'])
            if item['text'] != "":
                widget_info += ", text:{}".format(item['text'])

        if widget_info == "":
            continue

        device_operator.activate_device()
        d = device_operator.d

        logger.info("-----------")
        for op in config.operate_list:
            control = op
            if op == 'clickable':
                d.click(item['x'], item['y'])
            elif op == "longClickable":
                d.long_click(item['x'], item['y'], 1)
            elif op == "swipe_to_right":
                if item['type'] in config.not_swipe_types:
                    continue
                item['x'] += 8
                control = "swipe_to_right. from:[{}, {}] to:[{}, {}]".format(item['x'], item['y'],
                                                                             item['x'] + item['width'],
                                                                             item['y'] + item['height'])
                d.swipe(item['x'], item['y'], item['x'] + item['width'], item['y'] + item['height'])
            elif op == "swipe_to_left":
                if item['type'] in config.not_swipe_types:
                    continue
                control = "swipe_to_left. from:[{}, {}] to:[{}, {}]".format(item['x'] + item['width'],
                                                                            item['y'] + item['height'], item['x'],
                                                                            item['y'])
                d.swipe(item['x'] + item['width'], item['y'] + item['height'], item['x'], item['y'])

            logger.info(
                "widget_number:{}/{} | operator:{} | widget:{}".format(str(i + 1), str(len(current_page_widgets)),
                                                                       control,
                                                                       widget_info))
            time.sleep(1)

            next_page_json = get_page_json()
            widget_intent = task_dispatcher.analyze_widget_contextual_info(current_page_json, next_page_json,
                                                                           previous_page_json,
                                                                           widget_info, control)

            if text_processor.extract_action(widget_intent.strip()) not in json_intent:
                json_intent = json_intent + widget_intent.strip() + "\n"

            d.press("back")
            time.sleep(2)

            # judge whether press back fail
            return_current_page = get_page_json()
            if return_current_page != current_page_json:
                logger.info("back to current page fail, begin to reproduce current page")
                page_reproducer.reproduce(d)

    logger.info("current page's intentions: " + json_intent)
    return json_intent, current_page_json


def get_cur_action(markdown_text):
    """
    Extract the current action and code block from markdown text.
    """
    return text_processor.extract_select_action(markdown_text)


def get_cur_code(markdown_text):
    markdown_text = markdown_text.replace("python", "")
    markdown_text = markdown_text.replace("Python", "")
    markdown_text = markdown_text.replace("'···'", "")
    code = text_processor.extract_response(markdown_text)
    if code == '':
        code_ind1 = markdown_text.find("···\n")
        code_ind2 = -1
        code = ""
        if code_ind1 != -1:
            code_ind2 = markdown_text[code_ind1 + 4:].find("\n···")
            code = markdown_text[code_ind1 + 4: code_ind1 + 4 + code_ind2]
    logger.info("list of executable codes: " + code)

    return code


def update_actions(actions, cur_action):
    """
    Appends the current action to the list of actions.
    """
    logger.info("updating new actions:\n {}".format(cur_action))
    if actions == "":
        actions = cur_action
    else:
        actions = actions + "\n" + cur_action

    logger.info("-----------")
    logger.info("current executed actions:\n {}".format(actions))
    return actions


def exec_cur_code(codes, cur_actions):
    """
    Executes the current code block if it's not empty and doesn't contain the word "assert."
    """
    exec_actions = text_processor.unique_list(cur_actions.splitlines())
    cnt = 0
    action_states = []
    previous_exec_action = ""
    for code in text_processor.unique_list(codes.splitlines()):
        if code.startswith("# ") or code.strip() == "":
            continue
        if cnt >= len(exec_actions):
            exec_action = previous_exec_action
        else:
            exec_action = exec_actions[cnt]
        cnt += 1
        if code.strip() != "" and "assert" not in code:
            action_state = None
            code = code.replace("long_click()", "long_click(1)")
            for i in range(0, config.MAX_RETRY_TIMES):
                try:
                    device_operator.exec_code(code)
                    logger.info("exec code success: {}".format(code))
                    action_state = (exec_action, 'Exec_Success')
                    break
                except Exception as e:
                    logger.info("exec code fail: {}, count: {}".format(code, str(i + 1)))
                    logger.info(e)
                    if i == config.MAX_RETRY_TIMES - 1:
                        action_state = (exec_action, 'Exec_Fail')
            if cnt <= len(exec_actions):
                action_states.append(action_state)
        else:
            if code.strip() != "" and cnt <= len(exec_actions):
                action_states.append((exec_action, 'Exec_Success'))
        previous_exec_action = exec_action
    return action_states


def sort_key(path):
    match = re.search(r'(\d+)\.\w+$', path)
    return int(match.group(1)) if match else float('inf')


def get_test_case_files(directory):
    java_files = glob.glob(os.path.join(directory, '**', '*.java'), recursive=True)
    kotlin_files = glob.glob(os.path.join(directory, '**', '*.kt'), recursive=True)
    json_files = glob.glob(os.path.join(directory, '**', '*.json'), recursive=True)
    return sorted(java_files + kotlin_files + json_files, key=sort_key)


def select_event_and_execute(markdown_file, test_semantics, actions, pages_intentions):
    """
    This function orchestrates a single step of the testing process.
    It fetches the JSON intention, matches the test semantics with it,
    writes the results to a markdown file, executes code if necessary,
    and updates the list of actions.
    """
    select_result = task_dispatcher.select_event(test_semantics, actions, pages_intentions)
    cur_action = get_cur_action(select_result)

    script = task_dispatcher.generate_script(cur_action)

    executable_codes = get_cur_code(script)
    text_processor.generate_markdown_procedure(markdown_file, pages_intentions, select_result + '\n' + script)

    action_states = exec_cur_code(executable_codes, cur_action)
    actions_with_state = text_processor.concat_action_states(action_states, cur_action)
    actions = update_actions(actions, actions_with_state)

    return actions


def begin_operate(markdown_file, test_semantics):
    """
    The main entry point of the script. It runs the testing process using a loop until a termination condition is met.
    """
    try:
        actions = ""
        text_processor.generate_markdown_test_semantic(markdown_file, test_semantics)

        previous_page = ""
        while "DONE" not in actions and "NOT FOUND" not in actions:
            pages_intentions, previous_page = get_pages_intentions(previous_page)
            actions = select_event_and_execute(markdown_file, test_semantics, actions, pages_intentions)
        text_processor.generate_markdown_result(markdown_file, actions)
    except Exception as e:
        raise e
    finally:
        markdown_file.flush()


d = None


def migrate(source_test_case_path, markdown_file, package_name, target_launch_activity, device_number):
    device_operator.setup(device_number, package_name)
    device_operator.activate_device()
    start_time = time.time()
    global d
    d = device_operator.d

    logger.info("-----------")
    # get a11_b11 of ./dataset/result/craftdroid/a1-Browser/a11_b11 as Semantics file name
    test_semantics_file_path = (os.path.dirname(markdown_file.name) + "/"
                                + os.path.basename(os.path.dirname(markdown_file.name)) + "_Semantics_AutoTM.txt")
    test_semantics = task_dispatcher.get_test_semantics(test_semantics_file_path,
                                                        text_processor.read_file(source_test_case_path))
    logger.info("source_test_case_path: {}, semantics: {}".format(source_test_case_path, test_semantics))
    logger.info("-----------")

    device_operator.activate_device()
    device_operator.stop_app(package_name)
    device_operator.start_app(package_name)

    try:
        begin_operate(markdown_file, test_semantics)
    except Exception as e:
        logger.info("error occurred, error info: {}".format(e.__str__()))
        error_stack = traceback.format_exc()
        logger.info("error stack: {}".format(error_stack))
        text_processor.generate_markdown_exception(markdown_file, error_stack)
    finally:
        device_operator.stop_app(package_name)

        end_time = time.time()
        logger.info("time-consuming /s: {}".format(str(end_time - start_time)))

        markdown_file.flush()
        markdown_file.close()
        page_reproducer.clear()

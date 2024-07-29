import os
import json as j

from json_extractor import  simplify_json
import time
import constants
import logging
import glob
import traceback
import text_processor
import task_dispatcher
import page_reproducer
import device_operator
import page_info_cache

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler('../log/run.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_json():
    """
    Retrieves and simplifies the JSON hierarchy of the Android device.
    """

    # logger.info("dump hierarchy ...")

    for i in range(0, 10):
        time.sleep(1)
        json_page = device_operator.device.dump_hierarchy()
        if len(json_page['children']) > 0:
            break

    # logger.info("hierarchy_page_json: " + str(json_page))

    # logger.info("hierarchy dumped.")

    return simplify_json(json_page)


def get_test_intents(test_file_dir):
    """
    Reads and returns the test intent from a text file.
    """
    test_file = open(test_file_dir, "r")
    test_intents = test_file.read()
    # logger.info(test_intents)

    return test_intents


def request_agent(request_str, local_contest):
    i = 0

    while i < constants.MAX_RETRY_TIMES:
        try:
            exec(request_str, {}, local_contest)
        except Exception as ex:
            i += 1
            logger.info("agent_error, retrying, error info: {}".format(ex.__str__()))
            logger.info("agent_error, sleeping 1 minutes, retry times: {}".format(i))
            time.sleep(60 * 1)
            if i == constants.MAX_RETRY_TIMES:
                logger.info("retrying max reached, error info: {}".format(ex.__str__()))
                raise ex
            continue
        break
    return local_contest['response']


def get_page_intent(previous_page):
    json = ''
    for index in range(5):
        json = get_json()
        if json != '[]':
            break
        logger.info("dump hierarchy empty, retrying...")
        device_operator.activate_device()
        time.sleep(1)

    if json == '[]':
        raise RuntimeError("dump hierarchy empty")
    current_page_data = j.loads(json)

    def find_element_and_check_clickable(data, target_id):
        if isinstance(data, dict):
            if data.get('id') == target_id:
                return 'clickable' in data.get('control', [])
            for key in data:
                result = find_element_and_check_clickable(data[key], target_id)
                if result is not None:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = find_element_and_check_clickable(item, target_id)
                if result is not None:
                    return result
        return None

    def extract_fields(json_data):
        results = []

        def recurse(items):
            if isinstance(items, list):
                for item in items:
                    recurse(item)
            elif isinstance(items, dict):
                if all(k in items for k in ['id', 'x', 'y', 'desc']):
                    results.append({
                        'id': items['id'],
                        'x': items['x'],
                        'y': items['y'],
                        'desc': items['desc']
                    })
                if 'children' in items and items['children']:
                    recurse(items['children'])

        recurse(json_data)
        return results

    results = extract_fields(current_page_data)
    logger.info("-----------")
    logger.info("begin to extract context information for all widgets in the GUI interface: {}".format(results))
    json_intent = ""
    for item in results:
        id = item['id']
        if 'selected' in id:
            continue

        if id == '':
            widget_info = item['desc']
        else:
            widget_info = id

        if widget_info == "":
            continue

        device_operator.activate_device()
        global d
        d = device_operator.d

        if item['id'] != '':
            try:
                d(resourceId=id).click()
            except Exception as e:
                d.click(item['x'], item['y'])
        else:
            d.click(item['x'], item['y'])

        time.sleep(3)

        nex_page_json = get_json()
        time.sleep(3)

        d.press("back")
        time.sleep(3)

        logger.info("-----------")
        widget_intent = page_info_cache.get(json, nex_page_json, previous_page, widget_info)
        logger.info("widget_info:{}".format(widget_info))
        if widget_intent == "":
            widget_intent = task_dispatcher.analyze_widget_contextual_info(json, nex_page_json, previous_page, widget_info)
            page_info_cache.put(json, nex_page_json, previous_page, widget_info, widget_intent)
        else:
            logger.info("hit cache, intention: {}".format(widget_intent))

        json_intent = json_intent + widget_intent + "\n"

        # judge whether press back fail
        return_current_page = get_json()
        if return_current_page != json:
            page_reproducer.reproduce()

    logger.info("current page's intentions: " + json_intent)
    return json_intent, json


def get_cur_action(markdown_text):
    """
    Extract the current action and code block from markdown text.
    """
    if "~~~" not in markdown_text:
        return markdown_text
    return markdown_text.split("~~~\n")[1].split("\n~~~")[0]


def get_cur_code(markdown_text):
    markdown_text = markdown_text.replace("python", "")
    code_ind1 = markdown_text.find("···\n")
    code_ind2 = -1
    code = ""
    if code_ind1 != -1:
        code_ind2 = markdown_text[code_ind1 + 4:].find("\n···")
        code = markdown_text[code_ind1 + 4: code_ind1 + 4 + code_ind2]

    if code == '':
        return text_processor.extract_response(markdown_text)
    logger.info("executable codes: " + code)

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
    exec_actions = cur_actions.splitlines()
    cnt = 0
    action_states = []
    previous_exec_action = ""
    for code in codes.splitlines():
        if code.startswith("# ") or code == "":
            continue
        if cnt >= len(exec_actions):
            exec_action = previous_exec_action
        else:
            exec_action = exec_actions[cnt]
            cnt += 1
        if code != "" and "assert" not in code:
            action_state = None
            for i in range(0, constants.MAX_RETRY_TIMES):
                if exec_action == previous_exec_action:
                    break
                try:
                    device_operator.exec_code(code)
                    logger.info("exec code success: {}".format(code))
                    page_reproducer.collect(code)
                    action_state = (exec_action, 'Exec_Success')
                    break
                except Exception as e:
                    logger.info("exec code fail: {}, count: {}".format(code, str(i + 1)))
                    logger.info(e)
                    if i == constants.MAX_RETRY_TIMES - 1:
                        action_state = (exec_action, 'Exec_Fail')

            if exec_action != previous_exec_action:
                action_states.append(action_state)
        else:
            if code != "" and exec_action != previous_exec_action:
                action_states.append((exec_action, 'Exec_Success'))
        previous_exec_action = exec_action
    return action_states


def w_markdown_proceed(markdown_file, json_intent, match_result):
    markdown_text = \
        "#### Contextual Semantics of Widgets\n````\n" + json_intent + "\n````" \
        + "\n" \
        + "\n#### Selected Event(s) and Script\n````\n" + match_result + "\n````" \
        + "\n"
    markdown_file.write(markdown_text)
    markdown_file.flush()
    return markdown_text


def get_test_case_files(directory):
    java_files = glob.glob(os.path.join(directory, '**', '*.java'), recursive=True)
    kotlin_files = glob.glob(os.path.join(directory, '**', '*.kt'), recursive=True)
    json_files = glob.glob(os.path.join(directory, '**', '*.json'), recursive=True)
    return java_files + kotlin_files + json_files


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
    The main entry point of the script. It initializes variables, opens a markdown file for writing,
    and runs the testing process using a loop until a termination condition is met.
    """

    try:
        actions = ""
        text_processor.generate_markdown_test_semantic(markdown_file, test_semantics)

        previous_page = ""
        while "DONE" not in actions and "NOT FOUND" not in actions:
            pages_intentions, previous_page = get_page_intent(previous_page)

            actions = select_event_and_execute(markdown_file, test_semantics, actions, pages_intentions)
        text_processor.generate_markdown_result(markdown_file, actions)
    except Exception as e:
        raise e
    finally:
        markdown_file.flush()


d = None


def migrate(source_test_code_dir_path, package_name, target_launch_activity, device_number):
    device_operator.setup(device_number)
    device_operator.activate_device()
    global d
    d = device_operator.d

    logger.info("-----------")
    logger.info("beginning to migrate")
    start_time = time.time()
    logger.info("-----------")

    source_test_case_paths = get_test_case_files(source_test_code_dir_path)

    for source_test_case_path in source_test_case_paths:
        source_test_code_file_dir = os.path.dirname(source_test_case_path)
        source_test_code_file_name = os.path.splitext(os.path.basename(source_test_case_path))[0]
        markdown_file_path = source_test_code_file_dir + "/" + source_test_code_file_name + "_AutoTM.md"
        if os.path.exists(markdown_file_path):
            os.remove(markdown_file_path)
            logger.info(f"deleted the existing markdown file at {markdown_file_path}")
        else:
            os.makedirs(os.path.dirname(markdown_file_path), exist_ok=True)
        markdown_file = open(markdown_file_path, "a")
        logger.info("workflow markdown file path: " + markdown_file_path)

        text_processor.generate_markdown_title(markdown_file, source_test_code_file_name)

        logger.info("-----------")
        logger.info("test_semantic_analyzer_agent processing...")
        test_semantics_file = source_test_code_file_dir + "/" + source_test_code_file_name + "_Semantics_AutoTM.txt"
        test_semantics = task_dispatcher.get_test_semantics(test_semantics_file,
                                                            text_processor.read_file(source_test_case_path))
        logger.info("source_test_case_path: {}, semantics: {}".format(source_test_case_path, test_semantics))
        logger.info("-----------")

        device_operator.stop_app(package_name)
        device_operator.start_app(target_launch_activity)
        device_operator.activate_device()

        try:
            begin_operate(markdown_file, test_semantics)
        except Exception as e:
            logger.info("error occurred, error info: {}".format(e.__str__()))
            logger.info("error stack: {}".format(traceback.format_exc()))
        device_operator.stop_app(package_name)

        end_time = time.time()
        logger.info("time-consuming /s: {}".format(str(end_time - start_time)))
        text_processor.generate_markdown_cost(markdown_file, start_time, end_time)
        markdown_file.close()
        page_reproducer.clear()
        page_info_cache.clear()
        logger.info("---------------------finished-----------------------")

import os
import json as j


from jsonExtract import _AndroidDevice, simplify_json
import time
import constants
import logging
import glob
import agents.test_semantic_analyzer
import agents.event_contextual_semantic_analyzer
import agents.event_selector
import agents.test_script_generator

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


class Gpt:
    def __init__(self, key, model):
        self.key = key
        self.model = model


def get_json():
    """
    Retrieves and simplifies the JSON hierarchy of the Android device.
    """

    # logger.info("dump hierarchy ...")

    for i in range(0, 10):
        time.sleep(1)
        json_page = device.dump_hierarchy()
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


def get_json_intent(previous_page, rollbacker):
    json = ''
    for index in range(5):
        json = get_json()
        if json != '[]':
            break
        logger.info("dump hierarchy empty, retrying...")
        device = _AndroidDevice("")
        d = device.d
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

        device = _AndroidDevice("")
        d = device.d

        if item['id'] != '':
            d(resourceId=id).click()
        else:
            d.click(item['x'], item['y'])

        time.sleep(2)

        nex_page_json = get_json()
        time.sleep(1)

        d.press("back")
        time.sleep(2)

        logger.info("-----------")
        logger.info("event_contextual_semantic_analyzer processing...")
        local_contest = {'agents': agents, 'gpt_4': gpt_4, 'previous_page': previous_page,
                         'widget_info': widget_info, 'json': json, 'nex_page_json': nex_page_json}
        widget_intent = request_agent(
            'response = agents.event_contextual_semantic_analyzer.analyze(gpt_4, previous_page, widget_info, json, nex_page_json)',
            local_contest)
        logger.info("widget_info:{}, intention: {}".format(widget_info, widget_intent))
        logger.info("-----------")

        json_intent = json_intent + widget_intent + "\n"

        # judge whether press back fail
        return_current_page = get_json()
        if return_current_page != json:
            executed_codes = rollbacker.splitlines()
            for code in executed_codes:
                try:
                    exec(code)
                except Exception as ex:
                    pass

    logger.info("current page's intentions: " + json_intent)
    return json_intent, json


def select_event(test_semantics, actions, pages_intentions):
    """
    Uses the GPT-4 model to match the test semantics with the Page JSON intention.
    """
    logger.info("-----------")
    logger.info("event_selector processing...")
    if actions == "":
        actions = "The first operation has no executed actions"
    local_contest = {'agents': agents, 'gpt_4': gpt_4, 'test_semantics': test_semantics, 'actions': actions, 'pages_intentions': pages_intentions}
    select_result = request_agent('response = agents.event_selector.select(gpt_4, test_semantics, actions, pages_intentions)',
                                   local_contest)
    logger.info("select_result: {}".format(select_result))
    logger.info("-----------")

    return select_result


def get_cur_action(markdown_text):
    """
    Extract the current action and code block from markdown text.
    """
    if "~~~" not in markdown_text:
        return markdown_text
    return markdown_text.split("~~~\n")[1].split("\n~~~")[0]


def get_cur_code(markdown_text):
    code_ind1 = markdown_text.find("···\n")
    code_ind2 = -1
    code = ""
    if code_ind1 != -1:
        code_ind2 = markdown_text[code_ind1 + 4:].find("\n···")
        code = markdown_text[code_ind1 + 4: code_ind1 + 4 + code_ind2]

    logger.info("code: " + code)

    return code


def get_test_semantics(file_path, gpt_config, source_test_code):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            test_semantics = file.read()
    else:
        local_contest = {'agents': agents, 'gpt_config': gpt_config, 'source_test_code': source_test_code}
        test_semantics = request_agent('response = agents.test_semantic_analyzer.analyze(gpt_config, source_test_code)',
                                       local_contest)
        with open(file_path, 'w') as file:
            file.write(test_semantics)
    return test_semantics

def update_actions(actions, cur_action):
    """
    Appends the current action to the list of actions.
    """
    if actions == "":
        actions = cur_action
    else:
        actions = actions + "\n" + cur_action

    # logger.info("actions: "+actions)
    return actions


def exec_cur_code(codes, rollbacker, cur_actions):
    """
    Executes the current code block if it's not empty and doesn't contain the word "assert."
    """
    exec_actions = cur_actions.splitlines()
    cnt = 0
    action_states = []
    previous_exec_action = ""
    for code in codes.splitlines():
        if code.startswith("# "):
            continue
        if cnt >= len(exec_actions):
            exec_action = previous_exec_action
        else:
            exec_action = exec_actions[cnt]
            cnt += 1
        if code != "" and "assert" not in code:
            action_state = None
            for i in range(0, constants.MAX_RETRY_TIMES):
                try:
                    logger.info("exec code count: " + str(i + 1))
                    exec(code)
                    rollbacker += code + '\n'
                    rollbacker += 'time.sleep(3)' + '\n'
                    action_state = (exec_action, 'Exec_Success')
                    break
                except Exception as e:
                    logger.info(e)
                    if i == constants.MAX_RETRY_TIMES - 1:
                        action_state = (exec_action, 'Exec_Fail')
            action_states.append(action_state)
        else:
            if code != "":
                action_states.append((exec_action, 'Exec_Success'))
        previous_exec_action = exec_action
    return action_states, rollbacker


def w_markdown_proceed(markdown_file, json_intent, match_result):
    markdown_text = \
        "#### Contextual Semantics of Widgets\n````\n" + json_intent + "\n````" \
        + "\n" \
        + "\n#### Selected Event(s) and Script\n````\n" + match_result + "\n````" \
        + "\n"
    markdown_file.write(markdown_text)

    return markdown_text


def w_markdown_h2(markdown_file, test_intents, markdown_h2):
    intent_list = "> "
    for test_intent in test_intents:
        if test_intent != "\n":
            intent_list += test_intent
        else:
            intent_list += "\n> "
    markdown_text = "## " + markdown_h2 + "\n\n### Semantics of Source Test case" + intent_list + "\n\n### Process\n"
    markdown_file.write(markdown_text)


def w_markdown_done(markdown_file, actions):
    if "DONE" in actions:
        result = "### Success\n"
    else:
        result = "### Fail\n"
    result += "````\n" + actions + "\n````\n"
    markdown_file.write(result)


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def get_java_and_kotlin_files(directory):
    java_files = glob.glob(os.path.join(directory, '**', '*.java'), recursive=True)
    kotlin_files = glob.glob(os.path.join(directory, '**', '*.kt'), recursive=True)
    return java_files + kotlin_files

def generate_script(cur_action):
    """
    generate script via test_script_generator
    """
    logger.info("-----------")
    logger.info("test_script_generator processing...")
    local_contest = {'agents': agents, 'gpt_4': gpt_4, 'cur_action': cur_action}
    script = request_agent(
        'response = agents.test_script_generator.generate(gpt_4, "d", cur_action)',
        local_contest)
    logger.info("script: {}".format(script))
    return script

def match_and_update_actions(markdown_file, test_semantics, actions, pages_intentions, rollbacker):
    """
    This function orchestrates a single step of the testing process.
    It fetches the JSON intention, matches the test semantics with it,
    writes the results to a markdown file, executes code if necessary,
    and updates the list of actions.
    """

    select_result = select_event(test_semantics, actions, pages_intentions)
    cur_action = get_cur_action(select_result)

    script = generate_script(cur_action)

    codes = get_cur_code(script)


    w_markdown_proceed(markdown_file, pages_intentions, select_result + '\n' + script)
    action_states, rollbacker = exec_cur_code(codes, rollbacker, cur_action)

    actions_with_state = ""
    for action_state in action_states:
        actions_with_state += action_state[0] + ', ' + action_state[1] + '\n'

    logger.info("updating new actions: {}".format(cur_action))
    actions = update_actions(actions, actions_with_state)
    time.sleep(0.5)

    return actions, rollbacker



def run(markdown_file_path, markdown_h2, test_semantics, rollbacker):
    """
    The main entry point of the script. It initializes variables, opens a markdown file for writing,
    and runs the testing process using a loop until a termination condition is met.
    """
    if os.path.exists(markdown_file_path):
        os.remove(markdown_file_path)
        logger.info(f"deleted the existing markdown file at {markdown_file_path}")
    else:
        os.makedirs(os.path.dirname(markdown_file_path), exist_ok=True)

    markdown_file = open(markdown_file_path, "a")

    try:
        actions = ""
        if actions == "":
            w_markdown_h2(markdown_file, test_semantics, markdown_h2)

        previous_page = ""
        while "DONE" not in actions and "NOT FOUND" not in actions:
            pages_intentions, previous_page = get_json_intent(previous_page, rollbacker)

            actions, rollbacker = match_and_update_actions(markdown_file, test_semantics, actions, pages_intentions,
                                                           rollbacker)
        w_markdown_done(markdown_file, actions)
        markdown_file.flush()
    except Exception as e:
        raise e
    finally:
        markdown_file.close()


device = _AndroidDevice("")
d = device.d

gpt_4 = None


def migrate(source_test_code_dir_path, package_name, target_launch_activity, gpt_config):
    global gpt_4
    global device
    global d
    gpt_4 = gpt_config
    logger.info("-----------")
    logger.info("beginning to migrate")
    logger.info("-----------")

    source_test_code_paths = get_java_and_kotlin_files(source_test_code_dir_path)

    for source_test_code_path in source_test_code_paths:
        source_test_code_file_dir = os.path.dirname(source_test_code_path)
        source_test_code_file_name = os.path.splitext(os.path.basename(source_test_code_path))[0]

        logger.info("-----------")
        logger.info("test_semantic_analyzer_agent processing...")
        test_semantics_file = source_test_code_file_dir + "/" + source_test_code_file_name + "_Semantics_AutoTM.txt"
        test_semantics = get_test_semantics(test_semantics_file, gpt_config, read_file(source_test_code_path))
        logger.info("source_test_code_path: {}, semantics: {}".format(source_test_code_path, test_semantics))
        logger.info("-----------")

        rollbacker = ''
        stop_app_cmd = "adb shell am force-stop " + package_name
        os.system(stop_app_cmd)
        time.sleep(3)
        rollbacker += f'os.system("{stop_app_cmd}")' + '\n'
        rollbacker += 'time.sleep(3)' + '\n'

        start_app_cmd = "adb shell am start -n " + target_launch_activity
        os.system(start_app_cmd)
        time.sleep(3)
        rollbacker += f'os.system("{start_app_cmd}")' + '\n'
        rollbacker += 'time.sleep(3)' + '\n'

        device = _AndroidDevice("")
        d = device.d

        markdown_file_path = source_test_code_file_dir + "/" + source_test_code_file_name + "_AutoTM.md"

        logger.info("workflow markdown file path: " + markdown_file_path)

        try:
            run(markdown_file_path, source_test_code_file_name, test_semantics, rollbacker)
        except Exception as e:
            logger.info("error occurred, error info: {}".format(e.__str__()))
        stop_app_cmd = "adb shell am force-stop " + package_name
        os.system(stop_app_cmd)
        logger.info("---------------------finished-----------------------")

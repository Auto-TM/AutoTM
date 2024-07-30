"""
call agents
"""

import constants
import logging
import time
import os
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

gpt_4 = constants.openai_api_config


def request_agent(request_str, local_contest):
    i = 0

    while i < constants.MAX_AGENT_RETRY_TIMES:
        try:
            exec(request_str, {}, local_contest)
        except Exception as ex:
            i += 1
            logger.info("agent_error, retrying, error info: {}".format(ex.__str__()))
            if "8192 tokens" in ex.__str__() and "gpt_4" in local_contest:
                gpt_4.model = "gpt-4-32k"
                local_contest["gpt_4"] = gpt_4

            logger.info("agent_error, sleeping 1 minutes, retry times: {}".format(i))
            time.sleep(60 * 1)
            if i == constants.MAX_AGENT_RETRY_TIMES:
                logger.info("retrying max reached, error info: {}".format(ex.__str__()))
                raise ex
            continue

        break
    gpt_4.model = "'gpt-4"
    return local_contest['response']


def get_test_semantics(file_path, source_test_code):
    logger.info("test_semantic_analyzer_agent processing...")
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            test_semantics = file.read()
    else:
        local_contest = {'agents': agents, 'gpt_4': gpt_4, 'source_test_code': source_test_code}
        test_semantics = request_agent('response = agents.test_semantic_analyzer.analyze(gpt_4, source_test_code)',
                                       local_contest)
        with open(file_path, 'w') as file:
            file.write(test_semantics)
    return test_semantics


def analyze_widget_contextual_info(json, nex_page_json, previous_page, widget_info):
    logger.info("event_contextual_semantic_analyzer processing...")
    local_contest = {'agents': agents, 'gpt_4': gpt_4, 'previous_page': previous_page,
                     'widget_info': widget_info, 'json': json, 'nex_page_json': nex_page_json}
    widget_intent = request_agent(
        'response = agents.event_contextual_semantic_analyzer.analyze(gpt_4, previous_page, widget_info, json, nex_page_json)',
        local_contest)
    logger.info("intention: {}".format(widget_intent))
    return widget_intent


def select_event(test_semantics, actions, pages_intentions):
    """
    Uses the GPT-4 model to match the test semantics with the Page JSON intention.
    """
    logger.info("-----------")
    logger.info("event_selector processing...")
    if actions == "":
        actions = "The first operation has no executed actions"
    local_contest = {'agents': agents, 'gpt_4': gpt_4, 'test_semantics': test_semantics, 'actions': actions,
                     'pages_intentions': pages_intentions}
    select_result = request_agent(
        'response = agents.event_selector.select(gpt_4, test_semantics, actions, pages_intentions)',
        local_contest)
    logger.info("select_result: {}".format(select_result))
    logger.info("-----------")

    return select_result


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

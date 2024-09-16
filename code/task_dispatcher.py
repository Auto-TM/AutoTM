"""
call agents
"""

import config
import time
import os
import text_processor
import agents.test_semantic_analyzer
import agents.event_contextual_semantic_analyzer
import agents.event_selector
import agents.test_script_generator
from run_logger import logger

gpt_4 = config.openai_api_config


def request_agent(request_str, local_contest):
    i = 0

    while i < config.MAX_AGENT_RETRY_TIMES:
        try:
            exec(request_str, {}, local_contest)
        except Exception as ex:
            i += 1

            if "maximum context length is 819" in ex.__str__() and "gpt_4" in local_contest:
                gpt_4.model = "gpt-4-32k"
                local_contest["gpt_4"] = gpt_4
                logger.info("8192 tokens is not enough, switch to 32k model")
            else :
                logger.info("agent_error, retrying, error info: {}".format(ex.__str__()))
            logger.info("agent_error, sleeping " + str(3 * i) + " s, retry times: {}".format(i))
            time.sleep(3 * i)
            if i == config.MAX_AGENT_RETRY_TIMES:
                logger.info("retrying max reached, error info: {}".format(ex.__str__()))
                raise ex
            continue

        break
    gpt_4.model = config.model
    return local_contest['response']


def get_test_semantics(file_path, source_test_code):
    # logger.info("test_semantic_analyzer_agent processing...")
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


def analyze_widget_contextual_info(json, next_page_json, previous_page, widget_info, widget_control):
    # logger.info("event_contextual_semantic_analyzer processing...")
    local_contest = {'agents': agents, 'gpt_4': gpt_4, 'previous_page': previous_page,
                     'widget_info': widget_info, 'json': json, 'next_page_json': next_page_json, 'widget_control': widget_control}
    widget_intent = request_agent(
        'response = agents.event_contextual_semantic_analyzer.analyze(gpt_4, previous_page, widget_info, json, next_page_json, widget_control)',
        local_contest)
    widget_intent = text_processor.extract_response(widget_intent)
    logger.info("intention: {}".format(widget_intent.strip()))
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
    # logger.info("-----------")
    logger.info("test_script_generator processing...")
    local_contest = {'agents': agents, 'gpt_4': gpt_4, 'cur_action': cur_action}
    script = request_agent(
        'response = agents.test_script_generator.generate(gpt_4, "d", cur_action)',
        local_contest)
    logger.info("script: {}".format(script))
    return script

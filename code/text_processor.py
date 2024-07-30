"""
extract text or process text procedure
"""
import re
import token_extractor


def extract_response(text):
    extracted_texts = re.findall(r'(?:```|···)(.*?)(?:```|···)', text, re.DOTALL)
    res = ""
    for line in extracted_texts:
        if line == "":
            continue
        res += line + '\n'
    return res


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def concat_action_states(action_states, cur_action):
    actions_with_state = ""
    for action_state in action_states:
        actions_with_state += action_state[0] + ', ' + action_state[1] + '\n'

    if "DONE" in cur_action:
        actions_with_state += "DONE"
    if "NOT FOUND" in cur_action:
        actions_with_state += "NOT FOUND"

    return actions_with_state


def generate_markdown_title(markdown_file, markdown_h2):
    markdown_text = "## " + markdown_h2
    markdown_file.write(markdown_text)
    markdown_file.flush()


def generate_markdown_test_semantic(markdown_file, test_intents):
    intent_list = "> "
    for test_intent in test_intents:
        if test_intent != "\n":
            intent_list += test_intent
        else:
            intent_list += "\n> "
    markdown_text = "\n\n### Semantics of Source Test case\n" + intent_list + "\n\n### Process\n"
    markdown_file.write(markdown_text)
    markdown_file.flush()


def generate_markdown_procedure(markdown_file, json_intent, match_result):
    markdown_text = \
        "#### Contextual Semantics of Widgets\n````\n" + json_intent + "\n````" \
        + "\n" \
        + "\n#### Selected Event(s) and Script\n````\n" + match_result + "\n````" \
        + "\n"
    markdown_file.write(markdown_text)
    markdown_file.flush()
    return markdown_text


def generate_markdown_result(markdown_file, actions):
    if "DONE" in actions:
        result = "### Success\n"
    else:
        result = "### Fail\n"
    result += "````\n" + actions + "\n````\n"
    markdown_file.write(result)
    markdown_file.flush()


def generate_markdown_cost(markdown_file, start_time, end_time):
    try:
        in_token, out_token, price = token_extractor.collect_token(start_time, end_time)
    except Exception as e:
        in_token, out_token, price = start_time, end_time, -1

    result = "### Cost\n"
    result += "````\n" + "time cost: {} s".format(str(int(end_time - start_time))) + "\n"
    result += "in_token: {}".format(str(in_token)) + "\n"
    result += "out_token: {}".format(str(out_token)) + "\n"
    result += "spent: {} $".format(str(round(price, 2))) + "\n````\n"

    markdown_file.write(result)
    markdown_file.flush()

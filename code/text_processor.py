"""
extract text or process text procedure
"""
import re


def extract_response(text):
    extracted_texts = re.findall(r'(?:```|···)(.*?)(?:```|···)', text, re.DOTALL)
    res = ""
    for line in extracted_texts:
        if line == "":
            continue
        res += line + '\n'
    if res.strip() == "":
        return text
    return res


def extract_select_action(text):
    res = ""
    extracted_texts = re.findall(r'(?:```|~~~)(.*?)(?:```|~~~)', text, re.DOTALL)
    for line in extracted_texts:
        if line.strip() == "":
            continue
        res += line.strip() + '\n'

    if res == "":
        lines = text.strip().split('\n')
        keywords = ["ASSERT", "ACTION", "RETURN", "DONE", "NOT FOUND"]
        matching_lines = [line for line in lines if any(line.startswith(keyword) for keyword in keywords)]
        for line in matching_lines:
            if line.strip() == "":
                continue
            res += line.strip() + '\n'

    if res == "":
        return text.replace("~~~", "")
    return res


def extract_action(text):
    pattern = r'ACTION \([^)]*?(?:\([^)]*\)[^)]*)*\)'

    match = re.search(pattern, text)

    if match:
        action_part = match.group(0)
        return action_part
    else:
        return text
    return text


def unique_list(original_list):
    seen = set()
    return list(filter(None, [x for x in original_list if not (x in seen or seen.add(x))]))

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def concat_action_states(action_states, cur_action):
    actions_with_state = ""
    for action_state in action_states:
        if "DONE" in action_state or "NOT FOUND" in action_state:
            actions_with_state += action_state[0]
            break
        actions_with_state += action_state[0] + ', ' + action_state[1] + '\n'

    if "DONE" in cur_action and "DONE" not in actions_with_state:
        actions_with_state += "DONE"
    if "NOT FOUND" in cur_action and "NOT FOUND" not in actions_with_state:
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


def generate_markdown_exception(markdown_file, error):
    result = "### Runtime Exception\n````\n" + error + "\n````\n"
    markdown_file.write(result)
    markdown_file.flush()


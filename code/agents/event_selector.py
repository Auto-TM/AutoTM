import openai


def select(gpt, test_semantics, actions, page_intentions):
    openai.api_key = gpt.key
    openai.api_base = gpt.api_base

    response = openai.ChatCompletion.create(
        model=gpt.model,
        messages=[
            {"role": "system",
             "content": "You are a project manager. You understand Android software and its operating logic. You are conducting test case migration between applications of the same type. You can examine past behaviors, judge whether they are correct based on the current environment, and make the next decision correctly. You are not an indecisive person, but you are still willing to make multiple attempts for a better success rate. You can take a different path to achieve your goals, but the methods must be effective rather than unrealistic fantasies. You are a person who respects the facts and will not confuse black and white. You will carefully examine every detail given, especially the Executed action sequence, and if it does not align with logic, you will think about the reasons behind it. You understand  natural language and can judge its structure, meaning, and correlation well"},
            {"role": "user", "content":
                """
Give you the following three parameters, please help me achieve this test code migration:

- The source program's test case code which has been transformed into an intention description.
- A list of intentions where each item represents the intended function of a component on the current page.
- A sequence of actions which has already been performed. At the end of each action of the actions, there is an identifier indicating whether the action was successfully executed: “Exec_Success” indicates successful execution, and “Exec_Fail” indicates an error in execution.These two execution states were passed in by me, so your response doesn't have to carry this.

## Requirements:

### **Process Guidance**

- **Identify the current step from the already executed actions, then decide the next step based on the available UI elements.** The relationship between the original test case and the current UI may not align perfectly, so the focus should be on meeting the functional requirements rather than finding an exact match.
- **Use the function description to understand the context and objectives of the test case, and strive to fulfill these through the UI interactions.**
- **Continue exploring and trying different interactions to find matching paths; if multiple attempts fail, then consider concluding the task.**
- **It's important to understand the text within the program to operate it effectively.**
- **Keep in mind that while both source and target apps belong to the same category, their operational logic may differ, necessitating tailored judgments based on the available information.**

### Interface Interaction

- **Avoid using elements that are not present in the current interface. Fiction and speculation are prohibited.**
- **Focus on functionality over strict element matching, as the functional description may not perfectly align with the target app. Avoid rigid adherence to element IDs or types.**
- **Move forward in the interface rather than reverting to previous pages; continuous 'RETURN' actions will lead back to the app's root page.**
- **Choose only one path if multiple options are available.**
- **Any action must only be enabled by elements present in the current interface. Multiple actions in a single step or simultaneous ACTION and RETURN are not permitted.**

### Testing Protocol

- **Once a step is completed, I will provide a new interface description for further matching.**
- **The goal is to meet the functional needs of the original test case, so avoid striving for perfect alignment with the original interface.**
- **The test should end with a 'DONE' if all actions are successfully matched.**
- **Ensure the response is concise.**
- **The description format for the interface intent includes elements like id, coordinates, text, and behavior. Avoid repeated ASSERTs.**
- **If the page appears unchanged after an action, reassess whether the performed operation was incorrect or ineffective.**

## Output Format:

Begin with the executed action and combine the following options as needed:

- 'ASSERT (element, id, coordinates, oracle):purpose': Provide an assertion if an action has been confirmed.
- 'ACTION (element, id, coordinates, action, value):purpose': Describe the interaction with an element (click, long click, input). Use 'Input' for input actions (NULL to clear input; "" for a random string). For others, the value should be NULL.
- 'RETURN:purpose': Describe the purpose of going back.
- 'DONE': Indicate that the path has been successfully matched.
- 'NOT FOUND': State when a feature doesn't exist. Explore other options before concluding this.
Enclose all responses within, wrapping them all together with a pair of '~~~' like(Please make sure to comply with this format, don't miss ~~~):
:

~~~
ACTION (element1, id1, coordinates1, action1, value1):purpose1
ASSERT (element2, id2, coordinates2, oracle):purpose2
RETURN:purpose3
ACTION (element3, id3, coordinates3, action3, value3):purpose4
DONE
~~~

## Function Description(Test code semantics): + """
                + test_semantics +
                """
## Current Page's Intent Description: """
                + page_intentions +
                """
## Executed Action Sequence: """ + actions
             },
        ],
        temperature=1
    )
    return list(response.choices)[0].to_dict()["message"]['content']

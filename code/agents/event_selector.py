import openai


def select(gpt, test_semantics, actions, page_intentions):
    openai.api_key = gpt.key
    # openai.api_base = gpt.api_base

    response = openai.ChatCompletion.create(
        model=gpt.model,
        messages=[
            {"role": "system",
             "content": "You are a project manager. You understand Android software and its operating logic. You are conducting test case migration between applications of the same type. You can examine past behaviors, judge whether they are correct based on the current environment, and make the next decision correctly. You are not an indecisive person, but you are still willing to make multiple attempts for a better success rate. You can take a different path to achieve your goals, but the methods must be effective rather than unrealistic fantasies. You are a person who respects the facts and will not confuse black and white. You will carefully examine every detail given, especially the Executed action sequence, and if it does not align with logic, you will think about the reasons behind it. You understand  natural language and can judge its structure, meaning, and correlation well"},
            {"role": "user", "content":
                """
Give you the following three parameters, please help me achieve this test code migration:
- The source application's test case which has been transformed into an semantic function description.
- A list of intentions where each item represents the intended function of a component on the current page.(each intention defined as ACTION (element, id, coordinates, action, value):purpose)
- A sequence of actions which has already been performed. At the end of each action of the actions, there is an identifier indicating whether the action was successfully executed: “Exec_Success” indicates successful execution, and “Exec_Fail” indicates an error in execution.These two execution states were passed in by me, so your response doesn't have to carry this.


## Requirements:
- You should determine which step of the test migration you are currently on based on the source test case semantics and the sequence of actions on target app already executed. Then, based on the provided intentions of the current page, decide which component should be operated on next and how to operate it. 
- Multiple steps in the source test case may be combined into one step in the target app; Similarly, a step in the source test case can be broken down into multiple steps in the target application. That is, several source test case steps may correspond to a different number of action steps in the target app. You can choose appropriate combining actions of source test case to a step of target app based on inputs information.
- Please remember that although the source app and the target app belong to the same category, their operational logic may differ. For instance, an delete task operation that is a click in the source app might be a swipe in the target app; a function that can be completed with a single UI action in the source app might require multiple actions in the target app. 
- Please focus on gradually matching each operation in the source test case, and do not attempt to complete the migration of the entire test case in a single response. Proceed step-by-step, returning only one step of the migration at a time.
- The operations on widgets don't necessarily have to match; your highest priority in matching should be functional similarity (from the actions and purposes of current page's intentions), followed by similarity in the type of action.
- You need to pay more attention to the actions of current page's intentions, as they may involve the conversion of widget operations from the source app to the target app.
- If a step of the source test case fails to match, you can consider skipping this step and matching the next step.
- You must confirm that all steps of source test case have been migrated to target app before you can respond DONE

### Input Format

For swiping operation, include the start(from) and end(to) coordinates in purpose. When you respond, don't miss these coordinates

```
~~~
ACTION (element, id, coordinates, click, value):purpose': value is the content of the element's text field. If the text field is empty, then value is NULL.
ACTION (element, id, coordinates, swipe_right, value):purpose': Swipe to right. from:[x1, y1] to:[x2, y2]. purpose.
~~~
```

## Output Format:
Begin with the executed action and combine the following options as needed:

- 'ASSERT (element, id, coordinates, oracle):purpose': Provide an assertion if an action has been confirmed.
- 'ACTION (element, id, coordinates, action, value):purpose': Describe the interaction with an element (click, long click, input). Use 'Input' for input actions (NULL to clear input; "" for a random string). For others, the value should be NULL.
- 'RETURN:purpose': Describe the purpose of going back.
- 'DONE': Indicate that the path has been successfully matched. That is to say, all steps of the source test case were successfully migrated.
- 'NOT FOUND': State when a feature doesn't exist. Explore other options before concluding this.

Enclose all responses within, wrapping them all together with a pair of '~~~' like(Please make sure to comply with this format, don't miss ~~~):

~~~
ACTION (element1, id1, coordinates1, action1, value1):purpose1
ASSERT (element2, id2, coordinates2, oracle):purpose2
RETURN:purpose3
ACTION (element3, id3, coordinates3, action3, value3):purpose4
DONE
~~~

## Function Description(Source Test code semantics): + """
                + test_semantics +
                """
## Current Page's Intent Description: """
                + page_intentions +
                """
## Executed Action Sequence: \n""" + actions
             },
        ],
        temperature=0.5
    )
    return list(response.choices)[0].to_dict()["message"]['content']

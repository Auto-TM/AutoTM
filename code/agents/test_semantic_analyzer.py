import openai



def analyze(gpt, test_code):
    openai.api_key = gpt.key
    openai.api_base = gpt.api_base


    response = openai.ChatCompletion.create(
        model = gpt.model,
        messages=[
            {"role": "system", "content": "You are a project manager. You understand Android software and its operating logic. You are conducting test case migration between applications of the same type."},
            {"role": "user", "content":
             """
Please analyze the provided Android test code and generate a corresponding function description. The descriptions should follow the specified format below:

### Format:

Incorporate the necessary components as appropriate:

- **'ASSERT (element, id, coordinates, oracle):purpose'**: If an action is verified, provide an assertion detailing the expected result.
- **'ACTION (element, id, coordinates, action, value):purpose'**: Specify the interaction with an element (click, long click, input). Use 'Input' for input actions (where NULL clears the input and "" generates a random string); for other actions, the value should be NULL.
- **'RETURN:purpose'**: Describe the purpose of returning to a previous state or screen.

Each action should be encapsulated within the following markers:

```
~~~
ASSERT (element, id, coordinates, oracle):purpose
ACTION (element, id, coordinates, action, value):purpose
RETURN:purpose
~~~
```

### Example:

#### Input:

Android test code snippet:

```
    @Test
    public void expensesTest5() {
        ViewInteraction appCompatButton4 = onView(
                allOf(withId(R.id.total_month), withText("$35.00"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.ScrollView")),
                                        0),
                                1)));
        appCompatButton4.perform(click());

        DataInteraction linearLayout = onData(anything())
                .inAdapterView(allOf(withId(R.id.listView),
                        childAtPosition(
                                withClassName(is("android.widget.LinearLayout")),
                                0)))
                .atPosition(0);
        linearLayout.perform(click());

        ViewInteraction actionMenuItemView = onView(
                allOf(withId(R.id.action_delete), withContentDescription("Delete"),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.action_bar),
                                        2),
                                0),
                        isDisplayed()));
        actionMenuItemView.perform(click());

        ViewInteraction textView = onView(
                allOf(withId(R.id.total_history), withText("$0.00"),
                        childAtPosition(
                                childAtPosition(
                                        IsInstanceOf.<View>instanceOf(android.widget.LinearLayout.class),
                                        1),
                                1),
                        isDisplayed()));
        textView.check(matches(withText("$0.00")));
    }
```

#### Output:

```
This test case is testing the functionality of deleting an existing expense of "35" from the list in Expenses App.

The detailed process with serial numbers is as follows:

1. ACTION (Button, R.id.total_month, (), click, NULL) : Click on the total month button displaying '$35.00'.
2. ACTION (LinearLayout, R.id.listView, (0), click, NULL) : Select the first expense item in the list.
3. ACTION (Menu Item, R.id.action_delete, (), click, NULL) : Click on the 'Delete' option in the action bar.
4. ASSERT (TextView, R.id.total_history, (), setText("$0.00"), NULL) : Verify the total expenses in history total $0.00.
```

### test code to be migrated: """ + test_code
             },
        ],
        temperature=1
    )
    return list(response.choices)[0].to_dict()["message"]['content']
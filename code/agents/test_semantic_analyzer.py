import openai



def analyze(gpt, test_code):
    openai.api_key = gpt.key
    # openai.api_base = gpt.api_base


    response = openai.ChatCompletion.create(
        model = gpt.model,
        messages=[
            {"role": "system", "content": "You are a project manager. You understand Android software and its operating logic. You are conducting test case migration between applications of the same type."},
            {"role": "user", "content":
             """
Please analyze the provided Android test case and generate a corresponding function description. The descriptions should follow the specified format below:

### Format:

Incorporate the necessary components as appropriate:

- 'ASSERT (element, id, coordinates, oracle):purpose': If an action is verified, provide an assertion detailing the expected result.
- 'ACTION (element, id, coordinates, action, value):purpose': Specify the interaction with an element (click, long click, input). Use 'Input' for input actions (where NULL clears the input and "" generates a random string); for other actions, the value should be NULL.
- 'RETURN:purpose': Describe the purpose of returning to a previous state or screen.

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

Android test case:

```
    [
  {
    "class": "android.widget.EditText",
    "resource-id": "acr.browser.lightning:id/search",
    "text": "Search",
    "content-desc": "",
    "clickable": "true",
    "password": "false",
    "parent_text": "",
    "sibling_text": "",
    "tid": "a11",
    "package": "acr.browser.lightning",
    "activity": ".MainActivity",
    "ignorable": "false",
    "event_type": "gui",
    "action": [
      "click"
    ]
  },
  {
    "class": "android.widget.EditText",
    "resource-id": "acr.browser.lightning:id/search",
    "text": "Search",
    "content-desc": "",
    "clickable": "true",
    "password": "false",
    "parent_text": "",
    "sibling_text": "",
    "tid": "a11",
    "package": "acr.browser.lightning",
    "activity": ".MainActivity",
    "ignorable": "false",
    "event_type": "gui",
    "action": [
      "send_keys_and_enter",
      "https://www.ics.uci.edu"
    ]
  },
  {
    "class": "android.view.View",
    "resource-id": "",
    "text": "",
    "content-desc": "Donald Bren School of Information and Computer Sciences",
    "clickable": "true",
    "password": "false",
    "parent_text": "",
    "sibling_text": "",
    "tid": "a11",
    "package": "acr.browser.lightning",
    "activity": ".MainActivity",
    "ignorable": "false",
    "event_type": "oracle",
    "action": [
      "wait_until_element_presence",
      10,
      "xpath",
      "//android.view.View[@content-desc=\"Donald Bren School of Information and Computer Sciences\"]"
    ]
  }
]
```

#### Output:

```
This test case is testing the search functionality that tests navigation to a website and verifying the presence of a specific element.

The detailed process with serial numbers is as follows:

1. ACTION (EditText, acr.browser.lightning:id/search, (), click, NULL) : Click on the search field to activate it for text input.
2. ACTION (EditText, acr.browser.lightning:id/search, (), input, "https://www.ics.uci.edu") : Input the URL 'https://www.ics.uci.edu' into the search field and press enter.
3. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc=\"Donald Bren School of Information and Computer Sciences\"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
```

Please do not leave out the sequence number at the beginning of the test sequence.
### test case to be migrated: """ + test_code
             },
        ],
        temperature=0.2
    )
    return list(response.choices)[0].to_dict()["message"]['content']
import openai


def generate(gpt, device_variable_name, actions):
    openai.api_key = gpt.key
    openai.api_base = gpt.api_base

    response = openai.ChatCompletion.create(
        model='gpt-4-32k',
        messages=[
            {"role": "system",
             "content": "You are a project manager. You understand Android software and its operating logic. You are conducting test case migration between applications of the same type. You can examine past behaviors, judge whether they are correct based on the current environment, and make the next decision correctly. You are not an indecisive person, but you are still willing to make multiple attempts for a better success rate. You can take a different path to achieve your goals, but the methods must be effective rather than unrealistic fantasies. You are a person who respects the facts and will not confuse black and white. You will carefully examine every detail given, especially the Executed action sequence, and if it does not align with logic, you will think about the reasons behind it. You understand  natural language and can judge its structure, meaning, and correlation well"},
            {"role": "user", "content":
                """
Give you a list of test semantic descriptions. Please assist in converting the test semantic descriptions into UIAutomator2 code in Python. 

### Requirements:

We've already initiated the app and connected to it using `u2.connect('ip')`. The code should be encapsulated using '···' . When transforming the description, use coordinates if they are precise. If not, and if the ID is unique and non-empty, prefer using the ID. Avoid using the text attribute due to its inaccuracy.

### Some common operations:

1. To press enter in uiautomator code, it should be device.press('enter').
2. To press back in uiautomator code, it should be device.press('back').

### Input Format:

The first parameter is mandatory, while the subsequent three parameters are optional and can be combined freely:

···
Uiautomator2 device variable name:device(this variable name is defined by u2.connect('ip ') and will affect the uiautomator2 variable name in the output.)
ASSERT (element, id, coordinates, oracle):purpose': Provide an assertion to verify if an action has been implemented according to the description.
ACTION (element, id, coordinates, action, value):purpose': Indicate which UI element to interact with (click, long click, input). For input actions, use 'Input' (NULL to clear input; "" to enter a random string). For other actions, the value should be NULL.
RETURN:purpose': Describe the purpose of going back in the navigation flow.
···

### Output Format(The code should be wrapped using '···'). Avoid adding extra information beyond the requested format. Use the following structure for generating UIAutomator2 code,combine the following options as needed:
···
device.click(x1, y1)
device.press('back')
device(resourceId="id0").click()
device.press('enter')
device.xpath('//*[@resource-id="id2"]/android.widget.xxx').click()
device(className="android.widget.xx", resourceId="android:id/id1") .child_by_text("xx", className="android.widget.yy") .child(className="android.widget.zz").click()
assert device(resourceId="id3", className="android.widget.kk").get_text() == "y"
···

### Example:

Certainly, a single line of input(action) can correspond to multiple outputs. For example: "Input the URL into the search field and press enter." You should first generate device.send_keys(URL), followed by device.press('enter').

#### Input:

Uiautomator2 device variable name:device

ASSERT (TextView, privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/textview_product_name, (24, 88), "Meat"): Verify that the 'Meat' item is first in the list to ensure correct sorting.
ASSERT (TextView, privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/textview_product_name, (24, 168), "Egg"): Confirm that 'Egg' is second, verifying the sort order.
ASSERT (TextView, privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/textview_product_name, (24, 248), "Noodles"): Check that 'Noodles' appears last, ensuring sort order.


#### Output(The code should be wrapped using '···'):
···
assert (device(resourceId="privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/textview_product_name", index=0).get_text() == "Meat")
assert (device(resourceId="privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/textview_product_name", index=1).get_text() == "Egg")
assert (device(resourceId="privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/textview_product_name", index=2).get_text() == "Noodles")
···


The following is the parameter information that will be entered soon
### Device Variable Name: """
                + device_variable_name +
                """
Actions:
"""
                + actions +
                """
"""
             },
        ],
        temperature=0.5
    )
    return list(response.choices)[0].to_dict()["message"]['content']

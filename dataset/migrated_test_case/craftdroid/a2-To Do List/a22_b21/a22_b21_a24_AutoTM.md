## a22's b21 to a24

### Semantics of Source Test case
> This test case is testing the functionality of adding a new todo item in the application and verifying its presence in the list.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (ImageButton, douzifly.list:id/fab_add, (), click, NULL) : Click on the add button to create a new todo item.
> 2. ACTION (EditText, douzifly.list:id/edit_text, (), input, "Sample Todo") : Input the text 'Sample Todo' into the title field and hide the keyboard.
> 3. ACTION (ImageButton, douzifly.list:id/fab_add, (), click, NULL) : Click on the add button to save the new todo item.
> 4. ASSERT (TextView, douzifly.list:id/txt_thing, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]") : Verify that the todo item with the text 'Sample Todo' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): The clickable title bar of the app. Clicking this does not change the page, as both current and next JSON page are similar with no new elements introduced.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to edit the name of the new list. The page after clicking this control is the list page, where you can add new tasks to the list.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), longClick, NULL): Long click to paste the copied text into 'New List Name'. The page after long clicking this control shows the 'Paste' button.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add a new list. The page after clicking this control is the same current page with the ability to add more lists.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to edit the name of the new list. This action corresponds to the first step of the source test case, which is to create a new todo item.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the text 'Sample Todo' into the title field. This action corresponds to the second step of the source test case, which is to input the text 'Sample Todo' into the title field.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add a new list. This action corresponds to the third step of the source test case, which is to save the new todo item.
ASSERT (android.widget.TextView, android:id/title, (6, 25), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds. This action corresponds to the fourth step of the source test case, which is to verify the presence of the new todo item in the list.
DONE
~~~
Based on the provided semantic descriptions, the corresponding UIAutomator2 code in Python should be:

```python
# Click to edit the name of the new list
d(resourceId="kdk.android.simplydo:id/AddListEditText").click()

# Input the text 'Sample Todo' into the title field
d(resourceId="kdk.android.simplydo:id/AddListEditText").set_text("Sample Todo")

# Click to add a new list
d(resourceId="kdk.android.simplydo:id/AddListButton").click()

# Verify that the todo item with the text 'Sample Todo' is present within 10 seconds
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').wait(timeout=10)
```
This code first performs actions to create a new todo item with the name "Sample Todo", and then verifies that the new item appears in the list within 10 seconds.
````
### Success
````
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to edit the name of the new list. This action corresponds to the first step of the source test case, which is to create a new todo item., Exec_Success
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the text 'Sample Todo' into the title field. This action corresponds to the second step of the source test case, which is to input the text 'Sample Todo' into the title field., Exec_Success
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add a new list. This action corresponds to the third step of the source test case, which is to save the new todo item., Exec_Success
ASSERT (android.widget.TextView, android:id/title, (6, 25), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds. This action corresponds to the fourth step of the source test case, which is to verify the presence of the new todo item in the list., Exec_Success
DONE
````

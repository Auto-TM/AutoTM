## a24's b21 to a25

### Semantics of Source Test case
> This test case is testing the functionality of adding a new to-do list and verifying the presence of the created list.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (EditText, kdk.android.simplydo:id/AddListEditText, (), input, "Sample Todo") : Input the text 'Sample Todo' into the 'New List Name' field and hide the keyboard.
> 2. ACTION (Button, kdk.android.simplydo:id/AddListButton, (), click, NULL) : Click on the 'Add' button to create a new to-do list with the given name.
> 3. ASSERT (TextView, kdk.android.simplydo:id/text1, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]") : Verify that the element with the text 'Sample Todo' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate up. The page after clicking this control is the navigation drawer page, which allows users to navigate between different sections of the application.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete all selected or checked shopping list items. The page after clicking will present a confirmation dialog asking "Remove all checked items?" with "OK" and "Cancel" options.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), longClick, NULL): Long Click to delete checked items from the shopping list. The subsequent page after the long click action is the same shopping list page, with the checked items deleted.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to navigate to more options. The next page includes various options such as sort, create a new list, share, delete list, about, and settings.
ACTION (android.widget.ImageView, More options, (280, 28), longClick, NULL): Long click to open more options. The page after long clicking this control remains more or less the same, containing options for shopping list view, and add item button.
ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), long_click, NULL): Long click to interact with the shopping list view. The next page remains unchanged, indicating no changes or updates to the shopping list are made with this interaction.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. The next page is the new item page where you can type in the item description, quantity, and add the item to the list.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to navigate to more options. This action is taken to access the option to create a new list.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. This action is taken to create a new to-do list.
ACTION (EditText, kdk.android.simplydo:id/AddListEditText, (), input, "Sample Todo"): Input the text 'Sample Todo' into the 'New List Name' field and hide the keyboard. This action is taken to name the new to-do list.
ACTION (Button, kdk.android.simplydo:id/AddListButton, (), click, NULL): Click on the 'Add' button to create a new to-do list with the given name. This action is taken to confirm the creation of the new to-do list.
ASSERT (TextView, kdk.android.simplydo:id/text1, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the element with the text 'Sample Todo' is present within 10 seconds. This action is taken to verify the creation of the new to-do list.
DONE
~~~
Based on the provided input, here is the corresponding UIAutomator2 code in Python:

```python
d(resourceId="com.woefe.shoppinglist:id/fab_add").click()
d(resourceId="kdk.android.simplydo:id/AddListEditText").send_keys("Sample Todo")
d.press('enter')
d(resourceId="kdk.android.simplydo:id/AddListButton").click()
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').wait(timeout=10)
```

In the above code, the variable 'd' is your device which is already connected using `u2.connect('ip ')`. The 'click' function is used for clicking on a specific UI element with the given resourceId. The 'send_keys' function is used to enter text into a text field. The 'press' function is used to press a key, in this case, the 'enter' key. The 'wait' function is used to wait for the specified element to appear within the given timeout period.
````
### Success
````
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to navigate to more options. This action is taken to access the option to create a new list., Exec_Success
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. This action is taken to create a new to-do list., Exec_Fail
ACTION (EditText, kdk.android.simplydo:id/AddListEditText, (), input, "Sample Todo"): Input the text 'Sample Todo' into the 'New List Name' field and hide the keyboard. This action is taken to name the new to-do list., Exec_Success
ACTION (Button, kdk.android.simplydo:id/AddListButton, (), click, NULL): Click on the 'Add' button to create a new to-do list with the given name. This action is taken to confirm the creation of the new to-do list., Exec_Fail
ASSERT (TextView, kdk.android.simplydo:id/text1, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the element with the text 'Sample Todo' is present within 10 seconds. This action is taken to verify the creation of the new to-do list., Exec_Success
DONE
````

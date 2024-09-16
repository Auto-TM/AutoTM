## a25's b21 to a24

### Semantics of Source Test case
> This test case is testing the functionality of adding a new item to the shopping list and verifying the presence of the added item.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (ImageButton, com.woefe.shoppinglist:id/fab_add, (), click, NULL) : Click on the add button to create a new item in the shopping list.
> 2. ACTION (EditText, com.woefe.shoppinglist:id/new_item_description, (), input, "Sample Todo") : Input the description 'Sample Todo' for the new item and hide the keyboard.
> 3. ACTION (ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (), click, NULL) : Click on the 'Done' button to add the new item to the shopping list.
> 4. ASSERT (TextView, com.woefe.shoppinglist:id/text_description, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]") : Verify that the item with the description 'Sample Todo' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): Click to interact with the app. The page after clicking this control remains the same with varying interaction possibilities with different list items and the provision to add a new list.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Clicking to enter the name of the new list. After clicking, the user can enter the name and save it to the database after clicking the add button. The next page will still be the homepage with a new list added.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), long_click, NULL): Long click to edit the list name. The paste control appears after long clicking, indicating that the text can be replaced with the clipboard content.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add a new list. After clicking this "Add" button, it should add a new list item in the existing list seen from Next Page JSON.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click to select a list. The page after clicking this control takes the user to a detailed view of the selected sample to-do list, providing options to add a new item to this list.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), longClick, NULL): Long click to view options for the list. After a long click, the next page gives an option to add a new item to the 'Sample Todo' list.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), scroll, NULL): Scroll through the list. The next page after scrolling this control is the sample Todo list page, which contains an option to add a new item.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), click, NULL): Click to view the details of the selected Todo. The subsequent page provides options to add a new item to the selected Todo list.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text2, (278, 113), click, NULL): Click to go through the list and view the details. The next page will be the list details page, which has an Add function to add new items to the list.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the description 'Sample Todo' for the new list.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click on the 'Add' button to create a new list with the name 'Sample Todo'.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click on the list named 'Sample Todo' to view its details.
ASSERT (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the list with the name 'Sample Todo' is present.
~~~
Here is the Python code using UIAutomator2:

···
d(resourceId="kdk.android.simplydo:id/AddListEditText").set_text("Sample Todo")
d(resourceId="kdk.android.simplydo:id/AddListButton").click()
d(resourceId="kdk.android.simplydo:id/ListsListView").click()
assert d(resourceId="kdk.android.simplydo:id/text1").wait(timeout=10.0).get_text() == "Sample Todo"
···

In the code above, we first set the text of the EditText field to "Sample Todo". Then, we click the 'Add' button. After that, we click on the ListView to view the details of the list. Lastly, we assert that the TextView field displays "Sample Todo".
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): Click to navigate to the details of the Todo item. The page after clicking this control is the detailed view of the Todo item, which has a field to input item name and an "Add" button.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddItemEditText, (0, 49), click, NULL): Click to create a new item. The page after clicking this control is again the item creation page, with the text field reset for adding another item.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddItemEditText, (0, 49), longClick, NULL): Long click to edit the item's name. The page after long clicking this control is the edit item name page, which has a Paste button and an add item component.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddItemButton, (273, 51), click, NULL): Click to add a new item. The next page after clicking this control retains the same structure, implying the item addition is managed on the current page itself.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddItemEditText, (0, 49), input, "Sample Todo"): Input the description 'Sample Todo' for the new item.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddItemButton, (273, 51), click, NULL): Click on the 'Add' button to add the new item to the list.
ASSERT (android.widget.TextView, android:id/title, (6, 25), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the item with the description 'Sample Todo' is present within the list.
DONE
~~~
Based on the given input, here is the UIAutomator2 code in Python.

```python
d(resourceId="kdk.android.simplydo:id/AddItemEditText").set_text("Sample Todo")
d(resourceId="kdk.android.simplydo:id/AddItemButton").click()
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').wait(timeout=10.0)
```

The first line inputs the description 'Sample Todo' for the new item. The second line clicks on the 'Add' button to add the new item to the list. The last line verifies that the item with the description 'Sample Todo' is present within the list.
````
### Success
````
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the description 'Sample Todo' for the new list., Exec_Success
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click on the 'Add' button to create a new list with the name 'Sample Todo'., Exec_Success
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click on the list named 'Sample Todo' to view its details., Exec_Success
ASSERT (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the list with the name 'Sample Todo' is present., Exec_Success

ACTION (android.widget.EditText, kdk.android.simplydo:id/AddItemEditText, (0, 49), input, "Sample Todo"): Input the description 'Sample Todo' for the new item., Exec_Success
ACTION (android.widget.Button, kdk.android.simplydo:id/AddItemButton, (273, 51), click, NULL): Click on the 'Add' button to add the new item to the list., Exec_Success
ASSERT (android.widget.TextView, android:id/title, (6, 25), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the item with the description 'Sample Todo' is present within the list., Exec_Success
DONE
````

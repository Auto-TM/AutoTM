## a21's b21 to a24

### Semantics of Source Test case
> This test case is testing the functionality of adding a new to-do item in the MinimalTodo app and verifying its presence in the main activity.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (ImageButton, com.rubenroy.minimaltodo:id/addToDoItemFAB, (), click, NULL) : Click on the 'Add ToDo Item' button to initiate the process of adding a new to-do item.
> 2. ACTION (EditText, com.rubenroy.minimaltodo:id/userToDoEditText, (), input, "Sample Todo") : Input the text 'Sample Todo' into the title field for the new to-do item and hide the keyboard.
> 3. ACTION (ImageButton, com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton, (), click, NULL) : Click on the 'save' button to add a new item.
> 4. ASSERT (TextView, com.rubenroy.minimaltodo:id/toDoListItemTextview, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]") : Verify that the new to-do item with the text 'Sample Todo' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): The clickable title bar of the app. Clicking this does not change the page, as both current and next JSON page are similar with no new elements introduced.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to edit the name of the new list. The page after clicking this control is the list page, where you can add new tasks to the list.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add a new list. The page after clicking this control is the same current page with the ability to add more lists.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the text 'Sample Todo' into the title field for the new to-do item.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click on the 'Add' button to add a new item.
~~~
Based on your requirements, here is the transformed UIAutomator2 code in Python:

···
d(resourceId="kdk.android.simplydo:id/AddListEditText").send_keys("Sample Todo")
d(resourceId="kdk.android.simplydo:id/AddListButton").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): Clicking to interact with the app title. The subsequent page remains the same, indicating no observable actions are performed.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to enter a new list name. The page after clicking remains the same but allows for text input into the field for creating a new list.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add the list. The page after clicking this control remains the same except the new list would be added to the ListView control.

ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click to view the details of the list. After clicking the control, the page displays more list items.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), click, NULL): Click to view the Sample Todo list. The next page displays the Sample Todo list with options to add items.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text2, (278, 113), click, NULL): Click to enter the to-do list named "Sample Todo". The page after clicking this control is the to-do item list page, which has a "New Item Name" input box and an "Add" button for adding new items.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), click, NULL): Click to view the Sample Todo list.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text2, (278, 113), click, NULL): Click to enter the to-do list named "Sample Todo".
ASSERT (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the new to-do item with the text 'Sample Todo' is present within 10 seconds.
DONE
~~~
Based on the provided actions and assertions, the following UIAutomator2 code in Python can be generated:

```python
# Click to view the Sample Todo list.
d(resourceId="kdk.android.simplydo:id/text1").click()

# Click to enter the to-do list named "Sample Todo".
d(resourceId="kdk.android.simplydo:id/text2").click()

# Verify that the new to-do item with the text 'Sample Todo' is present within 10 seconds.
assert d(resourceId="kdk.android.simplydo:id/ListsListView").child_by_text("Sample Todo", className="android.widget.TextView").wait(timeout=10)
```

Please note that the provided semantic descriptions are converted into Python UIAutomator2 code. It is assumed that the device is already connected and the app is initiated.
````
### Success
````
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the text 'Sample Todo' into the title field for the new to-do item., Exec_Success
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click on the 'Add' button to add a new item., Exec_Success

ACTION (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), click, NULL): Click to view the Sample Todo list., Exec_Success
ACTION (android.widget.TextView, kdk.android.simplydo:id/text2, (278, 113), click, NULL): Click to enter the to-do list named "Sample Todo"., Exec_Success
ASSERT (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the new to-do item with the text 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

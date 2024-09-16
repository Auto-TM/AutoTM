## a23's b21 to a24

### Semantics of Source Test case
> This test case is testing the task creation functionality in the Privacy Friendly To-Do List application. It tests the process of skipping the tutorial, creating a new task, and verifying the presence of the created task.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (Button, org.secuso.privacyfriendlytodolist:id/btn_skip, (), click, NULL) : Click on the 'Skip' button to bypass the tutorial.
> 2. ACTION (ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (), click, NULL) : Click on the 'New Task' button to open the task creation interface.
> 3. ACTION (EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (), input, "Sample Todo") : Input the task name 'Sample Todo' into the task name field.
> 4. ACTION (Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (), click, NULL) : Click on the 'Okay' button to create the task.
> 5. ASSERT (TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]") : Verify that the task with the name 'Sample Todo' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): Clicking to interact with the app title. The subsequent page remains the same, indicating no observable actions are performed.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to enter a new list name. The page after clicking remains the same but allows for text input into the field for creating a new list.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), longClick, NULL): Long click to edit the list name. The page after long clicking this control shows an option to Paste.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add the list. The page after clicking this control remains the same except the new list would be added to the ListView control.

ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click to open existing lists. The next page after clicking this control is the list page, which includes a field for adding new item name and an 'Add' button to add the new item to the list.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), long click, NULL): Long click to open the selected list. The next page to be displayed contains a text field for a new item name and an add button, indicating you are in the list details, where you can add items into the list.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), click, NULL): Click to view the Sample Todo list. The next page displays the Sample Todo list with options to add items.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text2, (278, 113), click, NULL): Click to enter the to-do list named "Sample Todo". The page after clicking this control is the to-do item list page, which has a "New Item Name" input box and an "Add" button for adding new items.

````

#### Selected Event(s) and Script
````
Based on the given parameters, the next step should be to create a new task. Since the current page's intent description includes an action to enter a new list name, this action aligns with the next step in the function description. Here is the next action:

~~~
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the task name 'Sample Todo' into the task name field.
~~~
Based on the given parameters, here is the UIAutomator2 code in Python:

···
d(resourceId="kdk.android.simplydo:id/AddListEditText").set_text("Sample Todo")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): Click to switch to the list view. The page after clicking doesn't change the UI, but makes 'Sample Todo' list available for further operations.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to input new to-do list. The page after clicking this control is a prompt page offering suggestions or corrections for inputs.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), long_click, NULL): Long click to display the edit menu including paste and select all options. The page after long clicking this control has buttons for pasting, selecting all, and more options.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add a new list. The page after clicking this control shows an additional list item in the ListsListView component.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): The list item in the "Simply Do" app is clicked. The next page displays the detailed view of the list item.
~~~
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), long_click, NULL): Long click to interact with the list in the ListView. The next page shows an updated list with additional items.
~~~
ACTION (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), click, NULL): Click to view the selected list. The next page after clicking this control is the list details page, which has fields for adding new items to the list.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text2, (278, 113), click, NULL): Click to view the to-do list. The page after clicking this control is the list details page, which has an add item input field and an add item button.

````

#### Selected Event(s) and Script
````
Based on the executed action sequence, the task name 'Sample Todo' has been successfully inputted into the task name field. The next step is to add this new task to the list. 

~~~
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add the new task 'Sample Todo' to the list.
~~~
Based on the provided information, here is the UIAutomator2 code in Python:

···
d(resourceId="kdk.android.simplydo:id/AddListButton").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/title, (6, 25), click, NULL): Click to access the title of the page. After clicking, it stays on the current page without moving to other pages, and the sample todo items along with their status remain the same.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), click, NULL): Click to edit the name of the new list. The page after clicking this control is the list page, which allows for adding lists and viewing existing lists.
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), long_click, NULL): Long click to interact with the add list input field. The next page contains additional pasting options with a paste button on the screen.
ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add a new list. After clicking, the newly added list will appear in the list view on the current page.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click to select a list. The subsequent page displays the 'Sample Todo' list items with details, indicating that this operation allows the user to view and manage the selected list items.
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), longClick, NULL): Long click to interact with the list. Once this control is long clicked, the next page is the ToDo list page where new items can be added to the list.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), click, NULL): Click to navigate to the detailed view of 'Sample Todo' list. After clicking, it goes to the page where you can add new items to 'Sample Todo' list.
ACTION (android.widget.TextView, kdk.android.simplydo:id/text2, (278, 113), click, NULL): Click on this widget to navigate to a new page where you can add a new item name.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click to select the 'Sample Todo' list. The subsequent page should display the 'Sample Todo' list items with details.
ASSERT (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the task with the name 'Sample Todo' is present within 10 seconds.
DONE
~~~
Based on the input, here is the UIAutomator2 code in Python:

```python
d(resourceId="kdk.android.simplydo:id/ListsListView").click()
assert d(resourceId="kdk.android.simplydo:id/text1").wait_timeout(10).exists
```

Please note that the 'click' action is performed on the 'ListsListView' element identified by its resourceId. After that, we assert that the 'Sample Todo' text is present within the 'text1' element, and we wait for up to 10 seconds for this element to appear.
````
### Success
````
ACTION (android.widget.EditText, kdk.android.simplydo:id/AddListEditText, (0, 49), input, "Sample Todo"): Input the task name 'Sample Todo' into the task name field., Exec_Success

ACTION (android.widget.Button, kdk.android.simplydo:id/AddListButton, (273, 49), click, NULL): Click to add the new task 'Sample Todo' to the list., Exec_Success

ACTION (android.widget.ListView, kdk.android.simplydo:id/ListsListView, (0, 99), click, NULL): Click to select the 'Sample Todo' list. The subsequent page should display the 'Sample Todo' list items with details., Exec_Success
ASSERT (android.widget.TextView, kdk.android.simplydo:id/text1, (10, 109), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the task with the name 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

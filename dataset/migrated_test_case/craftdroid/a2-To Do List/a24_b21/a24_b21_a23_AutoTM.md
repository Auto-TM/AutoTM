## a24's b21 to a23

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
ACTION (android.widget.ImageButton, Open menu, (0, 24), click, NULL): Click to open the navigation menu. The page after clicking this control is the navigation menu page, which has multiple menu options like "All tasks", "Calendar", "Recycler", "Tutorial" and sample to-do list items.
ACTION (android.widget.ImageButton, NULL, (0, 24), longclick, NULL): Long-click to open the menu. The page after this action remains the same with the menu open.
ACTION (android.widget.TextView, To-Do List, (72, 38), click, NULL): Click to interact with the To-Do list. Post click, the Next Page appears the same as the current page, indicating no primary changes in GUI elements after this interaction.
ACTION (android.widget.ExpandableListView, org.secuso.privacyfriendlytodolist:id/exlv_tasks, (0, 80), long_click, NULL): Long click on the To-Do List to access additional options. After this interaction, the next page remains the same with the To-Do List view.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/ac_add, (232, 28), click, NULL): Click to open the "New To-Do list" page. This action will allow you to input the list name and confirm or cancel the creation of a new list.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to access more options such as Search, All tasks, Open tasks, Completed tasks, Group by priority, and Sort by deadline.
ACTION (android.widget.ImageView, "", (280, 28), longClick, NULL): The long click action on "More options" expands the accessible features of the app.
ACTION (android.widget.RelativeLayout, org.secuso.privacyfriendlytodolist:id/rl_exlv_task_group_root, (0, 80), click, NULL): Clicking on the task group opens up an expanded view of the tasks. The next page includes a detailed view of the task list and the option to add subtasks.
ACTION (android.widget.RelativeLayout, org.secuso.privacyfriendlytodolist:id/rl_exlv_task_group_root, (160, 116), long_click, NULL): Long click to activate task group options. The page has no subsequent elements after this interaction.
ACTION (android.widget.CheckBox, org.secuso.privacyfriendlytodolist:id/cb_task_done, (15, 100), click, NULL): Click to check or uncheck the task. The task status updated and reflected on the todo list on the next page.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name, (55, 90), click, NULL): Click to view details of the "Sample Todo" task. The next page, shown after clicking, displays details of the task including options to add a sub-task and mark the task as completed.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_deadline, (55, 115), click, NULL): Opens the task edit page, where more details of the task are provided, or the task can be modified.
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Clicking on this element opens the "New To-Do task" dialog on the next page, where users can enter task name, description, deadline, reminder, progress, priority, and select lists, and either cancel or confirm the task creation using the "Cancel" or "Okay" buttons.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Click to open the "New To-Do task" dialog
~~~
The generated UIAutomator2 code based on the provided parameters is as follows:

···
d(resourceId="org.secuso.privacyfriendlytodolist:id/fab_new_task").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/dialog_title, (16, 130), click, NULL): Click to create new To-Do task. The page after clicking contains elements to set task name, description, deadline, reminder, progress, priority, and task list.
ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (26, 205), click, NULL): The purpose is to input a name for the new To-Do task. After clicking, you can enter the task name in the input area.

ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_description, (26, 252), click, NULL): Clicking on the Description field enables the user to enter the description of their new To-Do task. The subsequent screen remains the same as the current page but allows for the entered description to be saved for the task.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_todo_list_deadline, (26, 299), click, NULL): Clicking this will bring up a date picker dialog for setting a task deadline. This includes options for previous and next month, choosing a specific date, choosing "No Deadline" and confirming your selected date.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_todo_list_reminder, (160, 299), click, NULL): Click to set reminder for the task. The page after this interaction is a reminder setting page, providing date and time options to set the reminder.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_task_progress, (31, 357), click, NULL): Click to reveal task progress. After click, user remains in the task details page with all components accessible.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/new_task_progress, (116, 381), click, NULL): Click to update the progress percentage of a new task. The page after clicking this control remains the same, which has the option to set Name, Description, Deadline, Reminder, Priority and List of the new task.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_new_task_priority, (132, 420), click, NULL): Selects the priority level for the new task. After clicking, the screen remains on the current page, allowing the user to further edit the new task's details.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_new_task_priority_str, (31, 420), longClick, NULL): The text view is longClicked to modify the priority of a new task. After the interaction, the task's priority can be modified on the same page.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_new_task_listchoose_str, (31, 452), click, NULL): Click to select list. The subsequent page opens a text field to enter the select task list.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_new_task_listchoose, (132, 452), click, NULL): Click to select a list for the new task. The page after this action is currently unknown based on the provided Next Page JSON.
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_cancel, (94, 485), click, NULL): Click to exit the current 'New To-Do task' page and return to the 'To-Do List' page. The 'To-Do List' page features such widgets as the Add List button, More options button and the tasks in the list among other controls.
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Clicking on 'Okay' after defining a To-Do task. The next page is still on new task creation window, potentially for correcting or fine-tuning task details.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (26, 205), input, "Sample Todo"): Input the text 'Sample Todo' into the 'New Task Name' field.
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Click on the 'Okay' button to create a new to-do task with the given name.
ASSERT (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/dialog_title, (16, 130), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the element with the text 'Sample Todo' is present within 10 seconds.
DONE
~~~
Based on the given parameters, the corresponding UIAutomator2 code in Python would be:

···
d(resourceId="org.secuso.privacyfriendlytodolist:id/et_new_task_name").send_keys("Sample Todo")
d(resourceId="org.secuso.privacyfriendlytodolist:id/bt_new_task_ok").click()
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').wait(timeout=10)
···

The first line of the code inputs the text 'Sample Todo' into the 'New Task Name' field. The second line clicks on the 'Okay' button to create a new to-do task with the given name. The last line verifies that the element with the text 'Sample Todo' is present within 10 seconds.
````
### Success
````
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Click to open the "New To-Do task" dialog, Exec_Success

ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (26, 205), input, "Sample Todo"): Input the text 'Sample Todo' into the 'New Task Name' field., Exec_Success
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Click on the 'Okay' button to create a new to-do task with the given name., Exec_Success
ASSERT (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/dialog_title, (16, 130), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the element with the text 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

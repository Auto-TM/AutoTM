## a22's b21 to a23

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
ACTION (android.widget.ImageButton, Open menu, (0, 24), click, NULL): Opens the main menu. The next page after clicking this control presents various options such as "All tasks", "Calendar", "Recycler", Tutorial", "Sample Todo", "Settings", "Help", "About". The page also contains an option to close the menu.
ACTION (android.widget.ImageButton, NULL, (0, 24), longclick, NULL): Long press to open the menu. After this interaction, the page remains the same, but with the menu open, revealing additional interactive options.
ACTION (android.widget.TextView, To-Do List, (72, 38), click, NULL): Click to view the dedicated To-Do list. The next page appears to be the same, suggesting the action refreshes the current page.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/ac_add, (232, 28), click, NULL): Click to add a new task. The next page, which opens when you click, is the 'New To-Do list' page where you can enter the name of the task and either approve by clicking 'Okay' or Cancel the operation.
ACTION (android.widget.ImageView, "", (280, 28), click, NULL): Click to open menu options. The next page displays search, view tasks by type, group by priority, and sort by deadline options.
ACTION (android.widget.ImageView, More options, (280, 28), long_click, NULL): Long clicking 'More options' displayed the same list page with no changes, maintaining the same state without additional options.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_empty_view_no_tasks, (0, 80), click, NULL): Click to open the 'No tasks available' prompt.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/second_alert, (107, 587), click, NULL): The user is able to click on the "ADD NEW TASK >" button to create a new task in the To-Do list. After clicking, the page remains the same allowing the user to add more tasks continuously if needed.
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Opens the New To-Do task form with various input fields for Name, Description, Deadline, Reminder, Progress, Priority and List selection. The page has an 'Okay' button to submit the task and a 'Cancel' button to close the form.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Click on the add button to create a new todo item.
~~~
Based on the provided input, here's the generated UIAutomator2 code in Python:

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
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_cancel, (94, 485), click, NULL): The purpose of clicking the cancel button is to exit the task creation, and return to the original page where you can add a new task or view the existing task list.
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Clicking on 'Okay' after defining a To-Do task. The next page is still on new task creation window, potentially for correcting or fine-tuning task details.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (26, 205), input, "Sample Todo"): Input the text 'Sample Todo' into the title field.
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Click on the 'Okay' button to save the new todo item.
ASSERT (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/dialog_title, (16, 130), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds.
DONE
~~~
Based on your instructions, the Uiautomator2 code in Python should be:

···
d(resourceId="org.secuso.privacyfriendlytodolist:id/et_new_task_name").send_keys("Sample Todo")
d(resourceId="org.secuso.privacyfriendlytodolist:id/bt_new_task_ok").click()
assert d(resourceId="org.secuso.privacyfriendlytodolist:id/dialog_title").wait(timeout=10).exists
···
````
### Success
````
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Click on the add button to create a new todo item., Exec_Success

ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (26, 205), input, "Sample Todo"): Input the text 'Sample Todo' into the title field., Exec_Success
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Click on the 'Okay' button to save the new todo item., Exec_Success
ASSERT (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/dialog_title, (16, 130), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

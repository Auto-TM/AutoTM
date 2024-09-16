## a25's b21 to a23

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
ACTION (android.widget.ImageButton, Open menu, (0, 24), click, NULL): Opens the app sidebar for various options such as "All tasks", "Calendar", "Recycler", and "Tutorial". The page after clicking this control changes to a navigation view page with options to navigate various sections of the application.
ACTION (android.widget.TextView, To-Do List, (72, 38), click, NULL): This action opens the To-Do List page, where tasks can be viewed or added.

ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/ac_add, (232, 28), click, NULL): Clicking this control opens the "New To-Do list" page with elements such as Name input field, Cancel button, and Okay button.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to open menu options including 'Search', 'All tasks', 'Open tasks', 'Completed tasks', 'Group by priority', and 'Sort by deadline'.
ACTION (android.widget.ExpandableListView, org.secuso.privacyfriendlytodolist:id/exlv_tasks, (0,80), click, NULL): Click to interact with the task list. After this action, the task list remains on the page, where each task can be clicked or long clicked for further interaction. This action may also lead to the expansion of individual tasks, revealing more details.
ACTION (android.widget.ExpandableListView, org.secuso.privacyfriendlytodolist:id/exlv_tasks, (0, 80), longClick, NULL): Long-press to open further options or details for a specific task on the list. After the interaction, the list of tasks remains but with availability of selecting the tasks and enabling additional tasks options.
ACTION (android.widget.RelativeLayout, org.secuso.privacyfriendlytodolist:id/rl_exlv_task_group_root, (0, 80), click, NULL): Opens the todo list item for further interactions like viewing details or editing. This action made an appearance of 'Add Subtask' button in the page, indicating a subtask can be added to this todo item.
ACTION (android.widget.RelativeLayout, org.secuso.privacyfriendlytodolist:id/rl_exlv_task_group_root, (0, 152), swipe, NULL): Swipe to left. from:[320, 152] to:[0, 80] for performing the task deletion. After swiping, the tasks list remains, excluding the deleted task.
ACTION (android.widget.CheckBox, org.secuso.privacyfriendlytodolist:id/cb_task_done, (15, 100), click, NULL): Mark the task as completed or not completed. The page after clicking this control remains the same, with the task checkbox status updated.
ACTION (android.widget.CheckBox, org.secuso.privacyfriendlytodolist:id/cb_task_done, (15,100), long click, NULL): Long click to select the task as done. The page after long clicking this control is the same task list page, which has the same control and list elements.

ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name, (55, 90), click, NULL): Click to view and edit the task details. The next page after clicking this control includes the task information along with options to add subtasks and edit the task.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_deadline, (55, 115), click, NULL): This interaction opens the task detail where the deadline of the task can be set or edited. The next page includes the components necessary for task details and editing including options like 'Add Subtask'.
ACTION (android.widget.CheckBox, org.secuso.privacyfriendlytodolist:id/cb_task_done, (15, 172), swipe, NULL): Swipe to right from:[15, 172] to:[47, 204] to mark the task as done. The next page reflects the task completion with the absence of the done task and a message indicating no tasks available or to add a new task, depending on the number of remaining tasks.
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): To create a new task. After clicking this button, a New To-Do task page shows up that allows users to enter task details, specify deadlines, set reminders, define task progress and priority, and choose the task list.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Click on the add button to create a new item in the To-Do list.
~~~
Based on the provided parameters, the UIAutomator2 code in Python would be:

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
ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (26, 205), input, "Sample Todo"): Input the name 'Sample Todo' for the new task.
ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_description, (26, 252), input, "Sample Todo"): Input the description 'Sample Todo' for the new task.
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Click on the 'Okay' button to add the new task to the To-Do list.
~~~
### Device Variable Name: d

Actions:

···
d(resourceId="org.secuso.privacyfriendlytodolist:id/et_new_task_name").send_keys("Sample Todo")
d(resourceId="org.secuso.privacyfriendlytodolist:id/et_new_task_description").send_keys("Sample Todo")
d(resourceId="org.secuso.privacyfriendlytodolist:id/bt_new_task_ok").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, Open menu, (0, 24), click, NULL): Click to open the navigation menu. The page after clicking this control is the navigation menu page, which has multiple menu options like "All tasks", "Calendar", "Recycler", "Tutorial" and sample to-do list items.
ACTION (android.widget.ImageButton, NULL, (0, 24), longclick, NULL): Long-click to open the menu. The page after this action remains the same with the menu open.
ACTION (android.widget.TextView, To-Do List, (72, 38), click, NULL): Click to interact with the To-Do list. Post click, the Next Page appears the same as the current page, indicating no primary changes in GUI elements after this interaction.
ACTION (android.widget.ExpandableListView, org.secuso.privacyfriendlytodolist:id/exlv_tasks, (0, 80), long_click, NULL): Long click on the To-Do List to access additional options. After this interaction, the next page remains the same with the To-Do List view.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/ac_add, (232, 28), click, NULL): Click to open the "New To-Do list" page. This action will allow you to input the list name and confirm or cancel the creation of a new list.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to access more options such as Search, All tasks, Open tasks, Completed tasks, Group by priority, and Sort by deadline.
ACTION (android.widget.ImageView, "", (280, 28), longClick, NULL): The long click action on "More options" expands the accessible features of the app.
ACTION (android.widget.RelativeLayout, org.secuso.privacyfriendlytodolist:id/rl_exlv_task_group_root, (0, 80), click, NULL): Clicking on this will expand the details of this to-do item. In the next screen, it shows task description and an option to add subtasks.
ACTION (android.widget.RelativeLayout, org.secuso.privacyfriendlytodolist:id/rl_exlv_task_group_root, (160, 116), long_click, NULL): Long click to activate task group options. The page has no subsequent elements after this interaction.
ACTION (android.widget.CheckBox, org.secuso.privacyfriendlytodolist:id/cb_task_done, (15, 100), click, NULL): Click to check or uncheck the task. The task status updated and reflected on the todo list on the next page.
ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name, (55, 90), click, NULL): Click to expand the task details. After clicking this control, the details of the task 'Sample Todo' with description and the 'Add Subtask' button are visible.

ACTION (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_deadline, (55, 115), click, NULL): Clicking on the "No deadline" TextView in the todo task does not initiate any changes or yield any new widgets on the page.
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Clicking on this element opens the "New To-Do task" dialog on the next page, where users can enter task name, description, deadline, reminder, progress, priority, and select lists, and either cancel or confirm the task creation using the "Cancel" or "Okay" buttons.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name, (55, 90), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the task with the name 'Sample Todo' is present within 10 seconds.
DONE
~~~
Based on the information provided, the following is the generated UIAutomator2 code:

```python
assert d(resourceId="org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name").wait(timeout=10)
assert d(resourceId="org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name").get_text() == "Sample Todo"
```
This code first waits for the TextView with the specified resourceId to be present within 10 seconds, and then verifies that the text of the TextView is 'Sample Todo'.
````
### Success
````
ACTION (android.widget.ImageButton, org.secuso.privacyfriendlytodolist:id/fab_new_task, (248, 568), click, NULL): Click on the add button to create a new item in the To-Do list., Exec_Success

ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_name, (26, 205), input, "Sample Todo"): Input the name 'Sample Todo' for the new task., Exec_Success
ACTION (android.widget.EditText, org.secuso.privacyfriendlytodolist:id/et_new_task_description, (26, 252), input, "Sample Todo"): Input the description 'Sample Todo' for the new task., Exec_Success
ACTION (android.widget.Button, org.secuso.privacyfriendlytodolist:id/bt_new_task_ok, (199, 485), click, NULL): Click on the 'Okay' button to add the new task to the To-Do list., Exec_Success

ASSERT (android.widget.TextView, org.secuso.privacyfriendlytodolist:id/tv_exlv_task_name, (55, 90), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the task with the name 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

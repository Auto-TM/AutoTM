## a22's b21 to a21

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
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to open more options. The page after clicking this control is the options page, which has a settings and about option.
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/addToDoItemFAB, (248, 568), click, NULL): Click to add new todo item. The page after clicking this control is the ToDo details page, which allows the user to set the title, reminder, date and other information of the ToDo.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/addToDoItemFAB, (248, 568), click, NULL): Click on the add button to create a new todo item.
~~~
Based on the information given, the test case can be converted into the following UIAutomator2 code:

···
d(resourceId="com.rubenroy.minimaltodo:id/addToDoItemFAB").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, Navigate up, (0, 24), click, NULL): The click action on the 'Navigate up' button returns the user to the previous page, with elements such as add todo button and more options.
ACTION (bq, com.rubenroy.minimaltodo:id/toDoCustomTextInput, (0, 121), click, NULL): Click to input the title for the new to-do item. The next page remains the task creation page where you can set a reminder option, and save the task.
ACTION (android.widget.EditText, com.rubenroy.minimaltodo:id/userToDoEditText, (32, 133), click, NULL): Click to enter or edit the task title. The next page after clicking this control is the same page with editable title input and additional controls like reminder settings and save button.
ACTION (android.widget.EditText, com.rubenroy.minimaltodo:id/userToDoEditText, (32, 133), longClick, NULL): Long clicking this element may allow you to paste copied text into this field. The subsequent page shows an enabled "Paste" button function, indicating the text can be pasted here.
ACTION (android.widget.LinearLayout, com.rubenroy.minimaltodo:id/todoReminderAndDateContainerLayout, (0, 220), click, NULL): Click to set reminder for the task. The next page remains on the task editing page, where reminders can be adjusted and toggled on/off.
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/userToDoReminderIconImageButton, (36, 296), click, NULL): Clicking on this control allows the user to set a reminder for the task. After the interaction, the page stays the same, but with the reminder set, the reminder status shows 'ON' in the subsequent page.
ACTION (android.widget.TextView, com.rubenroy.minimaltodo:id/userToDoRemindMeTextView, (65, 297), click, NULL): The 'Remind Me' text element is clicked to set a reminder for the task. The subsequent page after clicking 'Remind Me' displays a 'Switch' control that can toggle the reminder 'ON' or 'OFF'.
ACTION (android.widget.Switch, com.rubenroy.minimaltodo:id/toDoHasDateSwitchCompat, (211, 299), click, NULL): Clicking this switch enables the reminder for the to-do item. After the action, an additional widget for setting the date and time of the reminder becomes available on the current page.
ACTION (android.widget.Switch, com.rubenroy.minimaltodo:id/toDoHasDateSwitchCompat, (211, 299), click, NULL): Toggling this switch REMIND ME on the current UI, sets a date reminder. The next UI confirms that the reminder is set and provides options to input date and time of the reminder.
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton, (248, 192), click, NULL): Click to add a new todo item. The following page is the main page, where the todo will be displayed after being added.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.rubenroy.minimaltodo:id/userToDoEditText, (32, 133), input, "Sample Todo"): Input the text 'Sample Todo' into the title field and hide the keyboard.
~~~
Based on the provided information, the following is the UIAutomator2 code in Python:

···
d(resourceId="com.rubenroy.minimaltodo:id/userToDoEditText").set_text("Sample Todo")
d.press("enter")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, Navigate up, (0, 24), click, NULL): Click to navigate back. The page after clicking this control is the home page, which states "You don't have any todos" and contains options for adding todos.
ACTION (bq, com.rubenroy.minimaltodo:id/toDoCustomTextInput, (0, 121), click, NULL): Click to edit the title of the Todo. The page after clicking this control remains the same, retaining all the options for editing the title and reminder details.
ACTION (android.widget.EditText, com.rubenroy.minimaltodo:id/userToDoEditText, (32, 133), click, NULL): Click to edit the task title. The page after clicking remains the same, except the task title is now editable.
ACTION (android.widget.EditText, com.rubenroy.minimaltodo:id/userToDoEditText, (32, 133), long_click, NULL): Long clicking this widget leads to a context menu where options like 'Paste' and 'Select all' are available.
ACTION (android.widget.LinearLayout, com.rubenroy.minimaltodo:id/todoReminderAndDateContainerLayout, (0, 220), click, NULL): Clicking on this control opens reminder settings for the todo item. The next page has the same todo item components along with the reminder dialog box.
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/userToDoReminderIconImageButton, (36, 296), click, NULL): Click to set a reminder for the task. After the click, user stays on the same page with option to set reminder for the task.
ACTION (android.widget.TextView, com.rubenroy.minimaltodo:id/userToDoRemindMeTextView, (65, 297), click, NULL): Click to set a reminder for the todo item. After clicking, the status of the reminder changes to "ON" and can be configured with a specific reminder time.
ACTION (android.widget.Switch, com.rubenroy.minimaltodo:id/toDoHasDateSwitchCompat, (211, 299), click, NULL): Clicking this switch sets a reminder for the task in the 'Minimal ToDo' app. After setting, reminder date and time fields appear allowing the user to set specific date and time.
ACTION (android.widget.Switch, com.rubenroy.minimaltodo:id/toDoHasDateSwitchCompat, (211, 299), click, NULL): Click to set a reminder for the todo item. The page after clicking this control shows the reminder has been set for "Today at 12:00 AM".
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton, (248, 192), click, NULL): Clicking this button expedites the process of creating to-do items. After clicking, it will navigate to a new page where the created to-do item is visible and can be further interacted with.

````

#### Selected Event(s) and Script
````
Based on the provided information, the next step should be to save the new todo item. This can be achieved by clicking on the 'makeToDoFloatingActionButton' button. Here is the action:

~~~
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton, (248, 192), click, NULL): Click on the add button to save the new todo item.
~~~
Based on the provided information, the corresponding UIAutomator2 code in Python would be:

···
d(resourceId="com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageView, NULL, (280, 28), click, NULL): Click to access more options. The subsequent page contains options for "Settings" and "About".
ACTION (android.widget.LinearLayout, com.rubenroy.minimaltodo:id/listItemLinearLayout, (0, 80), click, NULL): Click to open the details of 'Sample Todo'. The next page has an editable text box for modifying the 'Sample Todo' and a button for setting reminders.
ACTION (android.widget.TextView, com.rubenroy.minimaltodo:id/toDoListItemTextview, (77, 101), click, NULL): Click to open the 'Sample Todo' details page. This page contains options to edit the title, set reminders, and toggle whether the to-do item has a date.
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/addToDoItemFAB, (248, 568), click, NULL): Click to add a new todo item. The next page is the add todo item page, where you can input the title and set a reminder for the to-do item.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, com.rubenroy.minimaltodo:id/toDoListItemTextview, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds.
DONE
~~~
Based on your input, here is the Uiautomator2 code in Python:

```python
from uiautomator2.exceptions import UiObjectNotFoundError

try:
    d(text="Sample Todo", className="android.widget.TextView", resourceId="com.rubenroy.minimaltodo:id/toDoListItemTextview").wait(timeout=10)
except UiObjectNotFoundError:
    assert False, "The todo item with the text 'Sample Todo' is not present within 10 seconds."
```

This code waits for the appearance of the "Sample Todo" text in the TextView with the specified resource ID within 10 seconds. If the element does not appear within this time, an exception is thrown, and the assertion fails.
````
### Success
````
ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/addToDoItemFAB, (248, 568), click, NULL): Click on the add button to create a new todo item., Exec_Success

ACTION (android.widget.EditText, com.rubenroy.minimaltodo:id/userToDoEditText, (32, 133), input, "Sample Todo"): Input the text 'Sample Todo' into the title field and hide the keyboard., Exec_Success

ACTION (android.widget.ImageButton, com.rubenroy.minimaltodo:id/makeToDoFloatingActionButton, (248, 192), click, NULL): Click on the add button to save the new todo item., Exec_Success

ASSERT (android.widget.TextView, com.rubenroy.minimaltodo:id/toDoListItemTextview, (), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

## a24's b21 to a22

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
ACTION (android.widget.TextView, douzifly.list:id/txt_title, (10, 24), click, NULL): Click to navigate through the list, after clicking, the next page contains "Groups" and different items to view and edit.
ACTION (android.widget.TextView, douzifly.list:id/txt_count, (233, 24), click, NULL): Clicking on this element has no effect as there are no interactive controls associated with it in the current page context.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_setting, (264, 24), click, NULL): Click to open the settings page. The page after clicking this control is the settings page, which contains multiple options such as 'Edit Group', 'Theme', 'Sounds', 'Backup & Restore', and 'Font size'.
ACTION (android.widget.RelativeLayout, douzifly.list:id/content, (13, 84), click, NULL): User clicking this widget accesses a Sample Todo Item. The subsequent screen allows user to view, edit and delete the selected todo item.
ACTION (android.widget.TextView, douzifly.list:id/txt_thing, (35, 99), click, NULL): Clicking the TextView elements switches to the detail view of the selected todo item. The next page allows for modifying the todo item's text content, choosing a group for it, and setting a reminder. Additional controls are available for saving changes, deleting the item, and marking it as completed.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 554), click, NULL): Click to add a new todo item. The next page after clicking this control is the create todo page, which has a variety of text input and dropdown options for creating a new todo item.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 554), click, NULL): Click to add a new todo item. The next page after clicking this control is the create todo page, which has a variety of text input and dropdown options for creating a new todo item.
~~~
Based on your given parameters, the generated UIAutomator2 code in Python is:

```python
d(resourceId="douzifly.list:id/fab_add").click()
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.FrameLayout, douzifly.list:id/input_panel, (0, 24), click, NULL): Click to prompt user input for creating a new to-do item. The next page maintains the user input panel for data entry with options for including title, content, and group category of the to-do item.
ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), click, NULL): Click to input the title for a new task. The subsequent page after the click will be the same as current page with clickable and longClickable EditText for Content.
ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), longClick, NULL): Long click to edit the todo title. After long clicking on this input field, the clipboard options such as "Paste" appear.


ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), click, NULL): Open the item editing interface. After performing this control, the user can edit the content of the event.
ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), long_click, NULL): Long click to edit content. The next page after long clicking this control is the edit content page, which allows user to paste text.

ACTION (android.widget.TextView, douzifly.list:id/txt_group, (20, 248), click, NULL): Click to switch to the Group view. The page after clicking this control is the group list page, which displays a list of groups.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add_reminder, (10, 320), click, NULL): Click to add reminder. The next page is a date picker for setting reminders.
ACTION (android.widget.TextView, douzifly.list:id/txt_title, (10, 24), click, NULL): Click to navigate to the detail page. The page loaded by clicking this control includes an edit text box for creating or editing a task.
ACTION (android.widget.TextView, douzifly.list:id/txt_count, (233, 24), click, NULL): Click to open the detailed list view of all items. The next page includes the corresponding details and options for each item in the list.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_setting, (264, 24), click, NULL): Click to go to the settings. The subsequent page is the settings page with editable fields for title, content, and group, as well as options to add a reminder.
ACTION (android.widget.RelativeLayout, douzifly.list:id/content, (13, 84), click, NULL): Click to edit a Todo element. The page following this action is the Todo editing page with various controls and fields to modify Todo details.
ACTION (android.widget.TextView, douzifly.list:id/txt_thing, (35, 99), click, NULL): Click to edit the selected task. The page after clicking this control will direct to task detail page, which has a task title text field and a task content text field to edit the specifics of the task.
ACTION (android.widget.RelativeLayout, douzifly.list:id/content, (13, 84), click, NULL): The click event on this control leads to an input panel where the user can interact with fields like 'Title', 'Content', and a variety of other elements. The user can also add a reminder using an ImageButton.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 308), click, NULL): Click to add a new item. The page after clicking this control is the add new item page, which contains title, content, group, and color picker components.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), input, "Sample Todo"): Input the text 'Sample Todo' into the 'New List Name' field and hide the keyboard.
~~~
Based on the given parameters and instructions, the corresponding UIAutomator2 code in Python for the action would be:

```python
d(resourceId="douzifly.list:id/edit_text").set_text("Sample Todo")
d.press('enter')
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.FrameLayout, douzifly.list:id/input_panel, (0, 24), click, NULL): The click causes the to-do input panel to activate, allowing entry of a new to-do item. The next page after clicking includes the active input panel with text boxes to enter a title, content, and reminder.
ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), click, NULL): Clicks in the EditText field to allow for user input. The control of the next page focuses on displaying the entered text.

ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), long_click, NULL): Long click to edit the to-do list item. The subsequent page shows options for paste or select all indicating possible text manipulation options.
ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), click, NULL): Opens the text input field to allow the user to edit the content of the note. After editing, the content is updated as reflected in the next page JSON.
ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), long_click, NULL): Long click to edit the content. The page after long clicking this control is the content edit page, which includes options to paste text content.
ACTION (android.widget.TextView, douzifly.list:id/txt_group, (20, 288), click, NULL): Click to select the 'Default' group. The page after clicking on this control is a group selection page, which shows the selected group details including the number of tasks in that group.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add_reminder, (10, 360), click, NULL): Click to add a reminder. The page after clicking this control is the date selection page, which has a date picker and OK/Cancel buttons.
ACTION (android.widget.TextView, douzifly.list:id/txt_title, (10, 24), click, NULL): Click to open the task list. The page after clicking this control is the list page with the content of the 'To-Do' list and associated options like add task or add reminder.

ACTION (android.widget.TextView, douzifly.list:id/txt_count, (233, 24), click, NULL): The count view is click to display the number of todos in a list. After clicking this control, the view remains same, showing no interactive change.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_setting, (264, 24), click, NULL): Click to proceed to the settings page. The next page contains elements to adjust application settings.
ACTION (android.widget.RelativeLayout, douzifly.list:id/content, (13, 84), click, NULL): Click to edit "Sample Todo" item. The following page allows modification of the text and the content of the Todo item.
ACTION (android.widget.TextView, douzifly.list:id/txt_thing, (35, 99), click, NULL): Click to view the detailed content of the todo item. The page after clicking this control contains the content details and editing options for the todo item.
ACTION (android.widget.TextView, douzifly.list:id/txt_thing, (35, 99), click, NULL): Click to view the details of the 'Sample Todo'. After clicking, it will remain on the same page, but the content of the 'Sample Todo' will change based on the selected todo.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 348), click, NULL): Click to add a new todo. The next page after clicking this control shows an additional todo item added to the list.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), input, NULL):purpose1
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (10, 360), click, NULL):purpose2
ASSERT (android.widget.TextView, douzifly.list:id/txt_thing, (35, 99), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"):purpose3
DONE
~~~
Based on the provided information, here is the UIAutomator2 code in Python:

```python
# Action 1: Clear the input in the EditText field
d(resourceId="douzifly.list:id/edit_text_content").clear_text()

# Action 2: Click on the ImageButton
d(resourceId="douzifly.list:id/fab_add").click()

# Assertion: Check if the TextView element with the text "Sample Todo" is present
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').exists
```

````
### Success
````
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 554), click, NULL): Click to add a new todo item. The next page after clicking this control is the create todo page, which has a variety of text input and dropdown options for creating a new todo item., Exec_Success

ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), input, "Sample Todo"): Input the text 'Sample Todo' into the 'New List Name' field and hide the keyboard., Exec_Success

ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), input, NULL):purpose1, Exec_Success
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (10, 360), click, NULL):purpose2, Exec_Success
ASSERT (android.widget.TextView, douzifly.list:id/txt_thing, (35, 99), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"):purpose3, Exec_Success
DONE
````

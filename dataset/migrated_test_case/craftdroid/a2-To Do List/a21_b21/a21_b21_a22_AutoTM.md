## a21's b21 to a22

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
ACTION (android.widget.TextView, douzifly.list:id/txt_title, (10, 24), click, NULL): Click to navigate from the default page to the page which lists all groups.
ACTION (android.widget.TextView, douzifly.list:id/txt_count, (233, 24), click, NULL): Click to view the count of items in the list. However, in the next page, the layout remains the same as the current page with no changes in count or other settings.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_setting, (264, 24), click, NULL): Click to navigate to the settings page. The subsequent page includes options for group editing, theme selection, sound options, backup & restore, and other settings.
```
ACTION (android.widget.TextView, douzifly.list:id/txt_empty, (0, 290), click, NULL): Click to add new item or list. The page after clicking this control displays the same content, potentially suggesting no action is tied to this control or the display is static.
```
```
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 554), click, NULL): Click to add a new item. The next page allows entry of title and content for the new item.
```

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 554), click, NULL): Click on the 'Add' button to initiate the process of adding a new item.
~~~
···
d(resourceId="douzifly.list:id/fab_add").click()
···
````
#### Contextual Semantics of Widgets
````
```
ACTION (android.widget.FrameLayout, douzifly.list:id/input_panel, (0, 24), click, NULL): Click to enter edit mode. The page after clicking this control is the edit item page, which has input fields for title and content.
```
```
ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), click, NULL): Click to enter/edit the title of a list item. The page after clicking shows input options for title and content, along with an add reminder button.
```
```
ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), long click, NULL): Long click to edit the list title. This action opens an options menu to paste text into the title field.
```
```
ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), click, NULL): Click to edit content. The page after clicking this control remains the same, allowing for text input in the content field.
```
```
ACTION (android.widget.EditText, douzifly.list:id/edit_text_content, (10, 68), longClick, NULL): Long click to edit content. The page after long clicking shows options for editing, including a paste button.
```
```
ACTION (android.widget.TextView, douzifly.list:id/txt_group, (20, 248), click, NULL): Click to navigate to the groups page. The page after clicking this control has a groups title and an add button for adding new group entries.
```
```
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add_reminder, (10, 320), click, NULL): Click to add a new reminder. The next page contains a date picker to set the reminder's date.
```
```
ACTION (android.widget.TextView, douzifly.list:id/txt_title, (10, 24), click, NULL): Clicking to navigate or filter items within the app. The page after clicking shows options or categories relevant to the selected title.
```
```
ACTION (android.widget.TextView, douzifly.list:id/txt_count, (233, 24), click, NULL): Click to view or edit the count of items. The next page allows editing the title and content for the list item.
```
ACTION (android.widget.ImageButton, douzifly.list:id/fab_setting, (264, 24), click, NULL): Click to access settings or preferences related to the list based on the provided current and next page JSON data.
```
ACTION (android.widget.TextView, douzifly.list:id/txt_empty, (0, 290), click, NULL): Click to prompt empty list message indicating no current list items.
```
```
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 554), click, NULL): Click to add a new item. The page after clicking this control shows an input panel for title and content, indicating entry into an item creation mode.
```

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), input, "Sample Todo"): Input the text 'Sample Todo' into the title field for the new to-do item.
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (10, 320), click, NULL): Click on the 'save' button to add a new item.
ASSERT (android.widget.TextView, douzifly.list:id/txt_title, (10, 24), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the new to-do item with the text 'Sample Todo' is present within 10 seconds.
DONE
~~~
Certainly, based on the actions and assertions provided, here's the corresponding UIAutomator2 code in Python:

···
d(resourceId="douzifly.list:id/edit_text").send_keys("Sample Todo")
d(resourceId="douzifly.list:id/fab_add").click()
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').wait(10)
···
````
### Success
````
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (238, 554), click, NULL): Click on the 'Add' button to initiate the process of adding a new item., Exec_Success

ACTION (android.widget.EditText, douzifly.list:id/edit_text, (10, 24), input, "Sample Todo"): Input the text 'Sample Todo' into the title field for the new to-do item., Exec_Success
ACTION (android.widget.ImageButton, douzifly.list:id/fab_add, (10, 320), click, NULL): Click on the 'save' button to add a new item., Exec_Success
ASSERT (android.widget.TextView, douzifly.list:id/txt_title, (10, 24), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the new to-do item with the text 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

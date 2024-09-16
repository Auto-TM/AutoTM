## a23's b21 to a25

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
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate up. The page after clicking this control is the navigation drawer page, which allows users to navigate between different sections of the application.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete all selected or checked shopping list items. The page after clicking will present a confirmation dialog asking "Remove all checked items?" with "OK" and "Cancel" options.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), longClick, NULL): Long click to delete the checked items. The page after long clicking this control is the confirmation dialog, having an 'OK' button to confirm deletion and a 'Cancel' button to cancel the action.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to navigate to more options. The next page includes various options such as sort, create a new list, share, delete list, about, and settings.
ACTION (android.widget.ImageView, NULL, (280, 28), longClick, NULL): Long click to show more options. The page after long clicking this control is the Options page, which has multiple options such as "Sort", "Create new list", "Share", "Delete list", "About", and "Settings".
ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), long_click, NULL): Long click to interact with the shopping list view. The next page remains unchanged, indicating no changes or updates to the shopping list are made with this interaction.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. The next page is the new item page where you can type in the item description, quantity, and add the item to the list.

````

#### Selected Event(s) and Script
````
Based on the provided information, the first step is to skip the tutorial. However, the current page does not have a 'Skip' button. The closest match is the 'Navigate up' button, but it leads to the navigation drawer page, not the main page of the app. Therefore, the 'Skip' action cannot be performed on this page. 

Let's try to find a matching path for the 'New Task' action. The current page has a 'Add a new item to the shopping list' button, which is similar to the 'New Task' button in the source app. Let's try this action:

~~~
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. The next page is the new item page where you can type in the item description, quantity, and add the item to the list.
~~~
Based on the information provided, the UIAutomator2 code in Python would be:

```python
d(resourceId="com.woefe.shoppinglist:id/fab_add").click()
```

This code is clicking on the ImageButton with the given id which is used to add a new item to the shopping list.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, Navigate up, (0, 24), click, NULL): Click to navigate back to the previous page. The page after clicking this control is the parent page, which shows all shopping lists.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete checked items from the shopping list. The page, that appears after clicking this control, contains a confirmation dialog with 'OK' and 'Cancel' buttons.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), longClick, NULL): Long click to delete checked items in the list. The next page after the long click is a dialog confirmation of deletion with options - OK and Cancel.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to display additional actions. The next page includes options such as Sort, Create new list, Share, Delete list, About, and Settings.
ACTION (android.widget.ImageView, More options, (280, 28), long click, NULL): Long click to open more options. The page after long clicking this control shows a list of options which include 'Sort', 'Create new list', 'Share', 'Delete list', 'About', 'Settings'.
ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), longClick, NULL): Long click to open item details. The next page after long clicking this control contains the item details with an input for item description, quantity, and a button for completing the item addition.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), click, NULL): Click to input a new item into the shopping list. After the click, the same page stays open for further inputs.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), longClick, NULL): Long click to perform additional input options for the item such as paste. The page after long clicking this control shows a paste button to paste the copied text.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), click, NULL): Click to input quantity for the new item. The page after clicking this control is the new item creation page, where you can complete the item's information before adding it to the list.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), longClick, NULL): Long click to input the quantity for the new item in the shopping list. After performing the long click, the user can input the quantity for the new item.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click to add a new item to shopping list. The page after clicking this control is the main shopping list page with the added item.

````

#### Selected Event(s) and Script
````
Based on the executed action sequence, the current step is to input the task name 'Sample Todo' into the task name field. However, the current page's intent description does not provide an exact match for this action. The closest match is the EditText element with id 'com.woefe.shoppinglist:id/new_item_description', which can be used to input a new item into the shopping list. 

Therefore, the next step would be to input 'Sample Todo' into this EditText field. 

~~~
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), input, "Sample Todo"): Input the task name 'Sample Todo' into the task name field.
~~~
Based on the input, here is the UIAutomator2 code in Python:

···
d(resourceId="com.woefe.shoppinglist:id/new_item_description").set_text("Sample Todo")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate back to the previous page.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete the checked items. After clicking this button, a dialog pops up asking for confirmation of removal of all checked items.

ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), longClick, NULL): Long click to delete the checked items. Upon interacting, a confirmation dialog appears asking to "Remove all checked items?". Options for "Cancel" and "OK" are provided.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL) : Click to view more options. The page after clicking this control displays a list of various options such as 'Sort', 'Create new list', 'Share', 'Delete list', 'About', and 'Settings'.
Action (android.widget.ImageView, More options, (280, 28), longClick, NULL): The More options control can be long clicked to bring up further options in the app. This seems to produce no changes in terms of the widgets on the next page.

ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), long click, NULL): Long click to interact with the shopping list. The page after long clicking this control is the shopping list page again, where items can be checked or cleared.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), click, NULL): Click to add a new item to the shopping list. The page after clicking this control is a suggestion list, which contains suggestions for the item name.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), long_click, NULL): Long click to edit the item description. After long-clicking this control, options to paste text or select all text in the field appear.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), click, NULL): Click to enter the quantity for the new to-do item. After clicking, the same page persists where you can input the quantity of the new item.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), long_click, NULL): Long click to edit the quantity of the new item. The page after long clicking this control displays a paste option, which might facilitate data input.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click to add the item to the shopping list. The next page shows the updated shopping list including the newly added item.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), input, "1"): Input the quantity '1' for the task 'Sample Todo'.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click to add the task 'Sample Todo' to the list.
ASSERT (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the task with the name 'Sample Todo' is present within 10 seconds.
DONE
~~~
### Device Variable Name: d
Actions:

Here is the UIAutomator2 code for the given actions:

···
d(resourceId="com.woefe.shoppinglist:id/new_item_quantity").send_keys("1")
d(resourceId="com.woefe.shoppinglist:id/button_add_new_item").click()
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').wait(timeout=10)
···
````
### Success
````
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. The next page is the new item page where you can type in the item description, quantity, and add the item to the list., Exec_Success

ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), input, "Sample Todo"): Input the task name 'Sample Todo' into the task name field., Exec_Success

ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), input, "1"): Input the quantity '1' for the task 'Sample Todo'., Exec_Success
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click to add the task 'Sample Todo' to the list., Exec_Success
ASSERT (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the task with the name 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

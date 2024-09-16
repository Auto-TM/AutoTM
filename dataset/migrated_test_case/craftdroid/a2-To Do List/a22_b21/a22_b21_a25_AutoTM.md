## a22's b21 to a25

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
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate up. The page after clicking this control is the navigation drawer page, which allows users to navigate between different sections of the application.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete all selected or checked shopping list items. The page after clicking will present a confirmation dialog asking "Remove all checked items?" with "OK" and "Cancel" options.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), longClick, NULL): Long Click to delete checked items from the shopping list. The subsequent page after the long click action is the same shopping list page, with the checked items deleted.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to navigate to more options. The next page includes various options such as sort, create a new list, share, delete list, about, and settings.
ACTION (android.widget.ImageView, More options, (280, 28), longClick, NULL): Long click to open more options. The page after long clicking this control remains more or less the same, containing options for shopping list view, and add item button.
ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), long_click, NULL): Long click to interact with the shopping list view. The next page remains unchanged, indicating no changes or updates to the shopping list are made with this interaction.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. The next page is the new item page where you can type in the item description, quantity, and add the item to the list.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click on the add button to create a new todo item.
~~~
Based on the provided information, the following UIAutomator2 code in Python can be generated:

···
d(resourceId="com.woefe.shoppinglist:id/fab_add").click()
···
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
~~~
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), input, "Sample Todo"): Input the text 'Sample Todo' into the title field and hide the keyboard.
~~~
Based on your instructions, the following UIAutomator2 code in Python should be generated:

```python
d(resourceId="com.woefe.shoppinglist:id/new_item_description").set_text("Sample Todo")
d.press("enter")
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate back to the previous page.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete the checked items. After clicking this button, a dialog pops up asking for confirmation of removal of all checked items.

ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), long click, NULL): Long click to delete checked items. This action remains the page the same but is expected to delete the checked items from the 'Shopping List'.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL) : Click to view more options. The page after clicking this control displays a list of various options such as 'Sort', 'Create new list', 'Share', 'Delete list', 'About', and 'Settings'.
Action (android.widget.ImageView, More options, (280, 28), longClick, NULL): The More options control can be long clicked to bring up further options in the app. This seems to produce no changes in terms of the widgets on the next page.

ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), long click, NULL): Long click to interact with the shopping list. The page after long clicking this control is the shopping list page again, where items can be checked or cleared.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), click, NULL): Click to add a new item to the shopping list. The page after clicking this control is a suggestion list, which contains suggestions for the item name.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), longClick, NULL): Long click to edit the new item description. The page after long clicking this control shows options to paste text or select all text.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), click, NULL): Click to enter the quantity for the new to-do item. After clicking, the same page persists where you can input the quantity of the new item.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), long_click, NULL): Long click to edit the quantity of the new item. The page after long clicking this control displays a paste option, which might facilitate data input.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click to add the item to the shopping list. The next page shows the updated shopping list including the newly added item.

````

#### Selected Event(s) and Script
````
Based on the executed action sequence, the next step should be to save the new todo item. This can be achieved by clicking the add button again. 

~~~
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click on the add button to save the new todo item.
~~~
Based on your description, the corresponding UIAutomator2 code in Python would be:

···
d(resourceId="com.woefe.shoppinglist:id/button_add_new_item").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate up. The page after clicking this control is the main page, which displays items in the shopping list and the "Add New Item" interface.

ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete all checked items in the list. After this action, a confirmation popup appears, with options to either cancel or confirm the deletion.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), longClick, NULL): Long click to delete checked items from the shopping list. Once clicked, the checked items are removed from the list displayed on the same page.
ACTION (android.widget.ImageView, "", (280, 28), click, NULL): Click to open more options. The next page after this interaction contains the options such as Sort, Create new list, Share, Delete list, etc.

ACTION (android.widget.ImageView, More options, (280, 28), longClick, NULL): Long click to display more options. The page after long clicking this control is the application options page, which has options for sorting, creating a new list, sharing, deleting a list, about, and settings.
ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), longClick, NULL): Long click to enter selection mode for items in the list. The next page displays the selected items in a detailed view for editing or deletion.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/text_description, (12, 92), click, NULL): Click to view/edit the details of the selected item "Sample Todo". The next page remains the same as the current one since the action might lead to a pop-up dialogue box for modification which is not captured in the Next Page JSON.
ACTION (android.widget.ImageView, com.woefe.shoppinglist:id/drag_n_drop_handler, (276, 95), click, NULL): The click action is used to change the order of items in the shopping list. It interacts with the RecyclerView on the current page, enabling users to rearrange items in the list for better organization.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), click, NULL): This action represents a click event on the "New Item" EditText field. After this click, the user is able to enter the description for the new item to be added to the shopping list.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), long click, NULL): Long click to paste text for a new item. The page after interaction contains a Paste button to paste the copied text into the New Item field.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), click, NULL): Click to input the quantity of the new item. The page that follows this interaction is the same shopping list page, used for adding new items with their specified quantities.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), longClick, NULL): The long click interaction on the quantity field allows the modification of the quantity for a new shopping item. The page after long clicking this control is the same shopping list page which allows the input of the item description and item quantity.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click to add a new item to the shopping list. After clicking this widget, the same shopping list page will show up but with the new item added to the list.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, com.woefe.shoppinglist:id/text_description, (12, 92), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds.
DONE
~~~
Based on the provided parameters, the corresponding UIAutomator2 code in Python would be:

```python
assert d.xpath('//android.widget.TextView[@resource-id="com.woefe.shoppinglist:id/text_description" and @text="Sample Todo"]').wait(timeout=10)
```

This code asserts that the todo item with the text 'Sample Todo' is present within 10 seconds. It uses the XPath to locate the TextView element with the specific resource-id and text. The 'wait' method is used to wait for the element to appear within the specified timeout.
````
### Success
````
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click on the add button to create a new todo item., Exec_Success

ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), input, "Sample Todo"): Input the text 'Sample Todo' into the title field and hide the keyboard., Exec_Success

ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click on the add button to save the new todo item., Exec_Success

ASSERT (android.widget.TextView, com.woefe.shoppinglist:id/text_description, (12, 92), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the todo item with the text 'Sample Todo' is present within 10 seconds., Exec_Success
DONE
````

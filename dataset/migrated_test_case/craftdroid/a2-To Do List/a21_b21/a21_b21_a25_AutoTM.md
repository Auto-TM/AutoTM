## a21's b21 to a25

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
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate up. The page after clicking this control is the navigation drawer page, which allows users to navigate between different sections of the application.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete all selected or checked shopping list items. The page after clicking will present a confirmation dialog asking "Remove all checked items?" with "OK" and "Cancel" options.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to navigate to more options. The next page includes various options such as sort, create a new list, share, delete list, about, and settings.
ACTION (android.widget.ImageView, NULL, (280, 28), longClick, NULL): Long click to show more options. The page after long clicking this control is the Options page, which has multiple options such as "Sort", "Create new list", "Share", "Delete list", "About", and "Settings".
ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), long_click, NULL): Long click to interact with the shopping list view. The next page remains unchanged, indicating no changes or updates to the shopping list are made with this interaction.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click to add a new item to the shopping list. The next page is the new item page where you can type in the item description, quantity, and add the item to the list.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click on the 'Add Item' button to initiate the process of adding a new item to the shopping list.
~~~
Based on the provided information, the UIAutomator2 code in Python corresponding to the given action would be:

···
d(resourceId="com.woefe.shoppinglist:id/fab_add").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, Navigate up, (0, 24), click, NULL): Click to navigate back to the previous page. The page after clicking this control is the parent page, which shows all shopping lists.
ACTION (android.widget.TextView, com.woefe.shoppinglist:id/action_delete_checked, (232, 28), click, NULL): Click to delete checked items from the shopping list. The page, that appears after clicking this control, contains a confirmation dialog with 'OK' and 'Cancel' buttons.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to display additional actions. The next page includes options such as Sort, Create new list, Share, Delete list, About, and Settings.
ACTION (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), longClick, NULL): Long click to open item details. The next page after long clicking this control contains the item details with an input for item description, quantity, and a button for completing the item addition.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), click, NULL): Click to input a new item into the shopping list. After the click, the same page stays open for further inputs.
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_quantity, (2, 344), click, NULL): Click to input quantity for the new item. The page after clicking this control is the new item creation page, where you can complete the item's information before adding it to the list.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click to add a new item to shopping list. The page after clicking this control is the main shopping list page with the added item.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), input, "Sample Todo"): Input the text 'Sample Todo' into the description field for the new item.
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click on the 'Add' button to add the new item to the shopping list.
ASSERT (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the new item with the text 'Sample Todo' is present within the shopping list.
DONE
~~~
Based on the provided information, the following UIAutomator2 code in Python is generated:

```python
d(resourceId="com.woefe.shoppinglist:id/new_item_description").set_text("Sample Todo")
d(resourceId="com.woefe.shoppinglist:id/button_add_new_item").click()
assert d.xpath('//android.widget.TextView[@text="Sample Todo"]').exists
```

This code performs the following operations:
1. It inputs the text 'Sample Todo' into the description field for the new item.
2. It clicks on the 'Add' button to add the new item to the shopping list.
3. It verifies that the new item with the text 'Sample Todo' is present within the shopping list.
````
### Success
````
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/fab_add, (248, 568), click, NULL): Click on the 'Add Item' button to initiate the process of adding a new item to the shopping list., Exec_Success

ACTION (android.widget.EditText, com.woefe.shoppinglist:id/new_item_description, (2, 298), input, "Sample Todo"): Input the text 'Sample Todo' into the description field for the new item., Exec_Success
ACTION (android.widget.ImageButton, com.woefe.shoppinglist:id/button_add_new_item, (242, 344), click, NULL): Click on the 'Add' button to add the new item to the shopping list., Exec_Success
ASSERT (android.support.v7.widget.RecyclerView, com.woefe.shoppinglist:id/shoppingListView, (0, 80), wait_until_element_presence, "xpath://android.widget.TextView[@text=\"Sample Todo\"]"): Verify that the new item with the text 'Sample Todo' is present within the shopping list., Exec_Success
DONE
````

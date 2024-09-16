## a52's b52 to a53

### Semantics of Source Test case
> ```
> This test case is testing the functionality of a tip calculator application that calculates the tip amount, total bill, and how the bill is split among a number of people. It also verifies the per-person amount calculation.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (EditText, com.appsbyvir.tipcalculator:id/billEditText, (), input, "56.6") : Clear the bill amount field and input the bill amount as '56.6'.
> 2. ACTION (EditText, com.appsbyvir.tipcalculator:id/tipEditText, (), input, "15") : Clear the tip percentage field, input the tip percentage as '15', and hide the keyboard.
> 3. ACTION (EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (), input, "4") : Clear the split bill field, input the number of ways to split the bill as '4', and hide the keyboard.
> 4. ASSERT (EditText, com.appsbyvir.tipcalculator:id/perPersonEditText, (), wait_until_text_presence, "text:16.27") : Verify that the per-person amount is correctly calculated and displayed as '16.27' within 10 seconds.
> ```

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, Simple Tip Calculator, (16, 39), click, NULL): The Simple Tip Calculator control is clicked to calculate tips. Afterwards, the GUI elements don't significantly change between the current page and the next page, indicating that the click operation doesn't introduce a new widget or navigate to a new page, but it may trigger certain background processing.
ACTION (android.view.View, Advertisement, (10, 96), click, NULL): Clicking on the Advertisement triggers the ad for user engagement. The page remains the same after the action and new widgets do not appear.
ACTION (android.widget.TextView, Test Ad, (129, 96), click, NULL): Click on the 'Test Ad' widget. After this interaction, no new page appears nor any new widget.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150, 166), click, "100.00"): User clicks on the 'Bill' field to enter the bill amount. After clicking on it, the current page remains the same allowing for user input.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150,166), click, "100.00"): Click to edit the total bill amount. After clicking this control, the same page remains open with no changes in the GUI elements. Therefore, this action potentially opens the keyboard for the user to input the new bill amount.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), click, "15"): Modify the tip percentage. Click on this control does not navigate to a new page but allows to edit the percentage of tip on the bill. The pages before and after clicking this control are identical, with the same list of components. This means that the exact result of clicking this control entirely depends on the user's input.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipMinus, (150, 216), click, "-"): Click to decrease the tip percentage. After clicking, the tip percent value in the EditText with the id "com.tleapps.simpletipcalculator:id/editTextTip" decreases by 1%.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipPlus, (190, 216), click, "+"): The '+' button is clicked to increase the tip percentage. After clicking, the tip percentage in the EditText with id "com.tleapps.simpletipcalculator:id/editTextTip" increases by 1, changing from "15" to "16".
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitMinus, (150, 266), click, "-"): A click on this control changes the 'Split' value in the current page. The change in value signifies the number of people the total bill will be divided amongst. No new pages or widgets appear after interaction.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitPlus, (190, 266), click, "+"): This action increases the split amount on 'Simple Tip Calculator'. After clicking, the split value in the input field with ID "com.tleapps.simpletipcalculator:id/editTextSplit" is incremented from '1' to '2'.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), click, "1"): The click interaction with this 'Split' element presumably triggers an on-screen keyboard for the input of a numeric/string value. After interaction, no new screen appears but the GUI remains same, suggesting that interaction might lead to user-entered changes on this screen itself, such as inputting a specific split value for bill calculation.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Click to calculate the tip. After this control is clicked, the Total Bill on the next page is updated to "$115.00", Total Tip becomes "$15.00", and per person payment also becomes "$115.00".
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonShare, (116, 317), click, "Share"): Click on this control to share the calculated tip and bill details. Clicking on this control does not navigate to a new page, but it enables the sharing functionality of the app.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCopyResult, (209, 317), click, "Copy"): Click to copy the result. No change in GUI elements of the next page was observed after the button click, indicating that the result might have copied to the clipboard.
ACTION (android.widget.TextView, Total Bill, (16, 396), click, NULL): Click on this control does not navigate to a new page, but changes are made in the current page. The text value of "Total Bill" which was "$0.00" before has now changed.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalToPay, (170, 396), click, "$0.00"): Click to view the total amount to pay. Clicking on this control does not navigate to a new page, but the amount displayed may change based on modifications made in the calculator.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalTip, (168, 428), click, "$0.00"): Click to view the total tip. Clicking does not navigate to a new page, but can update the displayed total tip amount based on the other input fields (bill amount, tip percentage, split number).
ACTION (android.widget.TextView, Per person, [16, 460], unclickable, 'Per person'): This control allows user to view the total split payment per person. No direct user interaction is possible as it is not clickable. After clicking the Calculate button, this TextView field displays updated data on split payments per person.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (178, 460), click, "$0.00"): Click to display the total per person. Clicking on this control does not navigate to a new page or display new elements.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150,166), input, "56.6"): Clear the bill amount field and input the bill amount as '56.6' in the target app.
~~~
Below is your conversion from Action description into UIAutomator2 code

···
d(resourceId="com.tleapps.simpletipcalculator:id/editTextBill").clear_text()
d(resourceId="com.tleapps.simpletipcalculator:id/editTextBill").send_keys("56.6")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, Simple Tip Calculator, (16, 39), click, NULL): Clicks on the 'Simple Tip Calculator' title does not change the page or lead to new elements, so it might only serve for page identity purposes.
ACTION (android.view.View, Advertisement, (10, 96), click, NULL): Clicking on the Advertisement loads the MAUHK MAUHK Clothing webview. There are no new components or changes on the current page when the Advertisement is clicked.
ACTION (android.view.View, NULL, (10, 96), clickable, NULL): Click on the advertisement. After clicking, perhaps redirecting to a new page or opening a new activity intended for the displayed advertisement, causing no new elements to appear on the current screen.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150, 166), click, "56.6"): Click to input the bill amount for calculation. After clicking this control, there is no new page, but the user can input their bill amount. The interaction with this control does not generate new widgets on the next page.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), click, "15"): Click to enter or change the tip percentage amount. The page after clicking this control remains the same but allows for input in the tip percentage field.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipMinus, (150, 216), click, "-"): clicking on this widget decreases the tip percentage by 1%. After clicking, the value in the tip percentage box decreases from 15% to 14%.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipPlus, (190, 216), click, "+"): Increase the tip percentage. After clicking this button, the tip percentage in the 'com.tleapps.simpletipcalculator:id/editTextTip' field increases by 1.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitMinus, (150, 266), click, "-"): This button interaction allows for decreasing the split number in the tip calculation. Upon interaction, the current page JSON has remained unchanged, indicating no new page was turned to, nor new widgets have appeared. Instead, the numerical value displayed in the ("com.tleapps.simpletipcalculator:id/editTextSplit") field, which represents the tip-split count, is expected to decrease.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitPlus, (190, 266), click, '+'): Increase the number of people to split the bill with. By clicking this control, the value in the 'Split' field (com.tleapps.simpletipcalculator:id/editTextSplit) increases by 1. This allows for more accurate split bill computations when there are multiple people involved.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), click, "1"): Click to edit and enter the number of people to split the bill. After clicking this control, no new page is present, but it allows input to divide the bill total among multiple people.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Calculate the bill total. After clicking this button, the Total Bill and Per Person amounts are updated on the current page, with the total Bill amount being "$65.09" and the Per Person amount being "$65.09". No new page appears but updated values in current page.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonShare, (116, 317), click, "Share"): 'Share' button on 'Simple Tip Calculator' is clicked to share the calculated amount. After the interaction, no new page appears or no new widgets are identified on the current page.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCopyResult, (209, 317), click, "Copy"): Click to copy the calculated tip result. No new page or widget appears after this action. The widgets remain the same as indicated by Next Page JSON.
ACTION (android.widget.TextView, Total Bill, (170, 396), click, "$0.00"): After clicking "Total Bill", user stays on the current page but is expected to update the calculation and fill the total value of the bill. As of this interaction, according to Next Page JSON data, no additions or changes in UI elements or controls have been identified.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalToPay, (170, 396), click, "$0.00"): Clicking on this control triggers the bill calculation based on the data provided in the form. After clicking, there are no changes on the screen or new widgets appear, but the calculated total bill should update in this TextView.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalTip, (168, 428), click, "$0.00"): Click on the Total Tip to check the total tip calculated. Clicking on this does not navigate to a new page, but the total tip amount displayed changes based on the inputs provided on the current page.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (178, 460), click, "$0.00"): The 'Per person' field is clicked to interact with the specified widget. However, this action does not lead to a new page or significant changes in the GUI elements.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), input, "15"): Clear the tip percentage field, input the tip percentage as '15', and hide the keyboard in the target app.
~~~
Based on the given Action information, the optimal UIAutomator2 code for the specified input will be:

···
d(resourceId="com.tleapps.simpletipcalculator:id/editTextTip").clear_text()
d(resourceId="com.tleapps.simpletipcalculator:id/editTextTip").set_text("15")
d.press('back')
···

In the code:
- The first line accesses the widget with given id and clears any existing text.
- The second line sets the text on the UI element with the designated ID. It inputs "15" into the field.
- The last line presses the 'back' button to hide the keyboard after entering the data.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, Simple Tip Calculator, (16, 39), click, NULL): Clicks on the 'Simple Tip Calculator' title does not change the page or lead to new elements, so it might only serve for page identity purposes.
ACTION (android.view.View, Advertisement, (10, 96), click, NULL): Clicking on the Advertisement loads the MAUHK MAUHK Clothing webview. There are no new components or changes on the current page when the Advertisement is clicked.
ACTION (android.view.View, NULL, (10, 96), clickable, NULL): Click on the advertisement. After clicking, perhaps redirecting to a new page or opening a new activity intended for the displayed advertisement, causing no new elements to appear on the current screen.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150, 166), click, "56.6"): Click to input the bill amount for calculation. After clicking this control, there is no new page, but the user can input their bill amount. The interaction with this control does not generate new widgets on the next page.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), click, "15"): Click to enter or change the tip percentage amount. The page after clicking this control remains the same but allows for input in the tip percentage field.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipMinus, (150, 216), click, "-"): clicking on this widget decreases the tip percentage by 1%. After clicking, the value in the tip percentage box decreases from 15% to 14%.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipPlus, (190, 216), click, "+"): Increase the tip percentage. After clicking this button, the tip percentage in the 'com.tleapps.simpletipcalculator:id/editTextTip' field increases by 1.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitMinus, (150, 266), click, "-"): This button interaction allows for decreasing the split number in the tip calculation. Upon interaction, the current page JSON has remained unchanged, indicating no new page was turned to, nor new widgets have appeared. Instead, the numerical value displayed in the ("com.tleapps.simpletipcalculator:id/editTextSplit") field, which represents the tip-split count, is expected to decrease.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitPlus, (190, 266), click, '+'): Increase the number of people to split the bill with. By clicking this control, the value in the 'Split' field (com.tleapps.simpletipcalculator:id/editTextSplit) increases by 1. This allows for more accurate split bill computations when there are multiple people involved.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), click, "1"): Click to edit and enter the number of people to split the bill. After clicking this control, no new page is present, but it allows input to divide the bill total among multiple people.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Calculate the bill total. After clicking this button, the Total Bill and Per Person amounts are updated on the current page, with the total Bill amount being "$65.09" and the Per Person amount being "$65.09". No new page appears but updated values in current page.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonShare, (116, 317), click, "Share"): 'Share' button on 'Simple Tip Calculator' is clicked to share the calculated amount. After the interaction, no new page appears or no new widgets are identified on the current page.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCopyResult, (209, 317), click, "Copy"): Click to copy the calculated tip result. No new page or widget appears after this action. The widgets remain the same as indicated by Next Page JSON.
ACTION (android.widget.TextView, Total Bill, (170, 396), click, "$0.00"): After clicking "Total Bill", user stays on the current page but is expected to update the calculation and fill the total value of the bill. As of this interaction, according to Next Page JSON data, no additions or changes in UI elements or controls have been identified.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalToPay, (170, 396), click, "$0.00"): Clicking on this control triggers the bill calculation based on the data provided in the form. After clicking, there are no changes on the screen or new widgets appear, but the calculated total bill should update in this TextView.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalTip, (168, 428), click, "$0.00"): Click on the Total Tip to check the total tip calculated. Clicking on this does not navigate to a new page, but the total tip amount displayed changes based on the inputs provided on the current page.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (178, 460), click, "$0.00"): The 'Per person' field is clicked to interact with the specified widget. However, this action does not lead to a new page or significant changes in the GUI elements.

````

#### Selected Event(s) and Script
````
Based on the provided information, the next step in the source test case is to input the number of ways to split the bill as '4'. This corresponds to the 'ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), click, "1")' in the current page's intentions. Therefore, the next action should be to input '4' in the 'com.tleapps.simpletipcalculator:id/editTextSplit' field in the target app.

~~~
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), input, "4"): Clear the split bill field, input the number of ways to split the bill as '4', and hide the keyboard in the target app.
~~~
Based on the given input, the converted test semantic description into UIAutomator2 code will be as follows:

···
d.click(225, 266)
d(resourceId="com.tleapps.simpletipcalculator:id/editTextSplit").clear_text()
d(resourceId="com.tleapps.simpletipcalculator:id/editTextSplit").set_text("4")
d.press('back') # to hide the keyboard
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, Simple Tip Calculator, (16, 39), click, NULL): Clicking on this element does not navigate to a new page, but any changes after clicking on the element do not appear in the attached JSON data. Hence, the specific purpose cannot be determined from the given information.
ACTION (android.view.View, NULL, (10, 96), click, NULL): Click to view the advertisement. After this interaction, no new page or widget appears, thus this action doesn't lead to a navigation or on-screen change.
ACTION (android.widget.TextView, Test Ad, (129, 96), click, NULL): Clicking on this ad does not navigate to a new page or create new visible elements.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150, 166), click, "56.6"): Clicking on the Bill text field to input the bill amount. No significant change in the next page, the state remains consistent. The editTextBill control was clicked but no change was observed in the GUI elements.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), click, "15"): This click action is to set tip percentage for the bill. After this action, the value might be changed on the same page in the widget com.tleapps.simpletipcalculator:id/editTextTip, but no new page or widget appears.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipMinus, (150, 216), click, "-"): Click to decrease the percentage tip by one. The percentage tip is shown in the EditText component with id "com.tleapps.simpletipcalculator:id/editTextTip" and updates from "15" to "14".
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipPlus, (190, 216), click, NULL): Increase the percentage of the tip. After the click, the value of the tip percentage in the "com.tleapps.simpletipcalculator:id/editTextTip" component increases by 1.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), click, "4"): Click to enter the number of people for split bill calculation. After this action, this does not navigate to a new page, but remains on the current page where the split number can be changed for bill calculation.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitMinus, (150, 266), click, "-"): The button is clicked to decrease the split value by 1. The split value changes from 4 to 3 as a result.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitPlus, (190, 266), click, NULL): Clicking this button increases the number of people that the bill is divided among. After the click, the 'editTextSplit' text field which represents the number of splits, increases the count from 4 to 5.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Clicking on this button calculates the total bill, tip, and split per person based on the entered values. After this action, you can see the calculated total bill amount "$65.09", total tip "$8.49", and amount per person "$16.27".
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonShare, (116, 317), click, "Share"): Tapping on the 'Share' button does not appear to navigate to a new page according to the provided Next Page JSON. Possible intention could be to trigger the sharing functionality to distribute the calculated tip information to others through various sharing options provided by the Android system.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCopyResult, (209, 317), click, "Copy"): Clicking the 'Copy' button does not result in a new page. However, the operation is intended to copy the calculated data output into the device's clipboard for further use or sharing.
ACTION (android.widget.TextView, Total Bill, (170, 396), click, "$0.00"): Clicking on the 'Total Bill' does not lead to a change in interface or initiate any events. It appears to be non-interactive.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalToPay, (170, 396), click, "$0.00"): Click to show the total amount to pay. Clicking on this control doesn't navigate to a new page. The summary of the calculation remains the same on the current page, along with the other existing widgets and their controls, displaying no changes in the page content.
ACTION (android.widget.TextView, Total Tip, (16, 428), click, "$0.00"): After clicking, the total tip value does not change as this widget is not clickable or modifiable. It maintains the output of the calculated tip.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalTip, (168, 428), click, "$0.00"): Clicking to see detailed Total Tip information. This action does not navigate to a new page or make any new widgets appear.
ACTION (android.widget.TextView, Per person, (16, 460), click, NULL): Transition to the calculation result page. The next page shows the calculated tip per person given the tip percentage and number of people splitting the bill. The calculated tip per person is displayed in the textViewTotalPerPerson component with id "com.tleapps.simpletipcalculator:id/textViewTotalPerPerson".
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (178, 460), click, "$0.00"): Clicking on this widget does not navigate to a new page or prompt any visible change.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Clicking on this button calculates the total bill, tip, and split per person based on the entered values. After this action, you can see the calculated total bill amount "$65.09", total tip "$8.49", and amount per person "$16.27".
ASSERT (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (178, 460), wait_until_text_presence, "text:16.27"): Verify that the per-person amount is correctly calculated and displayed as '16.27' within 10 seconds.
DONE
~~~
Based on your input, the UIAutomator2 code for the given sequence of actions and assertions would look something like this:

Input:
```python
d(resourceId="com.tleapps.simpletipcalculator:id/buttonCalculate").click()

import time
start_time = time.time()
while time.time() - start_time < 10:
    if d(resourceId="com.tleapps.simpletipcalculator:id/textViewTotalPerPerson").get_text() == "16.27":
        break
    else:
        time.sleep(0.5)
else:
    raise Exception("Assertion failed: text '16.27' not found within 10 seconds")
```
This sequence of commands will click the "Calculate" button and then continuously check for up to 10 seconds if the text "16.27" appears in the TextView with the id "textViewTotalPerPerson". If the text does not appear within 10 seconds, an exception is thrown, signaling that the assertion has failed.
````
### Success
````
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150,166), input, "56.6"): Clear the bill amount field and input the bill amount as '56.6' in the target app., Exec_Success

ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), input, "15"): Clear the tip percentage field, input the tip percentage as '15', and hide the keyboard in the target app., Exec_Success

ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), input, "4"): Clear the split bill field, input the number of ways to split the bill as '4', and hide the keyboard in the target app., Exec_Success

ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Clicking on this button calculates the total bill, tip, and split per person based on the entered values. After this action, you can see the calculated total bill amount "$65.09", total tip "$8.49", and amount per person "$16.27"., Exec_Success
ASSERT (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (178, 460), wait_until_text_presence, "text:16.27"): Verify that the per-person amount is correctly calculated and displayed as '16.27' within 10 seconds., Exec_Success
DONE
````

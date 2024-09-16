## a55's b51 to a53

### Semantics of Source Test case
> ```
> This test case is testing the functionality of a tip calculator application, specifically inputting a bill total and tip percentage, calculating the total with tip, and verifying the calculated total.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (EditText, com.jpstudiosonline.tipcalculator:id/etBillTotal, (), input, "56.6") : Clear the existing value and input '56.6' as the bill total.
> 2. ACTION (EditText, com.jpstudiosonline.tipcalculator:id/etTipAmount, (), input, "15") : Clear the existing tip percentage and input '15' as the new tip percentage, then hide the keyboard.
> 3. ACTION (Button, com.jpstudiosonline.tipcalculator:id/btCalculate, (), click, NULL) : Click on the 'Calculate' button to perform the calculation.
> 4. ASSERT (TextView, com.jpstudiosonline.tipcalculator:id/tvTotalWithTip, (), wait_until_text_presence, "text:65.09") : Verify that the 'Total with Tip' is correctly calculated and displayed as '$ 65.09' within 10 seconds.
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
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150, 166), input, "56.6"): Clear the existing value and input '56.6' as the bill total.
~~~
### Output:

Based on the action given, it looks like the element defined by the 'id' `com.tleapps.simpletipcalculator:id/editTextBill` needs to be interacted with. The method of interaction required is input, with a value of '56.6'.

Here is the conversion of the given action into a UIAutomator2 code:

```python
d(resourceId="com.tleapps.simpletipcalculator:id/editTextBill").set_text("56.6")
```

This code identifies the widget by its ID and sets the text of the input field to the value specified in the action.
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
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), input, "15"): Clear the existing tip percentage and input '15' as the new tip percentage, then hide the keyboard.
~~~
### Output:

Here is how you would convert the specified action into UIAutomator2 code:

```python
d(resourceId="com.tleapps.simpletipcalculator:id/editTextTip").clear_text()
d(resourceId="com.tleapps.simpletipcalculator:id/editTextTip").set_text("15")
d.press('back')
```

In this code:

- The first line clears the text in the EditText with the specific id.
- The second line enters the text '15' into the EditText designated by the specific id.
- The third line triggers the back action to hide the keyboard.
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
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Click on the 'Calculate' button to perform the calculation.
ASSERT (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalToPay, (170, 396), wait_until_text_presence, "text:$65.09"): Verify that the 'Total with Tip' is correctly calculated and displayed as '$ 65.09' within 10 seconds.
~~~
Based on your actions inputs, the corresponding uiautomator2 code in Python would be:

```
d(resourceId="com.tleapps.simpletipcalculator:id/buttonCalculate").click()
assert d(resourceId="com.tleapps.simpletipcalculator:id/textViewTotalToPay").wait(timeout=10).get_text() == "$65.09"
```

Please note that in this code example, `d.click(x=23, y=317)` has been replaced with the more reliable `d(resourceId="com.tleapps.simpletipcalculator:id/buttonCalculate").click()` as the button's ID is unique and known. Also, for the assertion, we used the `wait(timeout=10)` method to ensure that the 'Total with Tip' gets displayed within 10 seconds. This is an efficient way to handle cases where changes in the UI might take some time.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, Simple Tip Calculator, (16, 39), click, "Simple Tip Calculator"): Click to calculate the tip. This control does not navigate to a new page, but updates the current page. After clicking, the Total Bill on the current page from "$0.00" updates to "$65.09", the Total Tip from "$0.00" updates to "$8.49", and the Per person from "$0.00" updates to "$65.09". The changes indicate calculated results are now displayed.
ACTION (android.view.View, Advertisement, (10, 96), click, NULL): Click to redirect. The Widget with "Advertisement" description is clicked which leads to a new page or opens up a new in-app activity. This action doesn't result in changes on the current page with respect to the visible widgets.
ACTION (android.widget.TextView, Test Ad, (129, 96), click, NULL): Being clicked, but no changes occurred or navigated to a new page.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150, 166), click, "56.6"): 'Bill' is clicked to input bill amount for the tip calculation. Clicking this widget does not navigate to a new page.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), click, "15"): Click to update the tip percentage. After the click, the total bill with id "com.tleapps.simpletipcalculator:id/textViewTotalToPay", total tip with id "com.tleapps.simpletipcalculator:id/textViewTotalTip", and cost per person with id "com.tleapps.simpletipcalculator:id/textViewTotalPerPerson" are recalculated based on the updated tip percentage.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipMinus, (150, 216), click, "-"): Decreases the tip percentage in the calculator. After clicking the button, the tip percentage value displayed in the 'com.tleapps.simpletipcalculator:id/editTextTip' EditText decreases by 1 percent.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonTipPlus, (190, 216), click, "+"): Increment the tip percentage by 1. The action doesn't navigate to a new page, but the tip percentage displayed in the EditText with id "com.tleapps.simpletipcalculator:id/editTextTip" increases from "15" on the current page to "16" on the next page. It further affects the total bill and per person payment, as seen in the TextViews with ids "com.tleapps.simpletipcalculator:id/textViewTotalToPay" and "com.tleapps.simpletipcalculator:id/textViewTotalPerPerson".
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitPlus, (190, 266), click, "+"): The intent is to increase the split count on the 'Split' control. After clicking, there's no new page navigation but the Per Person amount and Total Bill and Tip in the current page are recalculated and updated based on the increased split number.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitMinus, (150, 266), click, "-"): Decrease the Split value by 1. When users want to split the bill less ways, they can decrease the value by clicking on this button. After clicking, the split value decreases by 1, as shown by the change in value of the editTextSplit element's text from "1" to "0" in the Next Page JSON.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonSplitPlus, (190, 266), click, NULL): Increase the number of persons splitting the bill. The split value after clicking this control has increased from '1' to '2'.
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (225, 266), click, '1'): The click on the widget does not navigate to a new page but opens an inline numerical keypad for users to change the split value for the bill calculation.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): The Calculate button has been clicked to calculate the total bill, tip, and split amount. The calculated values then appear in the respective fields on the same page; "Total Bill" now shows "$65.09", "Total Tip" shows "$8.49", and "Per person" displays "$65.09". No new page is opened.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonShare, (116, 317), click, "Share"): Click to share the calculation results. This action does not navigate to a new page or cause any changes on the current page.
ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCopyResult, (209, 317), click, "Copy"): The goal of clicking this button is to copy the calculated result for further use. After clicking this widget, the data remains the same, meaning it probably copies the result to the clipboard without altering the current user interface.
ACTION (android.widget.TextView, Total Bill, (16, 396), click, "Total Bill"): Clicking on the 'Total Bill' label does not lead to any change or navigation to another page. Its main purpose is to provide the total bill amount to the user. However, in this case, no additional widget or change in existing widget functionality was observed after the action.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalToPay, (164, 396), click, "$65.09"): After clicking this widget, there was no change. The same page with the same set of controls and widgets was maintained.
ACTION (android.widget.TextView, Total Tip, (169, 428), click, "$8.49"): Click to view the total tip details. No new page is navigated, but the displayed total tip value may change depending on the values entered in the "Bill", "Tip (%)" and "Split" fields.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalTip, (169, 428), click, "$8.49"): The user can click to view the total tip amount on the screen. In the subsequent page, no difference is perceived; thus, the same screen possibly persists where the user can view the calculated tip for the entered bill amount.
ACTION (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (172, 460), click, "$65.09"): Click to view the total amount to be paid per person. The changed element in the next page remains the same as the current page, indicating no new page is loaded or no new elements appear after clicking.

````

#### Selected Event(s) and Script
````
Based on the provided information, it seems that all the steps in the source test case have been successfully executed in the target application. The actions performed in the target application match the functional purpose of the actions in the source test case. 

The bill total and tip percentage were successfully inputted, the calculation was performed correctly, and the calculated total was verified and matched the expected result. 

As such, the test case migration process can be considered complete. 

Here is the final output:

~~~
DONE
~~~
As there are no actions to be converted into UIAutomator2 code, there's no output for this task. If tasks are given in the future, we can perform the conversion accordingly.
````
### Success
````
ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextBill, (150, 166), input, "56.6"): Clear the existing value and input '56.6' as the bill total., Exec_Success

ACTION (android.widget.EditText, com.tleapps.simpletipcalculator:id/editTextTip, (225, 216), input, "15"): Clear the existing tip percentage and input '15' as the new tip percentage, then hide the keyboard., Exec_Success

ACTION (android.widget.Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (23, 317), click, "Calculate"): Click on the 'Calculate' button to perform the calculation., Exec_Success
ASSERT (android.widget.TextView, com.tleapps.simpletipcalculator:id/textViewTotalToPay, (170, 396), wait_until_text_presence, "text:$65.09"): Verify that the 'Total with Tip' is correctly calculated and displayed as '$ 65.09' within 10 seconds., Exec_Success

DONE
````

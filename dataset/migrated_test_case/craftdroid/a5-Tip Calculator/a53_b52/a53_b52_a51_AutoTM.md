## a53's b52 to a51

### Semantics of Source Test case
> This test case is designed to validate the functionality of a simple tip calculator application by inputting bill amount, tip percentage, and split count, then verifying the calculated total per person.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (Button, android:id/button1, (), click, NULL) : Click on the 'Accept' button to proceed.
> 2. ACTION (EditText, com.tleapps.simpletipcalculator:id/editTextBill, (), input, "56.6") : Clear the bill amount field and input "56.6" as the new bill amount.
> 3. ACTION (EditText, com.tleapps.simpletipcalculator:id/editTextTip, (), input, "15") : Clear the tip percentage field and input "15" as the tip percentage.
> 4. ACTION (EditText, com.tleapps.simpletipcalculator:id/editTextSplit, (), input, "4") : Clear the split count field, input "4" as the number of splits, and hide the keyboard.
> 5. ACTION (Button, com.tleapps.simpletipcalculator:id/buttonCalculate, (), click, NULL) : Click on the 'Calculate' button to perform the calculation.
> 6. ASSERT (TextView, com.tleapps.simpletipcalculator:id/textViewTotalPerPerson, (), wait_until_text_presence, "text:16.27") : Verify that the 'Total Per Person' text view displays "$16.27" within 10 seconds, confirming the correct calculation based on the input values.

### Process
#### Contextual Semantics of Widgets
````

ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, "Bill Amount"): Clicking on this control allows the user to interact with or modify the bill amount. Swiping on this control does not navigate to a new page but maintains the current interface for editing financial details directly.
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "0.00"): Click to activate and edit the bill amount. No navigation to a new page occurs, but enables text input for updating the bill amount directly on the current page.
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, NULL): Clicking on this widget does not navigate to a new page or reveal new widgets.
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), click, "1"): Click to modify the number of people sharing the tip. Interaction does not change the page, maintaining context for input adjustment.
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "Tip Percent (%)"): Clicking on this control allows adjustment of the tip percentage. No new page appears but potentially updates related tip calculation fields on the current page.
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "15"): Clicking on this control allows for adjusting the tip percentage. However, interacting with it doesn't navigate to a new page but potentially updates calculations within the current page context, such as "Tip Per Person", "Total Tip", and "Each Person Pays" values, provided these elements dynamically change based on the tip percentage input.
ACTION (android.widget.TextView, anti.tip:id/textTipEach, (0, 190), click, NULL): Click to view details about 'Tip Per Person'. Swiping on this control does not navigate to a new page, but allows interaction with the corresponding editable field for entering individual tips. No new elements appear, indicating static interaction within the same screen context.
ACTION (android.widget.EditText, anti.tip:id/tipEach, (160, 178), click, "0.00"): Click to change the tip per person. Swiping on this control does not navigate to a new page, but the values of the editable fields are recalculated related to the bill amount, number of people, and tip percentage.
ACTION (android.widget.TextView, anti.tip:id/textTip, (0, 238), click, "0.00"): Clicking on this control does not navigate to a new page, but allows the user to input the total tip directly. No new elements or significant changes detected in the next page JSON.
ACTION (android.widget.EditText, anti.tip:id/tip, (160, 226), click, "0.00"): Click to modify or add a tip amount. No change to the navigation page, all inputs including bill amount, number of people, tip percent, and payments details remain editable post-click.
```
ACTION (android.widget.EditText, anti.tip:id/each, (160, 274), click, "0.00"): Click to edit the value for each person pays. Clicking on this control does not navigate to a new page, but allows for text entry in the field.
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, "Total Amount"): Clicking on this control does not navigate to a new page but allows updating the total amount directly on the current page.
```
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "0.00"): Clicking on this control does not navigate to a new page, but potentially allows updating the "Total Amount" value within the same page.

        
````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, NULL): Click to activate and edit the bill amount
~~~
Certainly, I will help you convert the given action into the appropriate UIAutomator2 code. Here are your transformed commands based on the input information:

### Input:
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, NULL): Click to activate and edit the bill amount

### Output Code:
···
d.click(0, 46)
···

This utilizes coordinates to perform the click on the UI element as requested.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, "Bill Amount"): Clicking on this control allows the user to interact with or modify the bill amount. Swiping on this control does not navigate to a new page but maintains the current interface for editing financial details directly.
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "0.00"): Click to activate and edit the bill amount. No navigation to a new page occurs, but enables text input for updating the bill amount directly on the current page.
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, NULL): Clicking on this widget does not navigate to a new page or reveal new widgets.
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), click, "1"): Click to modify the number of people sharing the tip. Interaction does not change the page, maintaining context for input adjustment.
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "Tip Percent (%)"): Clicking on this control allows adjustment of the tip percentage. No new page appears but potentially updates related tip calculation fields on the current page.
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "15"): Clicking on this control allows for adjusting the tip percentage. However, interacting with it doesn't navigate to a new page but potentially updates calculations within the current page context, such as "Tip Per Person", "Total Tip", and "Each Person Pays" values, provided these elements dynamically change based on the tip percentage input.
ACTION (android.widget.TextView, anti.tip:id/textTipEach, (0, 190), click, NULL): Click to view details about 'Tip Per Person'. Swiping on this control does not navigate to a new page, but allows interaction with the corresponding editable field for entering individual tips. No new elements appear, indicating static interaction within the same screen context.
ACTION (android.widget.EditText, anti.tip:id/tipEach, (160, 178), click, "0.00"): Click to change the tip per person. Swiping on this control does not navigate to a new page, but the values of the editable fields are recalculated related to the bill amount, number of people, and tip percentage.
ACTION (android.widget.TextView, anti.tip:id/textTip, (0, 238), click, "0.00"): Clicking on this control does not navigate to a new page, but allows the user to input the total tip directly. No new elements or significant changes detected in the next page JSON.
ACTION (android.widget.EditText, anti.tip:id/tip, (160, 226), click, "0.00"): Click to modify or add a tip amount. No change to the navigation page, all inputs including bill amount, number of people, tip percent, and payments details remain editable post-click.
```
ACTION (android.widget.EditText, anti.tip:id/each, (160, 274), click, "0.00"): Click to edit the value for each person pays. Clicking on this control does not navigate to a new page, but allows for text entry in the field.
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, "Total Amount"): Clicking on this control does not navigate to a new page but allows updating the total amount directly on the current page.
```
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "0.00"): Clicking on this control does not navigate to a new page, but potentially allows updating the "Total Amount" value within the same page.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), input, "56.6"): Clear the bill amount field and input "56.6" as the new bill amount.
~~~
Certainly, based on the details provided for the action to be converted into UIAutomator2 code, here is how it would look:

### Input Action Provided:
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), input, "56.6"): Clear the bill amount field and input "56.6" as the new bill amount.

### UIAutomator2 Code:
···
d(resourceId="anti.tip:id/bill").set_text("56.6")
···

This code specifies using the unique ID of the widget to set the text directly into the `EditText` field identified by `anti.tip:id/bill` with the value "56.6".
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, NULL): Clicking on the text 'Bill Amount' does not change any parameters or navigate to a new page. The next page maintains the same state with updated values on editable fields but does not introduce new elements or navigational changes.
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "56.6"): Click to edit the bill amount. Clicking on this control does not navigate to a new page, but allows for editing the bill amount directly within the current page.
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, "NULL"): Clicking does not change the page nor updates any visible elements - remains on the same input area with unchanged values.
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), click, "1"): Clicking modifies the number of people involved in the bill calculation. Swiping on this control does not navigate to a new page, but the values on the page such as 'Each Person Pays' and 'Total Amount' are recalculated based on the input number of people.
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "15"): Clicking on this widget allows the user to input or update the tip percentage. This action does not navigate to a new page but updates the values in the current page context, including updating 'Tip Per Person' to '8.49', 'Total Tip' to '8.49', and 'Each Person Pays' to '65.09'.
```
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "15"): Clicking on this control allows the user to input or modify the tip percentage. This action does not navigate to a new page but updates the calculations including "Tip Per Person" with id "anti.tip:id/tipEach" showing 8.49 and "Each Person Pays" showing 65.09 with id "anti.tip:id/each", reflecting the new total amount due by each person based on the updated tip percentage.
ACTION (android.widget.EditText, anti.tip:id/tipEach, (160, 178), click, "8.49"): Click to modify tip per person amount. Clicking on this control does not navigate to a new page, but allows editing the amount of tip each person has to pay based on the bill and tip percent. The value "8.49" can be updated.
ACTION (android.widget.TextView, anti.tip:id/textTip, (0, 238), click, "Total Tip"): Click to view detailed tip calculations. Clicking on this control does not navigate to a new page, but displays calculated tip values directly on the same screen. After interaction, displayed values "Total Tip: 8.49" and "Each Person Pays: 65.09" confirm detailed calculations based on user inputs.
ACTION (android.widget.EditText, anti.tip:id/tip, (160, 226), click, "8.49"): Click to modify the total tip. This interaction does not navigate to a new page but allows editing the total tip value directly in the input field.
ACTION (android.widget.EditText, anti.tip:id/each, (160, 274), click, "65.09"): Click to edit the amount each person pays. Clicking on this control does not navigate to a new page, but allows for direct modification of the payment value per person.
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, "65.09"): Clicking updates the total calculation reflecting bill amount, people count, tip percentage, and individual dues on the visible interface. No navigation occurs, but the summary fields like 'Each Person Pays', 'Total Tip', 'Tip Per Person' and 'Total Amount' are updated directly on the current page.
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "65.09"): Clicking on this control does not navigate to a new page, but the action is likely intended for updating or confirming the total amount after calculations. The same elements are present on the next page, indicating that the state of the application may not visibly change, but an internal update or confirmation might occur.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "15"):purpose: Click to activate and edit the tip percentage.
~~~
Certainly! Based on your input, here is the converted uiautomator2 code in Python:

```python
d.click(0, 142)
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, NULL): Clicking on the text 'Bill Amount' does not change any parameters or navigate to a new page. The next page maintains the same state with updated values on editable fields but does not introduce new elements or navigational changes.
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "56.6"): Click to edit the bill amount. Clicking on this control does not navigate to a new page, but allows for editing the bill amount directly within the current page.
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, "NULL"): Clicking does not change the page nor updates any visible elements - remains on the same input area with unchanged values.
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), click, "1"): Clicking modifies the number of people involved in the bill calculation. Swiping on this control does not navigate to a new page, but the values on the page such as 'Each Person Pays' and 'Total Amount' are recalculated based on the input number of people.
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "15"): Clicking on this widget allows the user to input or update the tip percentage. This action does not navigate to a new page but updates the values in the current page context, including updating 'Tip Per Person' to '8.49', 'Total Tip' to '8.49', and 'Each Person Pays' to '65.09'.
```
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "15"): Clicking on this control allows the user to input or modify the tip percentage. This action does not navigate to a new page but updates the calculations including "Tip Per Person" with id "anti.tip:id/tipEach" showing 8.49 and "Each Person Pays" showing 65.09 with id "anti.tip:id/each", reflecting the new total amount due by each person based on the updated tip percentage.
ACTION (android.widget.EditText, anti.tip:id/tipEach, (160, 178), click, "8.49"): Click to modify tip per person amount. Clicking on this control does not navigate to a new page, but allows editing the amount of tip each person has to pay based on the bill and tip percent. The value "8.49" can be updated.
ACTION (android.widget.TextView, anti.tip:id/textTip, (0, 238), click, "Total Tip"): Click to view detailed tip calculations. Clicking on this control does not navigate to a new page, but displays calculated tip values directly on the same screen. After interaction, displayed values "Total Tip: 8.49" and "Each Person Pays: 65.09" confirm detailed calculations based on user inputs.
ACTION (android.widget.EditText, anti.tip:id/tip, (160, 226), click, "8.49"): Click to modify the total tip. This interaction does not navigate to a new page but allows editing the total tip value directly in the input field.
ACTION (android.widget.EditText, anti.tip:id/each, (160, 274), click, "65.09"): Click to edit the amount each person pays. Clicking on this control does not navigate to a new page, but allows for direct modification of the payment value per person.
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, "65.09"): Clicking updates the total calculation reflecting bill amount, people count, tip percentage, and individual dues on the visible interface. No navigation occurs, but the summary fields like 'Each Person Pays', 'Total Tip', 'Tip Per Person' and 'Total Amount' are updated directly on the current page.
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "65.09"): Clicking on this control does not navigate to a new page, but the action is likely intended for updating or confirming the total amount after calculations. The same elements are present on the next page, indicating that the state of the application may not visibly change, but an internal update or confirmation might occur.

````

#### Selected Event(s) and Script
````
Based on the provided source test case semantics and the executed action sequence, it appears that we have successfully migrated the first three steps of the source test case to the target application. These steps involve:

1. Activating and editing the bill amount.
2. Inputting the bill amount.
3. Activating and editing the tip percentage.

The next step in the source test case involves clearing the tip percentage field and inputting "15" as the new tip percentage. The executed action sequence indicates that the activation and preparation to edit the tip percentage were successful. Now, we need to perform the actual input of the tip percentage.

Let's proceed with the next step:

~~~
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), input, "15"): Input "15" as the new tip percentage
~~~
Certainly! For the action described, you want to input the value "15" into an EditText element based on its widget id. Here's how you can do it in UIAutomator2 Python code:

```
d(resourceId="anti.tip:id/percent").set_text("15")
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, NULL): Clicking on the text 'Bill Amount' does not change any parameters or navigate to a new page. The next page maintains the same state with updated values on editable fields but does not introduce new elements or navigational changes.
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "56.6"): Click to edit the bill amount. Clicking on this control does not navigate to a new page, but allows for editing the bill amount directly within the current page.
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, "NULL"): Clicking does not change the page nor updates any visible elements - remains on the same input area with unchanged values.
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), click, "1"): Clicking modifies the number of people involved in the bill calculation. Swiping on this control does not navigate to a new page, but the values on the page such as 'Each Person Pays' and 'Total Amount' are recalculated based on the input number of people.
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "15"): Clicking on this widget allows the user to input or update the tip percentage. This action does not navigate to a new page but updates the values in the current page context, including updating 'Tip Per Person' to '8.49', 'Total Tip' to '8.49', and 'Each Person Pays' to '65.09'.
```
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "15"): Clicking on this control allows the user to input or modify the tip percentage. This action does not navigate to a new page but updates the calculations including "Tip Per Person" with id "anti.tip:id/tipEach" showing 8.49 and "Each Person Pays" showing 65.09 with id "anti.tip:id/each", reflecting the new total amount due by each person based on the updated tip percentage.
ACTION (android.widget.EditText, anti.tip:id/tipEach, (160, 178), click, "8.49"): Click to modify tip per person amount. Clicking on this control does not navigate to a new page, but allows editing the amount of tip each person has to pay based on the bill and tip percent. The value "8.49" can be updated.
ACTION (android.widget.TextView, anti.tip:id/textTip, (0, 238), click, "Total Tip"): Click to view detailed tip calculations. Clicking on this control does not navigate to a new page, but displays calculated tip values directly on the same screen. After interaction, displayed values "Total Tip: 8.49" and "Each Person Pays: 65.09" confirm detailed calculations based on user inputs.
ACTION (android.widget.EditText, anti.tip:id/tip, (160, 226), click, "8.49"): Click to modify the total tip. This interaction does not navigate to a new page but allows editing the total tip value directly in the input field.
ACTION (android.widget.EditText, anti.tip:id/each, (160, 274), click, "65.09"): Click to edit the amount each person pays. Clicking on this control does not navigate to a new page, but allows for direct modification of the payment value per person.
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, "65.09"): Clicking updates the total calculation reflecting bill amount, people count, tip percentage, and individual dues on the visible interface. No navigation occurs, but the summary fields like 'Each Person Pays', 'Total Tip', 'Tip Per Person' and 'Total Amount' are updated directly on the current page.
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "65.09"): Clicking on this control does not navigate to a new page, but the action is likely intended for updating or confirming the total amount after calculations. The same elements are present on the next page, indicating that the state of the application may not visibly change, but an internal update or confirmation might occur.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, NULL):purpose: Click to activate and edit the number of people splitting the bill.
~~~
Certainly, given your action description and the guidelines provided, here's how you can convert the given action into UIAutomator2 code in Python:

### Actions to Code:

For the given action: 

"ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, NULL):purpose: Click to activate and edit the number of people splitting the bill."

### UIAutomator2 Python Code:
```
d.click(0, 94)
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, NULL): Clicking on the text 'Bill Amount' does not change any parameters or navigate to a new page. The next page maintains the same state with updated values on editable fields but does not introduce new elements or navigational changes.
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "56.6"): Click to edit the bill amount. Clicking on this control does not navigate to a new page, but allows for editing the bill amount directly within the current page.
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, "NULL"): Clicking does not change the page nor updates any visible elements - remains on the same input area with unchanged values.
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), click, "1"): Clicking modifies the number of people involved in the bill calculation. Swiping on this control does not navigate to a new page, but the values on the page such as 'Each Person Pays' and 'Total Amount' are recalculated based on the input number of people.
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "15"): Clicking on this widget allows the user to input or update the tip percentage. This action does not navigate to a new page but updates the values in the current page context, including updating 'Tip Per Person' to '8.49', 'Total Tip' to '8.49', and 'Each Person Pays' to '65.09'.
```
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "15"): Clicking on this control allows the user to input or modify the tip percentage. This action does not navigate to a new page but updates the calculations including "Tip Per Person" with id "anti.tip:id/tipEach" showing 8.49 and "Each Person Pays" showing 65.09 with id "anti.tip:id/each", reflecting the new total amount due by each person based on the updated tip percentage.
ACTION (android.widget.EditText, anti.tip:id/tipEach, (160, 178), click, "8.49"): Click to modify tip per person amount. Clicking on this control does not navigate to a new page, but allows editing the amount of tip each person has to pay based on the bill and tip percent. The value "8.49" can be updated.
ACTION (android.widget.TextView, anti.tip:id/textTip, (0, 238), click, "Total Tip"): Click to view detailed tip calculations. Clicking on this control does not navigate to a new page, but displays calculated tip values directly on the same screen. After interaction, displayed values "Total Tip: 8.49" and "Each Person Pays: 65.09" confirm detailed calculations based on user inputs.
ACTION (android.widget.EditText, anti.tip:id/tip, (160, 226), click, "8.49"): Click to modify the total tip. This interaction does not navigate to a new page but allows editing the total tip value directly in the input field.
ACTION (android.widget.EditText, anti.tip:id/each, (160, 274), click, "65.09"): Click to edit the amount each person pays. Clicking on this control does not navigate to a new page, but allows for direct modification of the payment value per person.
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, "65.09"): Clicking updates the total calculation reflecting bill amount, people count, tip percentage, and individual dues on the visible interface. No navigation occurs, but the summary fields like 'Each Person Pays', 'Total Tip', 'Tip Per Person' and 'Total Amount' are updated directly on the current page.
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "65.09"): Clicking on this control does not navigate to a new page, but the action is likely intended for updating or confirming the total amount after calculations. The same elements are present on the next page, indicating that the state of the application may not visibly change, but an internal update or confirmation might occur.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), input, "4"): Input "4" as the new number of people splitting the bill.
~~~
···
d(resourceId="anti.tip:id/people").set_text("4")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, " Bill Amount"): Clicking on this widget does not reveal any changes or navigate to a new page, which indicates it might be a static element or part of the UI without interactive functionality.
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "56.6"): Click to edit the bill amount. Clicking on this control does not navigate to a new page, but allows for the modification of the bill amount, which is essential for recalculating the total tip and each person's share of the bill.
ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, NULL): Clicking on this control does not navigate to a new page, but updates the value of "# Of People" from 1 to 4. Swiping on this control adjusts the calculations for "Tip Per Person" from "8.49" to "2.12" and "Each Person Pays" from "65.09" to "16.27".
ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), click, "4"): Clicking on this control allows adjustment of the number of people sharing the bill. No navigation to a new page occurs, instead, updates like 'Tip Per Person' to '2.12' and 'Each Person Pays' to '16.27' happen on the same page.
ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, NULL): Click to select or edit the tip percent. Swiping on this control does not navigate to a new page, but allows adjustment of the tip percentage. The next page shows unchanged values, indicating no side effects from this action except potential modification of the 'Tip Percent (%)' field.
~~~
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "15"): Click to modify tip percentage. Swiping on this control does not navigate to a new page, but allows updating the tip percentage. The field update recalculates and displays new values for 'Tip Per Person', 'Total Tip', 'Each Person Pays', and 'Total Amount' on the same page.
~~~
ACTION (android.widget.TextView, anti.tip:id/textTipEach, (0, 190), click, "Tip Per Person"): Click to view detailed calculations. Swiping on this control does not navigate to a new page, but updates the calculation fields reflecting individual contributions. The updated elements include 'tipEach' with new text "2.12" and 'each' with new text "16.27".
ACTION (android.widget.EditText, anti.tip:id/tipEach, (160, 178), click, "2.12"): Click to edit the tip per person. Clicking on this control updates the value but stays on the same page, no new widgets or pages are displayed.
ACTION (android.widget.EditText, anti.tip:id/textTip, (0, 238), click, "8.49"): Click to update the total tip amount. Clicking on this control does not navigate to a new page, but possibly triggers calculation mechanisms to update related fields such as "Tip Per Person" and "Each Person Pays" with respective values "2.12" and "16.27".
ACTION (android.widget.EditText, anti.tip:id/tip, (160, 226), click, "8.49"): Click to edit the 'Total Tip'. Clicking on this control does not navigate to a new page, but allows editing of the tip amount within the same interface.
ACTION (android.widget.EditText, anti.tip:id/each, (160, 274), click, "16.27"): Click to edit the amount each person pays. Clicking on this control does not navigate to a new page, but allows the user to update the amount each person should pay based on changes in the number of people or tip percentage.
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, "Total Amount"): Clicking on this control does not navigate to a new page, but updates the 'Each Person Pays' and 'Total Amount' fields based on number of people and tip percentage on the same page. The new values are: 'Each Person Pays' with value 16.27 and 'Total Amount' with value 65.09.
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "65.09"): Clicking on this control does not navigate to a new page, but updates the values related to the tip calculation, showing the updated total amount each person pays based on the entered bill amount, number of people, and tip percent.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, NULL): Click to activate and view the total amount calculation.
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "65.09"): Click to edit the total amount. Input "65.09" as the new total amount.
ASSERT (android.widget.EditText, anti.tip:id/each, (160, 274), "16.27"): Verify that the 'Each Person Pays' field displays "16.27".
DONE
~~~
Certainly, here is the UIAutomator2 code for the provided actions and assertions as per your instructions:

···
d.click(0, 334)
d(resourceId="anti.tip:id/total").set_text("65.09")
assert d(resourceId="anti.tip:id/each").get_text() == "16.27"
···
````
### Success
````
ACTION (android.widget.TextView, anti.tip:id/textBill, (0, 46), click, NULL): Click to activate and edit the bill amount, Exec_Success

ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), input, "56.6"): Clear the bill amount field and input "56.6" as the new bill amount., Exec_Success

ACTION (android.widget.TextView, anti.tip:id/textPercent, (0, 142), click, "15"):purpose: Click to activate and edit the tip percentage., Exec_Success

ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), input, "15"): Input "15" as the new tip percentage, Exec_Success

ACTION (android.widget.TextView, anti.tip:id/textPeople, (0, 94), click, NULL):purpose: Click to activate and edit the number of people splitting the bill., Exec_Success

ACTION (android.widget.EditText, anti.tip:id/people, (160, 82), input, "4"): Input "4" as the new number of people splitting the bill., Exec_Success

ACTION (android.widget.TextView, anti.tip:id/textTotal, (0, 334), click, NULL): Click to activate and view the total amount calculation., Exec_Success
ACTION (android.widget.EditText, anti.tip:id/total, (160, 322), click, "65.09"): Click to edit the total amount. Input "65.09" as the new total amount., Exec_Success
ASSERT (android.widget.EditText, anti.tip:id/each, (160, 274), "16.27"): Verify that the 'Each Person Pays' field displays "16.27"., Exec_Success
DONE
````

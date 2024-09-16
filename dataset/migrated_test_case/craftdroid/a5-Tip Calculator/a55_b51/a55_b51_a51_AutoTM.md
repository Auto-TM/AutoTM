## a55's b51 to a51

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
Based on the provided information, we need to start the test case migration. The first step in the source test case is to clear the existing value and input '56.6' as the bill total. Let's find a matching operation in the current page's intentions.

The closest matching intention for updating the bill amount is:
```
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "0.00"): Click to activate and edit the bill amount.
```

Since this action allows for text input directly on the current page and matches the functionality of inputting a bill total, we'll use this to perform the first step of the source test case.

Here's the migration for the first step:

~~~
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), input, "56.6"): Clear the existing value and input '56.6' as the bill total.
~~~
···
d.click(160, 34)
d(resourceId="anti.tip:id/bill").set_text("56.6")
···
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
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "NULL"):purpose
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), input, "15"):purpose
~~~
```
d.click(160, 130)
d.send_keys("15")
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
ACTION (android.widget.Button, anti.tip:id/calculate, (), click, NULL): Click on the 'Calculate' button to perform the calculation.
~~~
···
d(resourceId="anti.tip:id/calculate").click()
···
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
ASSERT (android.widget.TextView, anti.tip:id/total, (160, 322), wait_until_text_presence, "text:65.09"): Verify that the total bill amount displayed is '65.09' within 10 seconds.
DONE
~~~
```
d.click(160, 274)
assert d(resourceId="anti.tip:id/each").get_text() == "65.09"
```
````
### Success
````
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), click, "0.00"): Click to activate and edit the bill amount., Exec_Success
ACTION (android.widget.EditText, anti.tip:id/bill, (160, 34), input, "56.6"): Clear the existing value and input '56.6' as the bill total., Exec_Success

ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), click, "NULL"):purpose, Exec_Success
ACTION (android.widget.EditText, anti.tip:id/percent, (160, 130), input, "15"):purpose, Exec_Success

ACTION (android.widget.Button, anti.tip:id/calculate, (), click, NULL): Click on the 'Calculate' button to perform the calculation., Exec_Fail

ASSERT (android.widget.TextView, anti.tip:id/total, (160, 322), wait_until_text_presence, "text:65.09"): Verify that the total bill amount displayed is '65.09' within 10 seconds., Exec_Success
DONE
````

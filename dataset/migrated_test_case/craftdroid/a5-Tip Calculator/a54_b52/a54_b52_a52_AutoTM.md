## a54's b52 to a52

### Semantics of Source Test case
> ```
> This test case is testing the functionality of a tip calculator that calculates the per person bill amount based on the total bill, tip percentage, and number of guests.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (EditText, com.zaidisoft.teninone:id/billAmountET, (), input, "56.6") : Clear the existing value and input '56.6' as the bill amount.
> 2. ACTION (EditText, com.zaidisoft.teninone:id/tipPercentET, (), input, "15") : Clear the existing value and input '15' as the tip percentage.
> 3. ACTION (EditText, com.zaidisoft.teninone:id/guestNumberET, (), input, "4") : Clear the existing value and input '4' as the number of guests.
> 4. ACTION (Button, com.zaidisoft.teninone:id/calculateBtn, (), click, NULL) : Click on the 'Calculate' button to compute the results.
> 5. ASSERT (TextView, com.zaidisoft.teninone:id/perPersonBillTV, (), wait_until_text_presence, "text:16.27") : Verify that the 'per person bill' text view displays '16.27' within 10 seconds after calculation.
> ```

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/message, (16, 276), click, "Connect to internet and enjoy more wonderful FREE games!"): Clicking on this control does not navigate to a new page, but offers options to 'Skip' or 'Connect' to internet services, each having buttons with ids "android:id/button2" and "android:id/button1" respectively.
ACTION (android.widget.Button, android:id/button2, (16, 339), click, "Skip"): Click to skip the connection step. The resulting page includes a Tip Calculator with fields for Bill amount, Tip percentage, Split information, and final calculation details.
ACTION (android.widget.Button, android:id/button1, (160, 339), click, "Connect"): Click to attempt a connection to the internet. No new page appears or no new widgets are displayed after the action.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.Button, android:id/button2, (16, 339), click, NULL): Click to skip the connection step and proceed to the Tip Calculator page.
~~~
```
d.click(16, 339)
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/action_bar_title, (49, 35), click, "Tip Calculator"): Click to navigate to the tip calculation page. No new page appears; however, the action reconfirms the user's presence on the Tip Calculator page, ready for input and interaction.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/billTextView, (17, 92), click, NULL): Clicking does not have a visible effect as no new elements appear and the scenario remains static.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), click, NULL): Click to enter or edit the bill amount. No new page appears and no new interactive elements are introduced on the current page.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/tipTextView, (17, 140), click, "Tip %"): Click on 'Tip %'. Interaction creates dynamic user input for tip percentage. Upon click, the tip percentage field allows adjustment, impacting subsequent calculations in fields such as Final Bill and Tip. This control being clicked does not navigate to a new page, but triggers potential recalculation of payment splits depending on tip percentage entered.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/tipEditText, (178, 133), click, "15.0"): Click to adjust tip percentage. No new page is navigated to, but modifying this element can dynamically update the calculated tip values reflected on the same page.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/splitBillTextView, (17, 258), click, "Split Bill"): Click to split bill options. Swiping on this control does not navigate to a new page, but allows adjustment of options related to splitting the bill within the same page.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), click, "# of ways"): Click to input the number of ways to split the bill. Swiping on this control does not navigate to a new page, but allows for adjustment of the bill splitting parameters directly on the current page.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalBillTextView, (17, 320), click, "Final Bill: Verified by Vir"): Clicking on this control does not navigate to a new page or change the layout significantly, suggesting that it might display or hide details about the final bill calculation on the same page.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTipTextView, (17, 372), click, NULL): Clicking on this control doesn't navigate to a new page or change the current page elements; it possibly triggers a calculation or displays a tip amount without altering the page structure.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalTipEditText, (178, 357), click, "0.0"): Interaction does not navigate to a new page or display new elements, but allows for entering or updating the tip amount directly within the widget.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTextView, (17, 420), click, "0.0"): Clicking on this control did not navigate to a new page or visibly alter the current page's layout or available widgets.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalBillEditText, (178, 405), click, NULL): Click to edit the final bill amount. Interaction with this control does not navigate to a new page, but allows user to update the bill calculations within the same page layout.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/perPersonTextView, (17, 468), click, "0.0"): Click to calculate the total amount per person based on the current inputs. Clicking this control updates values but does not navigate to a new page.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/perPersonEditText, (178, 453), click, "0.0"): Clicking on this control allows for inputting a share amount for the per person breakdown in the tip calculator. Interaction with this widget enables user-specific customization of tip sharing among participants. No new page is displayed, but it facilitates user engagement directly on the same interface.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/signoffTextView, (37, 517), click, NULL): Clicking on the 'Thanks for tipping your waiter/waitress!' text does not navigate to a new page nor modify any existing widget states or appearances on the current page.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), click, NULL):purpose
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), input, "56.6"): Clear the existing value and input '56.6' as the bill amount.
~~~
### Output (The code should be wrapped using '···'):

Based on the information provided, here is how to convert these actions into uiautomator2 code.

···
# Action: Click 
d.click(178, 77)

# Action: Input 
d(resourceId="com.appsbyvir.tipcalculator:id/billEditText").set_text("56.6")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/action_bar_title, (49, 35), click, "Tip Calculator"): Clicking on this control does not navigate to a new page but updates the calculation on the current page with the input values provided including Bill, Tip %, and number of ways to split the bill. The displayed final amounts on text fields 'Final Bill', 'Tip:', 'Total:', and 'Per Person:' reflect these updated calculations based on the entered values.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/billTextView, (17, 92), click, "Bill"): Click to focus on bill amount input. No page navigation occurs, but allows for bill amount editing in widget with id "com.appsbyvir.tipcalculator:id/billEditText".
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), click, "56.6"): Clicking on this control allows the user to edit the bill amount. After clicking, no new page appears but the existing page allows modification of the bill input directly.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/tipTextView, (17, 140), click, NULL): Clicking on this control does not navigate to a new page or bring up new widgets, indicating a potential functionality to display tip percentage input or adjust current tip percentage.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/tipEditText, (178, 133), click, "15"): Clicking on this control allows the user to enter a custom tip percentage. The same page elements are present before and after this interaction, indicating no navigation or new dialogues are introduced by this action.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/splitBillTextView, (17, 258), click, "Split Bill"): Clicking splits the bill. No navigation to a new page occurs; however, interaction potentially triggers calculation or update of bill split related fields on the same page.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), click, "# of ways"): Input to split the bill number of ways. Clicking on this control enables modification of the number of ways to split the bill. No new page appears but it allows real-time calculation on the existing page as reflected in the inputs and outputs of the tip calculator widgets.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalBillTextView, (17, 320), click, "Final Bill: Verified by Vir"): Clicking on this control does not navigate to a new page, but confirms the final bill calculation. There are no new widgets or changes detected in the GUI elements on the next page as per the provided JSON data.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTipTextView, (17, 372), click, "8.49"): Clicking on this control displays the final calculated tip amount based on the entered bill and tip percentage. Swiping on this control does not navigate to a new page, but retains the current display with calculated tip details.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalTipEditText, (178, 357), click, "8.49"): Click to edit the final tip amount. Swiping on this control does not navigate to a new page, but allows for the adjustment of the final tip value within the same UI context.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTextView, (17, 420), click, "Total: 65.09"): Clicking on this control does not navigate to a new page, but confirms the total amount to be paid calculated by the app, including tips, as verified by Vir. The information remains constant across the interaction indicating the final bill calculation feature.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalBillEditText, (178, 405), click, "65.09"): Clicking on this control does not navigate to a new page, but allows editing the final bill amount directly. No new widgets or significant changes on the page were detected.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/perPersonTextView, (17, 468), click, "65.09"): Clicking on Per Person value. The clickable action does not navigate to a new page but updates and verifies the final per person bill amount displayed on the same page with id "com.appsbyvir.tipcalculator:id/perPersonEditText".
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/perPersonEditText, (178, 453), click, "65.09"): Clicking on this control allows the user to edit the per person amount for the bill splitting. No new page appears, and no new widgets are introduced, indicating an in-place edit operation.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/signoffTextView, (37, 517), click, "Thanks for tipping your waiter/waitress!"): Click to acknowledge message. The click does not navigate to a new page, and no new widgets appear, but serves as a sign-off upon completing the transaction.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/tipEditText, (178, 133), input, "15"): Clear the existing value and input '15' as the tip percentage.
~~~
···
d(resourceId="com.appsbyvir.tipcalculator:id/tipEditText").set_text("15")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/action_bar_title, (49, 35), click, "Tip Calculator"): Clicking on this control does not navigate to a new page but updates the calculation on the current page with the input values provided including Bill, Tip %, and number of ways to split the bill. The displayed final amounts on text fields 'Final Bill', 'Tip:', 'Total:', and 'Per Person:' reflect these updated calculations based on the entered values.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/billTextView, (17, 92), click, "Bill"): Click to focus on bill amount input. No page navigation occurs, but allows for bill amount editing in widget with id "com.appsbyvir.tipcalculator:id/billEditText".
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), click, "56.6"): Clicking on this control allows the user to edit the bill amount. After clicking, no new page appears but the existing page allows modification of the bill input directly.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/tipTextView, (17, 140), click, NULL): Clicking on this control does not navigate to a new page or bring up new widgets, indicating a potential functionality to display tip percentage input or adjust current tip percentage.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/tipEditText, (178, 133), click, "15"): Clicking on this control allows the user to enter a custom tip percentage. The same page elements are present before and after this interaction, indicating no navigation or new dialogues are introduced by this action.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/splitBillTextView, (17, 258), click, "Split Bill"): Clicking splits the bill. No navigation to a new page occurs; however, interaction potentially triggers calculation or update of bill split related fields on the same page.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), click, "# of ways"): Input to split the bill number of ways. Clicking on this control enables modification of the number of ways to split the bill. No new page appears but it allows real-time calculation on the existing page as reflected in the inputs and outputs of the tip calculator widgets.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalBillTextView, (17, 320), click, "Final Bill: Verified by Vir"): Clicking on this control does not navigate to a new page, but confirms the final bill calculation. There are no new widgets or changes detected in the GUI elements on the next page as per the provided JSON data.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTipTextView, (17, 372), click, "8.49"): Clicking on this control displays the final calculated tip amount based on the entered bill and tip percentage. Swiping on this control does not navigate to a new page, but retains the current display with calculated tip details.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalTipEditText, (178, 357), click, "8.49"): Click to edit the final tip amount. Swiping on this control does not navigate to a new page, but allows for the adjustment of the final tip value within the same UI context.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTextView, (17, 420), click, "Total: 65.09"): Clicking on this control does not navigate to a new page, but confirms the total amount to be paid calculated by the app, including tips, as verified by Vir. The information remains constant across the interaction indicating the final bill calculation feature.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalBillEditText, (178, 405), click, "65.09"): Clicking on this control does not navigate to a new page, but allows editing the final bill amount directly. No new widgets or significant changes on the page were detected.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/perPersonTextView, (17, 468), click, "65.09"): Clicking on Per Person value. The clickable action does not navigate to a new page but updates and verifies the final per person bill amount displayed on the same page with id "com.appsbyvir.tipcalculator:id/perPersonEditText".
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/perPersonEditText, (178, 453), click, "65.09"): Clicking on this control allows the user to edit the per person amount for the bill splitting. No new page appears, and no new widgets are introduced, indicating an in-place edit operation.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/signoffTextView, (37, 517), click, "Thanks for tipping your waiter/waitress!"): Click to acknowledge message. The click does not navigate to a new page, and no new widgets appear, but serves as a sign-off upon completing the transaction.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), click, NULL):purpose
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), input, "4"): Clear the existing value and input '4' as the number of ways to split the bill.
~~~
···
d.click(178, 243)
d(resourceId="com.appsbyvir.tipcalculator:id/splitBillEditText").set_text("4")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/action_bar_title, (49, 35), click, "Tip Calculator"): Clicking on the action bar title does not navigate to a new page, but possibly refreshes the current page with no changes in the widget structure as indicated by the unchanged Next Page JSON data.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/billTextView, (17, 92), click, "Bill"): Click on 'Bill' does not navigate to a new page, but allows editing the bill amount in the EditText with id "com.appsbyvir.tipcalculator:id/billEditText".
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), click, "56.6"): Clicking on this control allows the user to edit the bill amount. Upon interaction, it does not navigate to a new page but remains on the current page allowing for immediate update of calculations based on the bill value entered.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/tipTextView, (17, 140), click, "Tip %"): Clicking on the Tip % does not navigate to a new page, but allows the user to input or edit the tip percentage directly on the current page.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/tipEditText, (178, 133), click, "15"): Clicking on the tip percentage input to adjust tip value leads to changes in update of the calculated total and per person amounts on the same page, updating the fields 'Total: 65.09' and 'Per Person: 16.27' respectively. This interaction reflects a recalculation of tip-based amounts without navigating to a new page.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/splitBillTextView, (17, 258), click, "Split Bill"): Click to adjust the number of ways the bill is split. The page after clicking this control shows the updated per person amount in the perPersonEditText field with new value "16.27".
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), click, "4"): Input in 'Split Bill' field affects recalculation of 'Per Person' cost from previous value to '16.27' in the Same Page without navigation to a new page.
~~~
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalBillTextView, (17, 320), click, "Final Bill: Verified by Vir"): Clicking on this control does not navigate to a new page or bring up a dialog. It remains on the current page where other bill and tip calculations are visible with editable fields for user inputs for bill adjustment, tipping percentage, and split bill scenarios.
~~~
~~~
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTipTextView, (17, 372), click, "8.49"): Clicking on 'Tip: 8.49' allows updating the tip amount. There is no change to the page structure; this action merely allows modifying the tip directly through the editable field linked to this TextView.
~~~
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalTipEditText, (178, 357), click, "8.49"): Click to edit the final tip amount. Clicking on this control does not navigate to a new page, but allows the user to update the tip directly on the current page.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/finalTextView, (17, 420), click, "65.09"): Click to reveal more details or finalize the bill calculation. No navigation to a new page, but potential update or calculation within the current page context as indicated by the unchanged JSON structure.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/finalBillEditText, (178, 405), click, "65.09"): Click to edit the final bill amount. Clicking on this control does not navigate to a new page, but updates data in the same screen including updated 'Per Person' calculated amount. The new 'Per Person' amount is "16.27", updated in an edit text box with id "com.appsbyvir.tipcalculator:id/perPersonEditText".
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/perPersonTextView, (17, 468), click, "16.27"): Click to display calculated per person amount. Interaction does not navigate to a new page or modify existing content significantly.
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/perPersonEditText, (178, 453), click, "16.27"): Click to edit the per person split of the bill. Swiping on this control does not navigate to a new page, but allows editing the value directly within the same layout view.
ACTION (android.widget.TextView, com.appsbyvir.tipcalculator:id/signoffTextView, (37, 517), click, NULL): Clicking on the 'signoffTextView' does not navigate to a new page or modify existing widgets; it remains a static text element.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, com.appsbyvir.tipcalculator:id/perPersonEditText, (178, 453), wait_until_text_presence, "text:16.27"): Verify that the 'per person bill' text view displays '16.27' within 10 seconds after calculation.
DONE
~~~
···
assert d(resourceId="com.appsbyvir.tipcalculator:id/perPersonEditText").wait_until(lambda d: d.get_text() == "16.27", timeout=10)
···
````
### Success
````
ACTION (android.widget.Button, android:id/button2, (16, 339), click, NULL): Click to skip the connection step and proceed to the Tip Calculator page., Exec_Success

ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), click, NULL):purpose, Exec_Success
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/billEditText, (178, 77), input, "56.6"): Clear the existing value and input '56.6' as the bill amount., Exec_Success

ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/tipEditText, (178, 133), input, "15"): Clear the existing value and input '15' as the tip percentage., Exec_Success

ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), click, NULL):purpose, Exec_Success
ACTION (android.widget.EditText, com.appsbyvir.tipcalculator:id/splitBillEditText, (178, 243), input, "4"): Clear the existing value and input '4' as the number of ways to split the bill., Exec_Success

ASSERT (android.widget.TextView, com.appsbyvir.tipcalculator:id/perPersonEditText, (178, 453), wait_until_text_presence, "text:16.27"): Verify that the 'per person bill' text view displays '16.27' within 10 seconds after calculation., Exec_Success
DONE
````

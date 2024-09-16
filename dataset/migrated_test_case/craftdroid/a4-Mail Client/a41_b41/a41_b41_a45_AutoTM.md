## a41's b41 to a45

### Semantics of Source Test case
> This test case is testing the search functionality in an email application, specifically searching for a specific email subject and verifying its presence.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ASSERT (TextView, com.fsck.k9:id/subject, (), wait_until_text_presence, "Another rabbit hole") : Verify that the email with the subject 'Another rabbit hole' is present within 10 seconds.
> 2. ACTION (TextView, com.fsck.k9:id/search, (), click, NULL) : Click on the search icon to activate the search field.
> 3. ASSERT (EditText, android:id/search_src_text, (), wait_until_element_presence, "android:id/search_src_text") : Verify that the search field is present within 10 seconds.
> 4. ACTION (EditText, android:id/search_src_text, (), input, "Automated") : Input the keyword 'Automated' into the search field and press enter.
> 5. ASSERT (TextView, com.fsck.k9:id/subject, (), wait_until_text_presence, "Automated Software Engineering") : Verify that the email with the subject 'Automated Software Engineering' is present within 10 seconds after the search.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.LinearLayout, park.outlook.sign.in.client:id/filter_tap_area, (16, 40), click, NULL): Clicking on this filter button, a new page appears providing options to filter the mails. The page includes options such as "All", "Unread", and "Flagged".
ACTION (android.widget.Spinner, park.outlook.sign.in.client:id/spinner, (16, 40), click, NULL): Click to reveal filter options for viewing emails. The subsequent page displays a list with filter options "All", "Unread", and "Flagged".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folder_name, (16, 40), click, NULL): Click to display the options 'All', 'Unread', and 'Flagged' in a dropdown list. After clicking, a new ListView component with id "android.widget.ListView" appears, including different filtering options for the mailbox with ids like "park.outlook.sign.in.client:id/filter_name".
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/search_tap_area, (106, 32), click, NULL): Click to open search page. After clicking this control, a search page opens which has a text input area with id "park.outlook.sign.in.client:id/search_text" and a cancel button with id "park.outlook.sign.in.client:id/toolbar_action_cancel".
ACTION (android.widget.Button, park.outlook.sign.in.client:id/icon_search, (274, 32), click, NULL): Click to search mails. Upon clicking this, a search bar with an 'EditText' appears, where user can type the content to be searched. The search bar has an id "park.outlook.sign.in.client:id/search_text". There is also a cancel action indicated by id "park.outlook.sign.in.client:id/toolbar_action_cancel" to cancel the search operation on the next page.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/front_layout, (0, 81), click, NULL): Clicking on this control does not navigate to a new page, but the items within the list view change position and virtual identifiers.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/google_native_ad, (0, 81), click, NULL): Clicking this advertisement leads to the removal of the ad from the current view. It does not navigate to a new page or trigger new widgets to appear. Instead, it simplifies the mail list view by removing the ad element.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/root_view, (8, 89), click, NULL): Click to open ad content. After the click, no new page is opened, and there's no change on the current page. It seems that the click action did not trigger any visible interface changes.
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 219), click, NULL): Click to select the email. After clicking this control, the page navigates to a new page that offer options for the selected email, including 'Mark as Unread', 'Flag', 'Move to Folder', 'Delete', and more.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 214), click, NULL): Clicking on this control navigates to a detailed mail view page. In the next page, you would have options such as Reply or Forward represented by park.outlook.sign.in.client:id/fab_expand_menu_button, Mark as read represented by park.outlook.sign.in.client:id/mailbox_mailmessage_content_readed and other navigational controls.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (268, 216), click, "8 Aug"): Clicking on this control navigates to a new page that displays detailed information about the selected email message. It contains a Go back button, options to Move to Folder, Mark as Spam, and Delete the email, along with more options button. At the bottom, there is a Reply or Forward button.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 235), click, "Another rabbit hole"): Opens the email. The page after clicking this control is the email detailed view page, which has functions such as "Go back", "Move to Folder", "Mark as Spam", "Delete", and "Reply or Forward".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, (88, 258), click, NULL): Click to view the details of an email. After clicking this control, it navigates to the email reading page which contains details of the selected email and options to reply, forward, mark as spam, and delete the email.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 214), click, "tm auto"): Click to view the 'Automated Software Engineering' mail from 'auto tm'. The next page includes mail details, reply or forward options, moving mail to the folder, marking as spam, and deleting functions.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_left, (0, 592), click, NULL): The action of clicking this button is to navigate to the 'Folders' page which contains various email folders like 'Drafts', '存档', 'Outbox', 'Spam', 'Inbox', 'Sent' as listed in the next page JSON.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, NULL) : Clicking on the 'Folders' button brings up a page where you can view and access different mail folders such as 'Drafts', 'Sent', 'Inbox', 'Spam', etc. Each folder represents a category of emails in the mailbox and has a clickable control.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_right, (204, 592), click, NULL): When the account button is clicked, it navigates to the account page that contains UI elements for closing the page, sending an email, adding recipients from contacts, and attaching a file to the email. An editable text field for entering the email's body message is also provided on this page.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/account_text, (262, 623), click, "Account"): Clicking on the account widget reveals personal data, account settings and application-specific settings in a new drop-down. New widgets that appear include interaction with personal data ("park.outlook.sign.in.client:id/highlighted_root_view"), account settings ("park.outlook.sign.in.client:id/text") and application settings ("park.outlook.sign.in.client:id/highlighted_root_view").
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Click to create new mail. After clicking this control, a new page appears presenting the new mailbox creation interface, which includes fields like 'To', 'Cc/Bcc', 'Subject' and automatically includes a default text in the mail body as '--\nSent from Outlook Email App for Android'.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/fab, (136, 585), click, NULL): Opens the email compose page, where you can input recipient, subject and body of the email. After clicking, a new page opens, equipped with Close, Send, Add from contacts and Attach file buttons. The To, Cc/Bcc and Subject fields are present as well.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (TextView, com.appple.app.email:id/subject, (), wait_until_text_presence, "text:Another rabbit hole") : Verify that the text 'Another rabbit hole' is present within 10 seconds.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/search_tap_area, (106, 32), click, NULL): Click to open search page. After clicking this control, a search page opens which has a text input area with id "park.outlook.sign.in.client:id/search_text" and a cancel button with id "park.outlook.sign.in.client:id/toolbar_action_cancel".
~~~
Based on the given action, the corresponding UIAutomator2 code in Python would be as follows(make sure to encapsulate the data with '···'): 

···
d.wait_for_exists(resourceId="com.appple.app.email:id/subject", text='Another rabbit hole', timeout=10)
d.click(106, 32)
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), click, NULL): When the search bar is clicked, a list appears allowing the user to select search parameters such as "from", "to", and "subject". Additionally, an "advanced search" option appears which permits further search customization.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_cancel, (268, 28), click, NULL): To cancel the search operation and return to the mails list page. The page after clicking this control is the inbox page, which has a filter area with id "park.outlook.sign.in.client:id/filter_tap_area" and a search area with id "park.outlook.sign.in.client:id/search_tap_area".
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/tabs_layout, (0, 82), click, NULL): Clicking on this control switches to a different search criteria tab. The tab options represent different methods of categorizing search results, with the options being "all", "from", "to", and "subject". The advanced search button with id "park.outlook.sign.in.client:id/advanced_search" is also present for additional search customization.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (12, 96), click, "all"): Click to filter search to "all". After clicking this control, it demonstrates that no new page is navigated. However, the clicked widget will be selected in the search filter tab, which helps in refining the search results.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/advanced_search, (279, 96), click, NULL): Execute a click to open advanced search. After clicking this control, advanced search options for Unread, Flagged, By Date, and Folder filters appear providing further ways to narrow down search results.
ACTION (android.view.ViewGroup, park.outlook.sign.in.client:id/advanced_search_view, (0,138), click, NULL): Open advanced search. Clicking on this control opens the advanced search view, which occupies a larger area in the subsequent page, indicating more search options are now visible.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), click, NULL): Activate the search field.
ASSERT (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), wait_until_element_presence, "park.outlook.sign.in.client:id/search_text"): Verify that the search field is present within 10 seconds.
~~~
For the provided information and instructions, the corresponding python code with UIAutomator2 would be:

```python
d.click(60, 41)
assert d(resourceId="park.outlook.sign.in.client:id/search_text").wait(timeout=10)
```

Here, `d` is the instance name of the UIAutomator2 device connection, `click` function is used to simulate a click action on the specified coordinates `(60, 41)`, and the `assert` statement with `wait` function is used to verify that the search field is present within 10 seconds. 

It may also be personalized by the program's specific needs or requirements, including different wait times, coordinates, or elements to interact with or verify.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), click, NULL): When the search bar is clicked, a list appears allowing the user to select search parameters such as "from", "to", and "subject". Additionally, an "advanced search" option appears which permits further search customization.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_cancel, (268, 28), click, NULL): Clicking on the cancel button navigates from the search page to the mails list page. The mails list page includes mail list items, a 'Retry' button with id "park.outlook.sign.in.client:id/repeat", a 'Folders' navigation element with id "park.outlook.sign.in.client:id/bottom_bar_left" and an 'Account' navigation element with id "park.outlook.sign.in.client:id/bottom_bar_right".
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/tabs_layout, (0, 82), click, NULL): Clicking on this control switches to a different search criteria tab. The tab options represent different methods of categorizing search results, with the options being "all", "from", "to", and "subject". The advanced search button with id "park.outlook.sign.in.client:id/advanced_search" is also present for additional search customization.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (12, 96), click, "all"): Click to filter search to "all". After clicking this control, it demonstrates that no new page is navigated. However, the clicked widget will be selected in the search filter tab, which helps in refining the search results.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/advanced_search, (279, 96), click, NULL): Execute a click to open advanced search. After clicking this control, advanced search options for Unread, Flagged, By Date, and Folder filters appear providing further ways to narrow down search results.
ACTION (android.view.ViewGroup, park.outlook.sign.in.client:id/advanced_search_view, (0,138), click, NULL): Open advanced search. Clicking on this control opens the advanced search view, which occupies a larger area in the subsequent page, indicating more search options are now visible.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), input, "Automated"): Input the keyword 'Automated' into the search field and press enter.
~~~
Based on your instructions. The corresponding Uiautomator2 code would be: 

···
d(resourceId="park.outlook.sign.in.client:id/search_text").set_text("Automated")
d.press('enter')
···

The code uses the UI element identified by the resourceId "park.outlook.sign.in.client:id/search_text" to input the keyword "Automated". After that, it simulates the press enter action to submit the input.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 152), click, NULL): Checking the checkbox for the automated software engineering email. Clicking on this control does not navigate to a new page, but the email status is changed to 'selected'.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 147), click, "auto tm <autotm123@outlook.com>"): Click to open the email content. The next page displays the detailed content of the email with the subject "Automated Software Engineering". It includes controls such as "Mark as read", "Flag", and actions like "Move to Folder", "Mark as Spam", and "Delete".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folder, (224, 149), click, "Inbox"): Click to open the mail. After clicking, it navigates to the email reading page where you can reply, forward, mark as read, or flag the message.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (268, 149), click, "8 Aug"): Click to view the details of the email sent on "8 Aug". After clicking this control, a new page opens, which presents detailed information about the email, including subject, sending date, sender and email content. The email detail page also provides functionalities such as marking as read, flagging the email, and actions like move, mark as spam, delete, and more options.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 168), click, "Automated Software Engineering"): Click to open the email with subject "Automated Software Engineering". The next page after clicking this element is the email content page, which includes components such as the email body, date received, and sender information. Additionally, there are interactive options to mark as read, flag, and move to folder with ids "mailbox_mailmessage_content_readed", "mailbox_mailmessage_content_flagged", and "toolbar_mailview_action_move" respectively.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, (88, 191), click, NULL): Clicking on this snippet opens the detailed email view page, which includes controls such as "Mark as read", "Flag", "Reply or Forward" and context like "Subject", "Date", and "Sender" informations derived from difference between current page JSON and next page JSON.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), click, "Automated"): Clicking the search field provides a dropdown of relevant search results based on the inputted text. There is no navigation to a new page, rather the current page updates to display search results. The results are displayed in a list where each item has a checkbox with id "park.outlook.sign.in.client:id/checkbox", sender details with id "park.outlook.sign.in.client:id/sender", folder details with id "park.outlook.sign.in.client:id/folder, and other necessary details.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_cancel, (268, 28), click, NULL): Click to cancel the search and go back to the inbox page. The page after clicking this control is the inbox page, which includes mails with contents "Another rabbit hole" and "Automated Software Engineering".
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/tabs_layout, (0, 82), click, NULL): After clicking this control, the layout remains largely the same, implying it is used to filter search results, given the context of its "all", "from", "to" and "subject" children widgets.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (153, 96), click, NULL): Clicking on this control does not navigate to a new page, but it changes the control status of the 'toolbar_action_cancel' with id "park.outlook.sign.in.client:id/toolbar_action_cancel".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (54, 96), click, "from"): Click to modify the search filter attribute 'from'. There is no navigation to a new page, but the search filter context changes to 'from'. This allows the user to narrow down their search scope.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (153, 96), click, "subject"): Click to filter the search by "subject". After clicking, the search filter changes to "subject" indicated by "selected" in the new widget with id "park.outlook.sign.in.client:id/text".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/advanced_search, (279, 96), click, NULL): Click to switch the display status of the advanced search menu. The page after clicking on this control still remains on the search page, but the advanced search settings are displayed instead. The advanced search settings include options for filtering 'Unread' messages with id "park.outlook.sign.in.client:id/unread", 'Flagged' messages with id "park.outlook.sign.in.client:id/flagged", specifying 'Date' with id "park.outlook.sign.in.client:id/date_layout", and selecting 'Folder' with id "park.outlook.sign.in.client:id/folder_layout".
ACTION (android.view.ViewGroup, park.outlook.sign.in.client:id/advanced_search_view, (0, 138), click, NULL): Click to open the advanced search view. No new pages appeared after this interaction, however, some widgets' properties such as size and position have been changed. Examples include the widget of id "park.outlook.sign.in.client:id/advanced_search" and the widget of id "park.outlook.sign.in.client:id/search_text".

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 168), wait_until_text_presence, "Automated Software Engineering"): Verify that the email with the subject 'Automated Software Engineering' is present within 10 seconds after the search.
~~~
### Output:
Given the action to verify an email with a particular subject, and the unique resource ID of the string present, the `wait_until_text_presence` function can be implemented as follows:

```python
import time
timeout = 10  # 10 seconds

def wait_until_text_presence(d, text):
    start = time.time()
    while time.time() - start <= timeout:
        if d(resourceId="park.outlook.sign.in.client:id/subject").get_text() == text:
            return True
        time.sleep(1)
    else:
        return False

assert wait_until_text_presence(d, "Automated Software Engineering")
```
This function continuously checks each second whether the text on the specified UI element matches the desired string. This is repeated until the text is found, or until the specified timeout has been reached.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 152), click, NULL): Checking the checkbox for the automated software engineering email. Clicking on this control does not navigate to a new page, but the email status is changed to 'selected'.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 147), click, "auto tm <autotm123@outlook.com>"): Click to open up the email from the sender 'auto tm <autotm123@outlook.com>'. This leads to a new page displaying the email content in detail with options to Reply, Forward, Move to Folder, Mark as Spam, and Delete. The page also includes a "Go Back" option to return to the inbox.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folder, (224, 149), click, "Inbox"): Clicking on the widget will open the specific email, displaying the details such as theme, date, and time. You can return back, move the email to another folder, mark it as spam, or delete it. Also, options like replying or forwarding the email are provided.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (268, 149), click, "8 Aug"): Click to view the details of the email sent on "8 Aug". After clicking this control, a new page opens, which presents detailed information about the email, including subject, sending date, sender and email content. The email detail page also provides functionalities such as marking as read, flagging the email, and actions like move, mark as spam, delete, and more options.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 168), click, "Automated Software Engineering"): Click to read or interact with the mail titled "Automated Software Engineering". After clicking, an interactive window is opened, showing the content of the email along with options for reply or forward, move to another folder, mark as spam, delete and more options. The window also includes controls for navigating back.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, (88, 191), click, NULL): Clicking on this snippet opens the detailed email view page, which includes controls such as "Mark as read", "Flag", "Reply or Forward" and context like "Subject", "Date", and "Sender" informations derived from difference between current page JSON and next page JSON.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), click, "Automated"): Clicking the search field provides a dropdown of relevant search results based on the inputted text. There is no navigation to a new page, rather the current page updates to display search results. The results are displayed in a list where each item has a checkbox with id "park.outlook.sign.in.client:id/checkbox", sender details with id "park.outlook.sign.in.client:id/sender", folder details with id "park.outlook.sign.in.client:id/folder, and other necessary details.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_cancel, (268, 28), click, NULL): Cancel the search and return to the mailbox page. Clicking on this control navigates to a new page with email list and options for folders and account settings. Also, a function button for a list of actions is available.
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/tabs_layout, (0, 82), click, NULL): After clicking this control, the layout remains largely the same, implying it is used to filter search results, given the context of its "all", "from", "to" and "subject" children widgets.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (153, 96), click, NULL): Clicking on this control does not navigate to a new page, but it changes the control status of the 'toolbar_action_cancel' with id "park.outlook.sign.in.client:id/toolbar_action_cancel".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (12, 96), click, 'all'): The click operation transitions the page to a state indicating a network error with components displaying "No connection" and a "Retry" option. More network-related info is displayed on a banner at the bottom of the page.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (54, 96), click, "from"): Click to modify the search filter. Clicking on this 'from' text does not navigate to a new page, but it changes the selected search filter to 'to'.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (12, 96), click, NULL): The execution of clicking on the "subject" tab navigates to the search page where the searchable elements are categorized differently. It switches the selected state from "all" to "subject".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/advanced_search, (279, 96), click, NULL): Click to navigate to the advanced search menu. The following widgets appear on the next page: "No connection" notification with id "park.outlook.sign.in.client:id/center_title", "Retry" option with id "park.outlook.sign.in.client:id/repeat", and the search field for "Unread" and "Flagged" filters with corresponding checkboxes having the ids "park.outlook.sign.in.client:id/unread" and "park.outlook.sign.in.client:id/flagged" respectively. Additionally, options to input Date and Folder are also visible with ids "park.outlook.sign.in.client:id/date_layout" and "park.outlook.sign.in.client:id/folder_layout" respectively.
ACTION (android.view.ViewGroup, park.outlook.sign.in.client:id/advanced_search_view, (0, 138), click, NULL): Opens up advanced search options. The resulting page has options to mark as read, flag, and delete messages along with offering options for moving the message to a suitable folder or marking it as spam.

````

#### Selected Event(s) and Script
````
~~~
DONE
~~~
Since there are no actions to convert to uiautomator2 code, we can't generate any code in this case. However, as per the guidelines, we are set up and ready to convert future action descriptions into suitable uiautomator2 code in Python when provided.
````
### Success
````
ASSERT (TextView, com.appple.app.email:id/subject, (), wait_until_text_presence, "text:Another rabbit hole") : Verify that the text 'Another rabbit hole' is present within 10 seconds., Exec_Success
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/search_tap_area, (106, 32), click, NULL): Click to open search page. After clicking this control, a search page opens which has a text input area with id "park.outlook.sign.in.client:id/search_text" and a cancel button with id "park.outlook.sign.in.client:id/toolbar_action_cancel"., Exec_Success

ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), click, NULL): Activate the search field., Exec_Success
ASSERT (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), wait_until_element_presence, "park.outlook.sign.in.client:id/search_text"): Verify that the search field is present within 10 seconds., Exec_Success

ACTION (android.widget.EditText, park.outlook.sign.in.client:id/search_text, (60, 41), input, "Automated"): Input the keyword 'Automated' into the search field and press enter., Exec_Success

ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 168), wait_until_text_presence, "Automated Software Engineering"): Verify that the email with the subject 'Automated Software Engineering' is present within 10 seconds after the search., Exec_Success

DONE
````

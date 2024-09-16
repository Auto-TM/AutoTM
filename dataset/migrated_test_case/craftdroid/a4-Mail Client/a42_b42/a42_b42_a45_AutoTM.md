## a42's b42 to a45

### Semantics of Source Test case
> This test case is testing the email composition and sending functionality, verifying both the presence of the "Inbox" label and the successful sending of an email by checking for the email subject in the sent items.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ASSERT (TextView, com.appple.app.email:id/actionbar_title_first, (), wait_until_text_presence, "text:Inbox") : Verify that the "Inbox" text is present within 15 seconds.
> 2. ACTION (TextView, com.appple.app.email:id/compose, (), click, NULL) : Click on the "Compose" button to start composing a new email.
> 3. ASSERT (MultiAutoCompleteTextView, com.appple.app.email:id/to, (), wait_until_element_presence, "id:to") : Verify that the "To" field is present within 15 seconds.
> 4. ACTION (MultiAutoCompleteTextView, com.appple.app.email:id/to, (), input, "autotm1234@gmail.com") : Input the recipient email address 'autotm1234@gmail.com' into the "To" field.
> 5. ACTION (EditText, com.appple.app.email:id/subject, (), input, "ICSTSuperCool") : Input 'ICSTSuperCool' as the subject of the email.
> 6. ACTION (EditText, com.appple.app.email:id/message_content, (), input, "ICSTSuperCoolBody") : Input 'ICSTSuperCoolBody' as the body of the email.
> 7. ACTION (TextView, com.appple.app.email:id/send, (), click, NULL) : Click on the "Send" button to send the email.
> 8. ASSERT (TextView, com.appple.app.email:id/subject, (), wait_until_text_presence, "text:ICSTSuperCool") : Verify that the email with the subject 'ICSTSuperCool' is present within 20 seconds.

### Process
#### Contextual Semantics of Widgets
````

ACTION (android.widget.LinearLayout, park.outlook.sign.in.client:id/filter_tap_area, (16, 40), click, NULL): Click to display mail filters. The next page features a list view with filter options such as All, Unread, and Flagged.
ACTION (android.widget.Spinner, park.outlook.sign.in.client:id/spinner, (16, 40), click, NULL): Opens a dropdown menu. Swiping on this control navigates to a menu where options like All, Unread, and Flagged are selectable. Each option is a separate item within the menu with respective ids "park.outlook.sign.in.client:id/spinner_item_internal".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folder_name, (16, 40), click, NULL): Click to switch folder view. After clicking, a dropdown menu appears with options like 'All', 'Unread', and 'Flagged' for filtering emails.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/search_tap_area, (106, 32), click, NULL): Click to open search. The subsequent page contains a EditText for 'Search Text' with id 'park.outlook.sign.in.client:id/search_text'.
ACTION (android.widget.Button, park.outlook.sign.in.client:id/icon_search, (274, 32), click, NULL): Initiating a search operation. Swiping on this control leads to a search page with an editable field with id "park.outlook.sign.in.client:id/search_text" for text input and a cancel option with id "park.outlook.sign.in.client:id/toolbar_action_cancel".
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/front_layout, (0, 81), click, NULL): Click to navigate. After the interaction, the page displays detailed contents of an email in a 'ViewPager' with a viewpager id 'park.outlook.sign.in.client:id/view_pager'. This view also includes a checkbox for marking the email as read with an id "park.outlook.sign.in.client:id/mailbox_mailmessage_content_readed".
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 97), click, NULL): Clicking on this control selects the email for further actions such as Mark as Unread, Unflag, Move to Folder, Delete which are visible in the toolbar of the next page, having respective IDs "park.outlook.sign.in.client:id/toolbar_action_unread", "park.outlook.sign.in.client:id/toolbar_action_unflag", "park.outlook.sign.in.client:id/toolbar_action_move", "park.outlook.sign.in.client:id/toolbar_action_delete".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 92), click, "tm auto"): Clicking on this control navigates to an email detailed view. In the next page, actions like 'Reply or Forward', 'Mark as read', and email management options such as 'Move to Folder', 'Mark as Spam', and 'Delete' are available. A WebView component displaying the email content also appears.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (268, 184), click, NULL): Click to view specific details. No new page is triggered, however, clicking on this date control likely provides more detailed interaction or view adjustment of the email items displayed. The page remains with email items detailing elements like sender, subject, and snippet unchanged.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 113), click, "Another rabbit hole"): Click to view details of the email. The page after clicking this control shows the email content, with options like "Reply or Forward", "Mark as read", "Flag", and actions such as "Move to Folder", "Mark as Spam", "Delete".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, (88, 136), click, NULL): Click to view details of the email 'Another rabbit hole'. This action does not navigate to a new page but expands options such as 'Reply or Forward' with park.outlook.sign.in.client:id/fab_expand_menu_button and detailed view of the email in park.outlook.sign.in.client:id/view_pager containing actions like 'Mark as read' and options for 'Move to Folder', 'Mark as Spam', 'Delete' or more through icons and buttons displayed.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (251, 94), click, "8 Aug"): Click to view details of the email sent on "8 Aug". The subsequent page displays a detailed view of the email with actions like 'Reply', 'Forward', 'Mark as read', 'Flag', 'Delete', and options to move the email to different folders or mark it as spam.
```
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, (88, 136), click, "Another rabbit hole"): Click to view detailed email. Navigating to detailed email page which includes actions like 'Mark as read', 'Flag', and control options like 'Move to Folder', 'Mark as Spam', 'Delete', along with key details of the email 'From:', 'Subject: Automated Software Engineering', and received date 'August 8, 2024, 18:22'.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_left, (0, 592), click, NULL): Click to navigate to the folders menu. The menu includes options such as 'Drafts', '存档', 'Outbox', 'Spam', 'Inbox', 'Sent' with corresponding ids for each folder option presented.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, "Folders"): Click to navigate to the folder management page, displaying various folders like Drafts, 存档 (Archive), Outbox, Junk, Inbox, and Sent. Each folder is accessible for email categorization.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, NULL): Click to navigate to new page displaying different folders like Drafts, 存档, Outbox, Junk, Inbox, Sent. On clicking, each folder shows respective emails categorized under that folder.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_right, (204, 592), click, "Account"): Click to navigate to account settings or profile. The next page allows editing the account with options like adding a signature, adjusting sync settings, or managing accounts with interactive elements such as "To" (for composing a new email), "Cc/Bcc" (for adding carbon and blind carbon copies), and attachments feature.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/account_text, (262, 623), click, NULL): Click to navigate to account settings. The next page contains settings options including 'Add account', 'Account Settings', and 'Settings' with corresponding widgets like 'park.outlook.sign.in.client:id/accounts_recycler' and 'park.outlook.sign.in.client:id/highlighted_root_view'.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Clicking this control opens an email composition interface. Notable widgets include a "Send" button with id "park.outlook.sign.in.client:id/toolbar_action_send", an editable "To" field marked as park.outlook.sign.in.client:id/edit, "Cc/Bcc" fields and a "Subject" input. There's also the standard mail signature field, and an "Attach file" icon with id "park.outlook.sign.in.client:id/add_attach_btn".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/fab, (136, 585), click, NULL): Pressing the floating action button opens an email composition interface. The new page includes multiple edit fields for sending an email, such as 'To' field with id "park.outlook.sign.in.client:id/edit" for recipient entry and 'Subject' field with id "park.outlook.sign.in.client:id/subject".

        
````

#### Selected Event(s) and Script
````
Given the description of the source test case and the current page's intentions, let's start the test case migration process.

### Source Test Case Step 1:
- **ASSERT (TextView, com.appple.app.email:id/actionbar_title_first, (), wait_until_text_presence, "text:Inbox") : Verify that the "Inbox" text is present within 15 seconds.**

### Current Page's Intent Description:
- There is no direct match for an assertion to check the presence of "Inbox" text in the current page's intentions. However, there is an action that navigates to different folders, including the "Inbox":
  - **ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, "Folders"): Click to navigate to the folder management page, displaying various folders like Drafts, 存档 (Archive), Outbox, Junk, Inbox, and Sent.**

### Proposed Migration Step:
Since the first step in the source test case is to verify the presence of the "Inbox", and given that the current page's intentions include navigating to the folder management page where "Inbox" is listed, the closest matching action would be to navigate to this folder management page and then assert the presence of "Inbox".

~~~
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), wait_until_text_presence, "text:Inbox"): Verify that the "Inbox" text is present within 15 seconds.
~~~
···
assert d(text="Inbox").wait(timeout=15000)
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.LinearLayout, park.outlook.sign.in.client:id/filter_tap_area, (16, 40), click, NULL): Click to filter emails. The page after clicking this control shows a list with filter options including "All", "Unread", and "Flagged".
ACTION (android.widget.Spinner, park.outlook.sign.in.client:id/spinner, (16, 40), click, NULL): Click to select inbox filter. Clicking on this control reveals a dropdown list including options: All, Unread, Flagged.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folder_name, (16, 40), click, NULL): Navigates to a filter selection page displaying options 'All', 'Unread', and 'Flagged'. Swiping on this control does not navigate to a new page, but a listView appears allowing selection among different filter options with ids "park.outlook.sign.in.client:id/spinner_item_internal".
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/search_tap_area, (106, 32), click, NULL): Click to activate search. The subsequent page contains a search text field with id "park.outlook.sign.in.client:id/search_text", demonstrating navigation to a dedicated search page, and various clickable text elements like "all", "from", "to", "subject" for refined search options, alongside an 'Advanced Search' button with id "park.outlook.sign.in.client:id/advanced_search".
ACTION (android.widget.Button, park.outlook.sign.in.client:id/icon_search, (274, 32), click, NULL): Click to initiate search functionality. The next page includes a search text box with id "park.outlook.sign.in.client:id/search_text" to input search queries and multiple filtering options like 'all', 'from', 'to', 'subject' under id "park.outlook.sign.in.client:id/tabs_layout" for detailed search criteria. Also, a button for canceling the search with id "park.outlook.sign.in.client:id/toolbar_action_cancel" is available.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/front_layout, (0, 81), click, NULL): Click to refresh mail list. The next page shows refreshed mail items with updated timestamps and possibly new mail items.
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 271), click, NULL): Tapping on this checkbox does not navigate to a new page but toggles the selection state. After the interaction, a new option panel for "Reply or Forward" with id 'park.outlook.sign.in.client:id/fab_expand_menu_button' appears that allows further actions.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 176), click, NULL): Clicking on this control navigates to the email details page, where options such as "Reply or Forward" with ID "park.outlook.sign.in.client:id/fab_expand_menu_button" are available. Additionally, functionalities like "Mark as read", "Flag", and access to the sender's information indicate an expanded email viewing experience.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, NULL, click, NULL): Click to view detailed email content. Swiping on this control does not navigate to a new page but expands options in-app like 'Reply' or 'Forward' with id "park.outlook.sign.in.client:id/fab_expand_menu_button" and reveals detailed content like message date "August 8, 2024", sender information, and options like 'Mark as read' or 'Flag' the email in the subsequent UI elements.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, NULL, click, "Another rabbit hole"): Click to view email details. Navigating to an email content page displays actions such as 'Reply or Forward', 'Mark as read', 'Flag', controls for the email content, and options like 'Move to Folder', 'Mark as Spam', and 'Delete'.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, NULL, click, NULL): Clicking on this control navigates to the detailed email view. New elements such as "Reply or Forward" button with id "park.outlook.sign.in.client:id/fab_expand_menu_button" and mail content within a "android.webkit.WebView" appear, along with options like "Mark as Spam", "Delete", and "Move to Folder" for mail management.
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 181), click, NULL): The click does not navigate to a new page but positions of some email items slightly change, maintaining the same function without revealing new widgets or features.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, NULL, click, NULL): Clicking on the sender widget leads to the detailed mail view. In the next page, visibly new elements related to the detailed email view such as "Mark as read" with id "park.outlook.sign.in.client:id/mailbox_mailmessage_content_readed" and options for "Reply or Forward" with id "park.outlook.sign.in.client:id/fab_expand_menu_button" appear amongst others.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (268, 268), click, "8 Aug"): Click to open detailed email view. In the response page, detailed sections of the email are displayed, such as email content in a WebKit view, recipient and date details, and additional interaction options like marking as read, moving to a folder, marking as spam, or deleting the email. Additionally, there are options for replying or forwarding the email.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 235), click, "Another rabbit hole"): Click to navigate or open the email detail. The page after clicking this element displays the complete content of the email titled "Another rabbit hole".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/center_title, (48, 359), click, "No connection"): Click to attempt to reconnect. The Retry button with id "park.outlook.sign.in.client:id/repeat" becomes clickable for reconnection attempt.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/repeat, (249, 350), click, NULL): Click to attempt reconnecting or refreshing the data. Swiping on this control does not navigate to a new page, but a floating action button with id "park.outlook.sign.in.client:id/fab_expand_menu_button" and a description "Reply or Forward" appears, suggesting actions related to email management are now available.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_left, (0, 592), click, NULL): Click to navigate. The page after clicking this control is the folder navigation page, which includes multiple folder options like Drafts, Sent, Inbox each with their respective clickable highlights. Notably, clicking on the widget with id "park.outlook.sign.in.client:id/highlighted_root_view" brings different folder views like Inbox with id "park.outlook.sign.in.client:id/text".
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/folders_text, (0, 623), click, "Folders"): Click to navigate to folders list. The next page includes options such as Drafts, 存档 (Archive), Outbox, Spam, Inbox, and Sent folders.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, NULL): Click to navigate to the folder management page. The next screen includes options for different folders like 'Drafts', '存档' (Archive), 'Outbox', 'Spam', 'Inbox', and 'Sent', located within highlighted sections (park.outlook.sign.in.client:id/highlighted_root_view) that allow further interactions.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_right, (204, 592), click, NULL): Click to navigate to the account settings page. The next page includes elements for email composition such as To, Cc/Bcc, Subject, and an Attach file button with respective ids "park.outlook.sign.in.client:id/edit", "park.outlook.sign.in.client:id/edit", "park.outlook.sign.in.client:id/subject", and "park.outlook.sign.in.client:id/add_attach_btn".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/account_text, (262, 623), click, NULL): to navigate to the account settings page displaying account options which includes 'Add account', 'Personal Data', 'Settings' with respective elements for further interaction.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Clicking this button opens a page where the user can compose a new email. New widgets include fields for To, Cc/Bcc, Subject, and email content, with options for attachments and sending the email.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/fab, (136, 585), click, NULL): Click to compose a new email. The next page allows entering recipient ("To"), adding from contacts, setting "Cc/Bcc", specifying "Subject", attaching files, and composing the email body. New elements include "Send" button with id "park.outlook.sign.in.client:id/toolbar_action_send" and editable fields for email composition.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Click to start composing a new email.
~~~
···
d.click(112, 573)
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to navigate to inbox. The page after clicking this control includes a filter area with id "park.outlook.sign.in.client:id/filter_tap_area" and a search area with id "park.outlook.sign.in.client:id/search_tap_area".
ACTION (android.widget.TextView, autotm123@hotmail.com, (72, 38), click, NULL): Clicking on the email address does not navigate to a new page, but maintains the current email composition context. No new elements or changes occurred between the current page and the next page JSON data.
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL):purpose: Click to focus on the recipient input field, allowing the user to start typing or editing the email recipient's address. Swiping on this control does not navigate to a new page, but enables the user to input or edit recipient details directly on this page.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Clicking on this control allows for input in the "To" field of the email composition page. No new page appears but enables the user to enter recipient details for the email.
~~~
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/users_icon, (270, 81), click, NULL): Click to open contacts. Upon clicking, a new snackbar message indicating 'No Contacts' appears at the bottom of the screen with id "park.outlook.sign.in.client:id/snackbar_text".
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 133), click, NULL): Click on Cc/Bcc text field facilitates the display expansion for entering carbon copy (Cc) addresses. This control interaction does not navigate to a new page, but expands visibility to include Bcc field and provides access to add participants from contacts.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL): Clicking on this control allows the user to focus on the subject field for input, but clicking does not navigate to a new page or bring up a new dialog.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, NULL): Tapping on this control allows for input into the subject field of an email. Swiping on this control does not navigate to a new page, but allows the user to provide a subject for the email they are composing.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to attach file. The page after this action leads to a gallery page with options like "Image or video", "Take photo", "File".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. Clicking on this control does not navigate to a new page, but allows the user to input text into the email body which may include signature or additional content.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), wait_until_element_presence): Verify that the "To" field is present within 15 seconds.
~~~
```python
assert d(resourceId="park.outoutlook.sign.in.client:id/edit").wait(timeout=15000)
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the compose mail page. Swiping on this control does not navigate to a new page, but a dialog/popupMenu which includes edit and delete item appears. the new dialog has a edit button with id "autotm.test:id/edit_button" and a delete item component with id "autotm.test:id/delete_item".
ACTION (android.widget.TextView, autotm123@hotmail.com, (72, 38), click, NULL): Clicking on the email address does not navigate to a new page, but maintains the current email composition context. No new elements or changes occurred between the current page and the next page JSON data.
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL):purpose: Click to focus on the recipient input field, allowing the user to start typing or editing the email recipient's address. Swiping on this control does not navigate to a new page, but enables the user to input or edit recipient details directly on this page.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Clicking on this control allows for input in the "To" field of the email composition page. No new page appears but enables the user to enter recipient details for the email.
~~~
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/users_icon, (270, 81), click, NULL): Click to open contacts. Upon clicking, a new snackbar message indicating 'No Contacts' appears at the bottom of the screen with id "park.outlook.sign.in.client:id/snackbar_text".
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 133), click, NULL): Click on Cc/Bcc text field facilitates the display expansion for entering carbon copy (Cc) addresses. This control interaction does not navigate to a new page, but expands visibility to include Bcc field and provides access to add participants from contacts.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL): Clicking on this control allows the user to focus on the subject field for input, but clicking does not navigate to a new page or bring up a new dialog.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, NULL): Tapping on this control allows for input into the subject field of an email. Swiping on this control does not navigate to a new page, but allows the user to provide a subject for the email they are composing.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to attach file. The page after this action leads to a gallery page with options like "Image or video", "Take photo", "File".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. Clicking on this control does not navigate to a new page, but allows the user to input text into the email body which may include signature or additional content.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL):purpose: Click to focus on the recipient input field, allowing the user to start typing or editing the email recipient's address.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "autotm1234@gmail.com"):purpose: Input the recipient email address 'autotm1234@gmail.com' into the "To" field.
~~~
···
d.click(72, 88)
d.send_keys("autotm1234@gmail.com", clear=True)
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to navigate to inbox. The page after clicking this control includes a filter area with id "park.outlook.sign.in.client:id/filter_tap_area" and a search area with id "park.outlook.sign.in.client:id/search_tap_area".
ACTION (android.widget.TextView, autotm123@hotmail.com, (72, 38), click, NULL): Clicking on the email address does not navigate to a new page, but maintains the current email composition context. No new elements or changes occurred between the current page and the next page JSON data.
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL):purpose: Click to focus on the recipient input field, allowing the user to start typing or editing the email recipient's address. Swiping on this control does not navigate to a new page, but enables the user to input or edit recipient details directly on this page.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Clicking on this control allows for input in the "To" field of the email composition page. No new page appears but enables the user to enter recipient details for the email.
~~~
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/users_icon, (270, 81), click, NULL): Click to open contacts. Upon clicking, a new snackbar message indicating 'No Contacts' appears at the bottom of the screen with id "park.outlook.sign.in.client:id/snackbar_text".
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 133), click, NULL): Click on Cc/Bcc text field facilitates the display expansion for entering carbon copy (Cc) addresses. This control interaction does not navigate to a new page, but expands visibility to include Bcc field and provides access to add participants from contacts.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL): Clicking on this control allows the user to focus on the subject field for input, but clicking does not navigate to a new page or bring up a new dialog.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, NULL): Tapping on this control allows for input into the subject field of an email. Swiping on this control does not navigate to a new page, but allows the user to provide a subject for the email they are composing.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to attach file. The page after this action leads to a gallery page with options like "Image or video", "Take photo", "File".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. Clicking on this control does not navigate to a new page, but allows the user to input text into the email body which may include signature or additional content.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), input, "ICSTSuperCool"): Input 'ICSTSuperCool' as the subject of the email.
~~~
···
d.click(72, 179)
d.send_keys("ICSTSuperCool")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the email draft. After clicking, a confirmation dialog appears asking "Do you want to save to Drafts?" with options "No" and "Yes", identified by "android:id/button2" and "android:id/button1" respectively.
ACTION (android.widget.TextView, ICSTSuperCool, (72, 38), click, "ICSTSuperCool"): The click on this control does not navigate to a new page, but maintains the same interface with no changes observed in content or interactive elements.
```
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, (72, 179), click, "ICSTSuperCool"): Click to edit the subject 'ICSTSuperCool'. Swiping on this control does not navigate to a new page, but allows direct editing of the subject field on the same page.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, NULL): Clicking on this control does not navigate to a new page, but allows text input in the 'To' field of an email, preparing for sending an email.
ACTION (android.widget.TextView, Cc/Bcc, (16, 126), click, NULL): Click to expand or modify the Cc/Bcc fields in the email composition. After clicking, the view changes to separate Cc and Bcc input fields, providing options to add addresses directly or from contacts with 'park.outlook.sign.in.client:id/users_icon'.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Click to activate the text field for email entry. Swiping on this control does not navigate to a new page, but allows the user to input text for the 'To' field. Subsequent interactions may include adding recipients from contacts, indicated by the presence of an 'Add to carbon copy from contacts' button with id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, "ICSTSuperCool"): Clicking on this control opens the subject field for editing. Swiping on this control does not navigate to a new page, but allows text input for subject of the email, as indicated by interaction with subject text field id "park.outlook.sign.in.client:id/subject".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, "ICSTSuperCool"): Click to edit the subject of the email. Clicking on this control does not navigate to a new page, but allows editing the email's subject directly on the current page.
~~~
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to attach files. After the interaction, an add attachment page appears showing options like 'Image or video', 'Take photo', and 'File'. New controls are visible for selecting these options.
~~~
ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. Clicking this control does not navigate to a new page, but toggles the emoji keyboard with id "park.outlook.sign.in.client:id/toggle_btn".

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. 
ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/mailbox_create_new_body, (16, 228), input, "ICSTSuperCoolBody"): Input 'ICSTSuperCoolBody' as the body of the email.
~~~
···
d.click(16, 228)
d(resourceId="park.outoutlook.sign.in.client:id/mailbox_create_new_body").set_text("ICSTSuperCoolBody")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close email editor. Clicking on this control prompts a dialog asking 'Do you want to save to Drafts?', with options 'No' (android:id/button2) and 'Yes' (android:id/button1).
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/toggle_btn, (274, 550), click, NULL): Click to open the emoji keyboard. Swiping on this control does not navigate to a new page, but it toggles the emoji keyboard on the screen for text input enhancement.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Click to edit the recipient. Swiping on this control does not navigate to a new page, but a new widget with the option to "Add from contacts" appears, with id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, NULL): Clicking on this control does not navigate to a new page, but it enables text entry in the 'To' field for sending an email. The editable field indicated allows for insertion of email addresses directly. After clicking, an additional control 'Add from contacts' with id 'park.outlook.sign.in.client:id/users_icon' appears, offering an alternative method to add recipients by selecting from contacts.
ACTION (android.widget.TextView, , (16, 126), click, "Cc/Bcc"): Click to edit CC/BCC field, revealing options to add more recipients directly from contacts. The new widget 'Add to carbon copy from contacts' has an id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL): Click to set email subject. Swiping on this control does not navigate to a new page, but allows editing the subject field with id "park.outlook.sign.in.client:id/subject".
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, "ICSTSuperCool"): Click to edit the subject of the email. Interaction reveals no immediate page change, but focuses input on the email's subject field which currently contains the text "ICSTSuperCool".
~~~
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to add an attachment. Clicking on this control navigates to a new page where options to add 'Image or video', 'Take photo', and 'File' appear. The options are given with the IDs: 'park.outlook.sign.in.client:id/add_attach_action'.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. No new page appears; no new widgets are introduced.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 228), input, "ICSTSuperCoolBody"): Input 'ICSTSuperCoolBody' as the body of the email.
~~~
···
d.click(16, 228)
d.send_keys("ICSTSuperCoolBody")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the email composition. Dialog for saving draft appears with options 'Yes' and 'No'.
ACTION (android.widget.TextView, autotm123@hotmail.com, (72, 38), click, NULL): Clicking on this control does not navigate to a new page, but maintains the current email composition interface allowing further user interaction with elements like "To", "Cc/Bcc", and "Subject".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/toggle_btn, (274, 550), click, NULL): Click to open the emoji and sticker interface. Dialog with emoji options appears containing tabs for emojis and stickers with ids "park.outlook.sign.in.client:id/panel_btn_smiles", "park.outlook.sign.in.client:id/panel_btn_stickers", and a close button "park.outlook.sign.in.client:id/panel_btn_close". A scrollable view also opens with various stickers accessible by id "park.outlook.sign.in.client:id/sticker".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Clicking on this control enables editing the recipient of the email. The page after clicking includes an additional button with id "park.outlook.sign.in.client:id/users_icon" for adding contacts from the address book.
ACTION (android.widget.TextView, , (16, 126), click, "Cc/Bcc"): Clickable to toggle Cc/Bcc fields. Swiping on this control does not navigate to a new page, but expands the email form to include separate Cc and Bcc fields for specifying additional recipients, along with an option to add contacts to carbon copy from contacts with id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, NULL): Click to edit email contents. Clicking on this control does not navigate to a new page, but enables editing of 'To', 'Cc', 'Bcc', and 'Subject' fields directly on the current page. Additional changes are observed in the next page JSON such as the separation of 'Cc' and 'Bcc' into distinct fields and the addition of a button to add carbon copy from contacts with id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, "Subject"): The click on the 'Subject' widget launches the email subject field editor with id "park.outlook.sign.in.client:id/subject" having the prefilled text "ICSTSuperCool". This facilitates the user in quickly editing or verifying the subject line of an email draft.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, "ICSTSuperCool"): Click to edit the subject. Updates the subject in the email compose window. This change reflects immediately in the subject displayed at the top of the email body with the text "ICSTSuperCool".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to add attachment. Swiping on this control navigates to a new page, which offers options to add image, video, or file. The new page includes clickable components with ids "park.outlook.sign.in.client:id/add_attach_action" for actions such as "Image or video", "Take photo", and "File".
ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "ICSTSuperCoolBody\n\n--\nSent from Outlook Email App for Android"): Click to edit mail body content. Swiping on this control does not navigate to a new page, but allows editing of the existing mail body in the same layout.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/send, (), click, NULL): Click on the "Send" button to send the email.
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/subject, (72, 179), wait_until_text_presence, "text:ICSTSuperCool"): Verify that the email with the subject 'ICSTSuperCool' is present within 20 seconds.
DONE
~~~
···
d(resourceId="park.outlook.sign.in.client:id/send").click()
assert d(text="ICSTSuperCool").wait(timeout=20000)
···
````
### Success
````
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), wait_until_text_presence, "text:Inbox"): Verify that the "Inbox" text is present within 15 seconds., Exec_Success

ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Click to start composing a new email., Exec_Success

ASSERT (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), wait_until_element_presence): Verify that the "To" field is present within 15 seconds., Exec_Success

ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL):purpose: Click to focus on the recipient input field, allowing the user to start typing or editing the email recipient's address., Exec_Success
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "autotm1234@gmail.com"):purpose: Input the recipient email address 'autotm1234@gmail.com' into the "To" field., Exec_Success

ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), input, "ICSTSuperCool"): Input 'ICSTSuperCool' as the subject of the email., Exec_Success

ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. , Exec_Success
ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/mailbox_create_new_body, (16, 228), input, "ICSTSuperCoolBody"): Input 'ICSTSuperCoolBody' as the body of the email., Exec_Fail

ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 228), input, "ICSTSuperCoolBody"): Input 'ICSTSuperCoolBody' as the body of the email., Exec_Success

ACTION (android.widget.TextView, park.outlook.sign.in.client:id/send, (), click, NULL): Click on the "Send" button to send the email., Exec_Success
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/subject, (72, 179), wait_until_text_presence, "text:ICSTSuperCool"): Verify that the email with the subject 'ICSTSuperCool' is present within 20 seconds., Exec_Success
DONE
````

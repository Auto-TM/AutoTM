## a41's b42 to a45

### Semantics of Source Test case
> This test case is testing the email composition and sending functionality in the K-9 Mail app. It verifies the presence of the Inbox, composes a new email, inputs recipient, subject, and body, sends the email, and finally verifies the presence of the sent email in the message list.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ASSERT (TextView, com.fsck.k9:id/actionbar_title_first, (), wait_until_text_presence, "Inbox") : Verify that the 'Inbox' text is present within 15 seconds.
> 2. ACTION (TextView, com.fsck.k9:id/compose, (), click, NULL) : Click on the 'Compose' button to start composing a new email.
> 3. ASSERT (MultiAutoCompleteTextView, com.fsck.k9:id/to, (), wait_until_element_presence, "com.fsck.k9:id/to") : Verify that the 'To' field is present within 15 seconds.
> 4. ACTION (MultiAutoCompleteTextView, com.fsck.k9:id/to, (), input, "autotm1234@gmail.com") : Input the recipient email 'autotm1234@gmail.com' into the 'To' field and hide the keyboard.
> 5. ACTION (EditText, com.fsck.k9:id/subject, (), input, "ICSTSuperCool") : Input the subject 'ICSTSuperCool' into the 'Subject' field.
> 6. ACTION (EditText, com.fsck.k9:id/message_content, (), input, "ICSTSuperCoolBody") : Input the body 'ICSTSuperCoolBody' into the 'Message text' field.
> 7. ACTION (TextView, com.fsck.k9:id/send, (), click, NULL) : Click on the 'Send' button to send the composed email.
> 8. ASSERT (TextView, com.fsck.k9:id/subject, (), wait_until_text_presence, "ICSTSuperCool") : Verify that the sent email with the subject 'ICSTSuperCool' is present in the message list within 20 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.LinearLayout, park.outlook.sign.in.client:id/filter_tap_area, (16, 40), click, NULL): Clicking on this control brings up ListView with various filter options such as All, Unread, and Flagged. This page includes list items each with id 'park.outlook.sign.in.client:id/spinner_item_internal' indicating different filter options like All Inbox, Unread messages, and Flagged messages.
ACTION (android.widget.Spinner, park.outlook.sign.in.client:id/spinner, (16, 40), click, NULL): Click to open dropdown menu. The new page after clicking this control includes a dropdown list with options 'All', 'Unread', and 'Flagged'.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folder_name, (16, 40), click, NULL): Clicking changes the mail folder view. The next page displays options such as "All", "Unread", and "Flagged" for filtering mails.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/search_tap_area, (106, 32), click, NULL): Click to open the search feature. The page after clicking this control is the search page, which allows editing search text with id "park.outlook.sign.in.client:id/search_text" and a toolbar action cancel button with id "park.outlook.sign.in.client:id/toolbar_action_cancel".
ACTION (android.widget.Button, park.outlook.sign.in.client:id/icon_search, (274, 32), click, NULL): Click to activate the search. The page after clicking this control provides a detailed search interface, which includes fields to enter search text, with id "park.outlook.sign.in.client:id/search_text", and options to cancel the search with id "park.outlook.sign.in.client:id/toolbar_action_cancel".
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/front_layout, (0, 81), click, NULL): Click to refresh the view. No new pages appear, but inbox items are restructured with updated emails having ids "park.outlook.sign.in.client:id/checkbox", "park.outlook.sign.in.client:id/sender", "park.outlook.sign.in.client:id/date", "park.outlook.sign.in.client:id/subject", "park.outlook.sign.in.client:id/snippet" with contents "tm auto", "8 Aug", "Another rabbit hole" and "auto tm", "8 Aug", "Automated Software Engineering" respectively.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/root_view, (8, 89), click, NULL): Clicking on this control opens up an email page where actions like 'Mark as read', 'Mark as Spam', 'Move to Folder', 'Delete', and 'Reply or Forward' are available. New widgets such as a ViewPager for email content with id 'park.outlook.sign.in.client:id/view_pager' and controls for email actions like delete and spam with ids 'park.outlook.sign.in.client:id/toolbar_mailview_action_delete' and 'park.outlook.sign.in.client:id/toolbar_mailview_action_spam' appear.
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 219), click, NULL): Click to select the email. Clicking on this control selects the email for further actions such as mark as unread, move to folder, or delete, shown on the toolbar of the next page.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 214), click, "tm auto"): Click to expand email details. The page after clicking this control is the email detail page, which has a reply or forward menu with id "park.outlook.sign.in.client:id/fab_expand_menu_button" and contains various mailbox message content, including a marked as read checkbox with id "park.outlook.sign.in.client:id/mailbox_mailmessage_content_readed".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (251, 216), click, "8 Aug"): Clicking on this control navigates to a detailed mail page. The new page includes interactions like "Reply or Forward" with a spinner component with id "park.outlook.sign.in.client:id/fab_expand_menu_button". Additionally, actions like marking as read, flagging emails, managing recipients, and view enhancements can be performed, with additional details displayed in an expanded email content view facilitated by a ViewPager with id "park.outlook.sign.in.client:id/view_pager".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject, (88, 235), click, "Another rabbit hole"): Click to view details of the email. The next page includes options for Reply or Forward with id "park.outlook.sign.in.client:id/fab_expand_menu_button" and displays the full content and details of the email.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, (88, 258), click, "Another rabbit hole"): Click to view detailed message. The next page displays a detailed view of the email with the subject 'Another rabbit hole', allowing actions such as 'Mark as read', 'Flag', and other operations such as 'Move to Folder', 'Mark as Spam', 'Delete'. These are accessible via various controls like checkboxes and buttons with respective IDs like 'park.outlook.sign.in.client:id/mailbox_mailmessage_content_readed' for marking as read.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_left, (0, 592), click, NULL): Click to navigate to folders. The next page includes multiple folders like Drafts, 存档(Archive), Outbox, Junk, Inbox, and Sent with their respective TextView components displaying the folder names.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, "Folders"): Click to navigate to folders list. This action brings up a menu with various folder options such as Drafts, 存档(archive), Outbox, Spam, Inbox, and Sent.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, NULL): Clicking on this control does not navigate to a new page, but a modal appears with options for different folders including "Drafts", "存档", "Outbox", "Spam", "Inbox", "Sent". Each folder option is represented by a TextView with their respective ids and texts.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_right, (204, 592), click, "Account"): Click to switch to account management. After clicking, elements for sending an email such as To, Cc/Bcc fields, Subject, and Send button appear on the next page. This includes a new editable field for the email body with id "park.outlook.sign.in.client:id/mailbox_create_new_body".
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/account_text, (262, 623), click, NULL): Accessing the account options from the bottom navigation bar opens a new page with user account settings and preferences. On the subsequent page, new elements like "Add account", "Account autotm123@hotmail.com", and "Account Settings" are now available, promoting user interaction with account management features.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Click to navigate to compose mail page. The page after clicking this control has multiple widgets for composing an email. It includes fields like To, CC/Bcc, Subject, and an editing area for writing the email. The Send button is located on the toolbar with id "park.outlook.sign.in.client:id/toolbar_action_send".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/fab, (136, 585), click, NULL): Clicking the fab button navigates to the compose email page, allowing the user to send an email with fields for recipient ("To"), copies ("Cc/Bcc"), subject, body, and options to attach files and send the email. New elements include 'Close' ImageButton, 'Send' TextView, recipient EditText, 'Add from contacts' ImageButton, 'Subject' label and EditText, 'Attach file' ImageButton, and the email body EditText.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/folder_name, (16, 40), wait_until_text_presence, "Inbox"): Verify that the 'Inbox' text is present within 15 seconds.
~~~
···
assert d(resourceId="park.outlook.sign.in.client:id/folder_name").wait(text="Inbox", timeout=15)
···
````
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
~~~
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Click to open email composition interface.
~~~
···
d.click(112, 573)
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the compose mail. Navigating back to Inbox which displays emails and mailbox actions.
ACTION (android.widget.TextView, autotm123@hotmail.com, (72, 38), click, NULL): Clicking on the email address does not navigate to a new page, but maintains the current email composition context. No new elements or changes occurred between the current page and the next page JSON data.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, NULL): Click to send an email. Attempt to send triggers a validation message, showing a Snackbar with message "Please specify a recipient." with id "park.outlook.sign.in.client:id/snackbar_text".
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL):purpose: Click to focus on the recipient input field, allowing the user to start typing or editing the email recipient's address. Swiping on this control does not navigate to a new page, but enables the user to input or edit recipient details directly on this page.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Clicking on this control allows for input in the "To" field of the email composition page. No new page appears but enables the user to enter recipient details for the email.
~~~
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/users_icon, (270, 81), click, NULL): Click to open contacts. Upon clicking, a new snackbar message indicating 'No Contacts' appears at the bottom of the screen with id "park.outlook.sign.in.client:id/snackbar_text".
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 133), click, NULL): Click on Cc/Bcc text field facilitates the display expansion for entering carbon copy (Cc) addresses. This control interaction does not navigate to a new page, but expands visibility to include Bcc field and provides access to add participants from contacts.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL): Clicking on this control allows the user to focus on the subject field for input, but clicking does not navigate to a new page or bring up a new dialog.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, NULL): Tapping on this control allows for input into the subject field of an email. Swiping on this control does not navigate to a new page, but allows the user to provide a subject for the email they are composing.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to attach file. The page after this action leads to a gallery page with options like "Image or video", "Take photo", "File".
~~~
ACTION (android.widget.EditText, park.outout.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the body of the email. After interaction, addition of emoji keyboard enhances user expression capabilities via 'Open emoji keyboard' button with id "park.outlook.sign.in.client:id/toggle_btn".
~~~

````

#### Selected Event(s) and Script
````
Based on the provided details, the source test case involves verifying the presence of the Inbox, composing an email, and verifying the sent email. The executed action sequence indicates that the email composition interface has been opened successfully.

From the current page's intention description, the next logical step aligns with the second step of the source test case, which is to click on the 'Compose' button to start composing a new email. However, since the composition interface is already open as indicated by the executed action sequence, we can proceed to the next step.

The next step in the source test case is to verify the presence of the 'To' field and then input the recipient email. From the intentions, we have two relevant actions:
- ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL): Click to focus on the recipient input field.
- ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "​"): Allows for input in the "To" field.

Since the 'To' field needs to be verified and then filled, the appropriate action would be to focus on the recipient input field and input the email address. Therefore, the next action to perform is:

~~~
ASSERT (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), wait_until_element_presence, "park.outoutlook.sign.in.client:id/edit") : Verify that the 'To' field is present within 15 seconds.
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL): Click to focus on the recipient input field.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), input, "autotm1234@gmail.com"): Input the recipient email 'autotm1234@gmail.com' into the 'To' field.
~~~
···
assert d(resourceId="park.outlook.sign.in.client:id/edit").wait(timeout=15000)
d.click(72, 88)
d(resourceId="park.outlook.sign.in.client:id/edit").set_text("autotm1234@gmail.com")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the email composition screen. Clicking on this control prompts a dialog asking 'Do you want to save to Drafts?' with options 'No' at id "android:id/button2" and 'Yes' at id "android:id/button1".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), click, "autotm1234@gmail.com"): Clicking on this control updates the recipients in the email to include "autotm1234@gmail.com". No navigation to a new page occurs, but the content of the "To" field is updated to reflect the new recipient.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, NULL): Click to navigate from email composition to the main inbox view. The page after clicking this button displays the inbox, allowing users to search and filter emails. New controls include park.outlook.sign.in.client:id/filter_tap_area for filters and park.outlook.sign.in.client:id/search_tap_area for search.
ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/edit, (72, 88), click, "autotm1234@gmail.com"): Click to edit the 'To' field. Swiping on this control does not navigate to a new page, but allows the user to modify the recipient's email address directly on the current page.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/users_icon, (270, 81), click, NULL): Clicking on users_icon navigates to a contacts page which includes a notification with "No Contacts" message and an option to go back.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 133), click, NULL): Tapping on the Cc/Bcc field brings up new editable fields for Cc and Bcc email addresses. The new Cc field has an id "park.outlook.sign.in.client:id/edit" at coordinates (72,169) for entering carbon copy addresses, and a new Bcc field has an id "park.outlook.sign.in.client:id/edit" at coordinates (72,214) for entering blind carbon copy addresses. Additionally, icons for adding contacts to Cc and Bcc are provided with respective ids "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL): Clicking the 'Subject' label aids in focusing the subject input field for email composition.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 179), click, NULL): Click to edit the subject of the email. After interaction, an editable text field focuses allowing further input. Swiping on this control does not navigate to a new page, but modifies element dimensions and positions, especially the 'To' field changing into a bubble layout with an editable text field.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 171), click, NULL): Click to attach a file or media. Swiping on this control navigates to a new page, showing options to attach an image/video, take a photo, or attach a file. The new page includes buttons with ids "park.outlook.sign.in.client:id/add_attach_action" for each media type.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 228), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. Swiping on this control brings up the emoji keyboard with id "park.outlook.sign.in.client:id/toggle_btn". The new toggle for emoji keyboard appears at (274, 390).

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL):purpose
~~~
Certainly, I will transform the provided test semantic description into UIAutomator2 code in Python:

### Input:
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL):purpose

### Output:
···
d.click(16, 171)
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the email composition. Swiping this control leads to a dialog "Do you want to save to Drafts?" with options "No" (android:id/button2) and "Yes" (android:id/button1).
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, NULL): Sending an email. The next page displays a "Sending..." notification with id "park.outlook.sign.in.client:id/snackbar_text" and an "Edit" option with id "park.outlook.sign.in.client:id/snackbar_action".
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/bubble_item, (72, 89), click, NULL): Click to edit recipient email. Swiping on this control does not navigate to a new page, but updates the recipient email from autotm1234@gmail.com to a editable input field with id "park.outlook.sign.in.client:id/edit".
~~~
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/bubble_item, (72, 89), click, NULL): Clicking on this control triggers the display of an email address popup for selection. The popup contains an email address "autotm1234@gmail.com" with id "park.outlook.sign.in.client:id/email_popup".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (108, 95), click, "autotm1234@gmail.com"): Click to select the email address. Swiping on this control navigates to a new page, which includes an email popup with id "park.outlook.sign.in.client:id/email_popup".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (16, 125), click, NULL): Click to enter recipient details. The page after clicking this control is the email composition page, where recipients' email addresses can be added or edited.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 169), click, NULL): Click to edit Cc/Bcc fields. The next page shows separated 'Cc' and 'Bcc' fields, each with editable text fields and an option to add from contacts, enhancing email composition flexibility.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 207), click, NULL): Clicking on this control does not navigate to a new page, but allows editing the subject of the email. The control for editing the subject, id "park.outlook.sign.in.client:id/subject", becomes available post-click.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), click, NULL): Clicking on this control allows for input in the subject field of an email composition form. No new page opens, and no new widgets appear as a result of this action.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 207), click, NULL): Click to add an attachment. Opens a page/dialog with options: "Gallery is empty ;(" indicates no images or videos available, "Image or video" for adding multimedia, "Take photo" to capture a new photo, and "File" to attach documents.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 264), click, "\n\n--\nSent from Outlook Email App for Android"): Clicking on the email body does not navigate to a new page, but allows editing directly on this page. The next screen after interaction shows an "Open emoji keyboard" button with id "park.outlook.sign.in.client:id/toggle_btn" to enhance message composition.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), click, NULL): Click to focus on the subject input field.
~~~
Certainly, based on the information provided for performing actions with the UIAutomator2 in Python, the necessary code snippet to execute the action described would be as follows:

```python
d.click(72, 215)
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the email composition. Swiping this control leads to a dialog "Do you want to save to Drafts?" with options "No" (android:id/button2) and "Yes" (android:id/button1).
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, NULL): Click to send the email. After interaction, navigates to inbox page with new emails loaded, demonstrating that the action triggers the sending process and subsequent inbox refresh.
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/bubble_item, (72, 89), click, NULL): Click to edit recipient email. Swiping on this control does not navigate to a new page, but updates the recipient email from autotm1234@gmail.com to a editable input field with id "park.outlook.sign.in.client:id/edit".
~~~
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/bubble_item, (72, 89), click, NULL): Clicking on this control triggers the display of an email address popup for selection. The popup contains an email address "autotm1234@gmail.com" with id "park.outlook.sign.in.client:id/email_popup".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (108, 95), click, "autotm1234@gmail.com"): Click to select recipient 'autotm1234@gmail.com' for the email. Selecting this recipient does not navigate to a new page, but ensures the 'To' field is correctly populated with 'autotm1234@gmail.com'.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (16, 125), click, NULL): Click to enter recipient details. The page after clicking this control is the email composition page, where recipients' email addresses can be added or edited.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 169), click, NULL): Click to edit Cc/Bcc fields. The next page shows separated 'Cc' and 'Bcc' fields, each with editable text fields and an option to add from contacts, enhancing email composition flexibility.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 207), click, NULL): Clicking on this control does not navigate to a new page, but allows editing the subject of the email. The control for editing the subject, id "park.outlook.sign.in.client:id/subject", becomes available post-click.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), click, NULL): Clicking on this control allows for input in the subject field of an email composition form. No new page opens, and no new widgets appear as a result of this action.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 207), click, NULL): Click to add an attachment. Opens a page/dialog with options: "Gallery is empty ;(" indicates no images or videos available, "Image or video" for adding multimedia, "Take photo" to capture a new photo, and "File" to attach documents.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 264), click, "\n\n--\nSent from Outlook Email App for Android"): Clicking on the email body does not navigate to a new page, but allows editing directly on this page. The next screen after interaction shows an "Open emoji keyboard" button with id "park.outlook.sign.in.client:id/toggle_btn" to enhance message composition.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), input, "ICSTSuperCool"): Input the subject 'ICSTSuperCool' into the 'Subject' field.
~~~
···
d.click(72, 215)
d.send_keys("ICSTSuperCool")
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the composing mail draft. Swiping on this control transitions to a dialog asking whether to save to Drafts. The dialog displays a message with id "android:id/message" and offers choices 'No' and 'Yes' with IDs "android:id/button2" and "android:id/button1", respectively.
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/subject, (72, 215), click, "ICSTSuperCool"): Click to edit the subject of the email. The page after this interaction remains unchanged with the ability to edit the subject line directly from the subject field.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, "ICSTSuperCool"): Click to send the email. After clicking, the new page displays inbox entries with options to view or search emails. There's also a lower navbar providing quick access to folders and account settings, enhancing usability and navigation.
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/imageview_delete, (272, 28), click, "Delete"): Swipe to right. from:[0, 80] to:[320, 144] to delete the list. Swiping on this control navigates to a new page with updated recipient address from 'ICSTSuperCool' to 'autotm123@hotmail.com', reflecting changes in the Email entry.
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/bubble_item, (72, 89), click, "autotm1234@gmail.com"): Click to reveal detailed contact information or related actions. Clicking on this control displays an email popup with id "park.outlook.sign.in.client:id/email_popup" showing "autotm1234@gmail.com".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (108, 95), click, "autotm1234@gmail.com"): Click to select the email. Swiping on this control does not navigate to a new page, but a popupMenu which includes the email address appears. the new popup has a email address with id "park.outlook.sign.in.client:id/email_popup".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (16, 125), click, NULL): Clicking the control updates recipient field. Swiping on this control does not navigate to a new page, but introduces an option to add recipients from contacts, indicated by the appearance of an 'Add from contacts' button with id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.TextView, , (16, 162), click, "Cc/Bcc"): Click to add or modify the carbon copy (Cc) or blind carbon copy (Bcc) recipients for the email. After clicking, new input fields for Cc and Bcc appear, allowing more recipients to be specified directly from the contacts with the use of an added icon (id: "park.outlook.sign.in.client:id/users_icon") for each field.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (16, 125), click, "​"): The click on this control edits the main recipient address. Swiping does not navigate to a new page, but allows adding a Cc field with a button to add more from contacts with id "park.outlook.sign.in.client:id/users_icon" and a Bcc field.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 207), click, NULL): Clicking on this control does not navigate to a new page, but allows editing of the email subject. The subject field with id "park.outlook.sign.in.client:id/subject" becomes active for text input.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), click, "ICSTSuperCool"): Click to edit the subject line of the email. Clicking on this control does not navigate to a new page, but allows text editing in the same field with id "park.outlook.sign.in.client:id/subject".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 207), click, NULL): Click to attach file. This action navigates to the attachments page, displaying options including 'Image or video', 'Take photo', and 'File'.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 264), click, "\n\n--\nSent from Outlook Email App for Android"): Click to edit the email body. The page after clicking this control does not navigate to a new page, but enables text input for composing the email content. A new widget for opening the emoji keyboard appears with id "park.outlook.sign.in.client:id/toggle_btn".

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 264), click, NULL): Click to focus on the email body input field.
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 264), input, "ICSTSuperCoolBody"): Input the body 'ICSTSuperCoolBody' into the 'Message text' field.
~~~
Certainly! Based on the given actions, here's how you can convert the semantic descriptions into UIAutomator2 code in Python. I have considered the use of coordinates and IDs appropriately as instructed.

### Generated UIAutomator2 code:

···
d.click(16, 264)
d(resourceId="park.outlook.sign.in.client:id/mailbox_create_new_body").send_keys("ICSTSuperCoolBody")
···

In this provided code:
- The first line clicks on the specified coordinates (16, 264) to set focus on the email body input field.
- The second line inputs the string "ICSTSuperCoolBody" into the focused field using its unique resource ID.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (4, 36), click, NULL): Click to close the editor. Clicking on this control triggers a confirmation dialog asking 'Do you want to save to Drafts?' with options 'No' and 'Yes' having respective ids 'android:id/button2' and 'android:id/button1'.
ACTION (android.widget.TextView, autotm123@hotmail.com, (72, 38), click, "autotm123@hotmail.com"): Click to open the detailed profile or settings associated with the email 'autotm123@hotmail.com'. There are no subsequent navigational changes or new widgets introduced on the resulting page that differ from the current page setup.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, NULL): Click to send the email. The subsequent page shows an 'All Inbox' filter option and a search feature, indicating successful submission and redirection to the inbox.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/toggle_btn, (274, 550), click, NULL): Click to open the emoji and stickers panel. After clicking this control, emoji and stickers options become visible with respective buttons for smiles, stickers, and close options appearing. These new elements include 'Open emoji tab' and 'Open stickers tab' with respective IDs 'park.outlook.sign.in.client:id/panel_btn_smiles' and 'park.outlook.sign.in.client:id/panel_btn_stickers'.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/bubble_item, (72, 89), click, "autotm1234@gmail.com"): Click to edit recipient list. Clicking on this control brings up the option to modify 'To' field recipient. The new page retains prior elements with the addition of an icon for adding users from contacts with id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/bubble_item, (72, 89), click, NULL): Click to select the email address. Selected email is 'autotm1234@gmail.com'. This control does not navigate to a new page, but selects the email and shows further options like adding from contacts.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/text, (108, 95), click, "autotm1234@gmail.com"): Click to select the recipient email. Clicking on this control brings up a recipient selection or detail view. The new view includes an edit field with id "park.outlook.sign.in.client:id/edit" and a users icon with id "park.outlook.sign.in.client:id/users_icon".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (16, 125), click, NULL): Swiping on this control does not navigate to a new page, but a dialog/popupMenu which includes edit and delete item appears. the new dialog has a edit button with id "park.outlook.sign.in.client:id/users_icon" and a delete item component with id "autotm.test:id/delete_item".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/edit, (72, 169), click, "​"): Click to add or edit Cc/Bcc emails. This action reveals the 'Cc' and 'Bcc' fields for input and displays an icon to add carbon copy from contacts, making the 'Cc' and 'Bcc' editable directly on the page.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 207), click, "ICSTSuperCool"): Click to focus on the subject input field. Clicking on this control does not navigate to a new page, but allows editing the email's subject directly from the "Subject" field with id "park.outlook.sign.in.client:id/subject".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), click, "ICSTSuperCool"): Click to edit the subject of the email. Swiping on this control does not navigate to a new page, but enables editing of the email subject directly on the current page. The subject editText field reads "ICSTSuperCool".
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/add_attach_btn, (270, 207), click, NULL): Click to attach a file. This action does not navigate to a new page, instead, it provides options including 'Image or video', 'Take photo', 'File' on the same page.
ACTION (android.widget.EditText, park.outoutlook.sign.in.client:id/mailbox_create_new_body, (16, 264), click, "ICSTSuperCoolBody"): Clicking on this text field allows the user to edit the body of a new email, retaining the entered text 'ICSTSuperCoolBody' across page changes.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, NULL): Click to send the email.
~~~
···
d.click(268, 28)
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.LinearLayout, park.outlook.sign.in.client:id/filter_tap_area, (16, 40), click, NULL): Click to open filter options. Clicking on this control opens a list view with filter options such as 'All', 'Unread', and 'Flagged'.
ACTION (android.widget.Spinner, park.outlook.sign.in.client:id/spinner, (16, 40), click, NULL): Click to expand spinner options. After clicking this widget, a dropdown ListView appears with items for 'All', 'Unread', and 'Flagged' which allows filtering the email list based on these conditions.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folder_name, (16, 40), click, "Inbox"): Click to filter the inbox. The page after clicking this control shows a list of filter options including 'All', 'Unread', and 'Flagged'.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/search_tap_area, (106, 32), click, NULL): Clicking on the search area transitions to the search page with editable search text field ('park.outlook.sign.in.client:id/search_text') and cancel button ('park.outlook.sign.in.client:id/toolbar_action_cancel'). Tabs for filtering search ('all', 'from', 'to', 'subject') become available along with an advanced search option.
ACTION (android.widget.Button, park.outlook.sign.in.client:id/icon_search, (274, 32), click, NULL): Click to search mails. After clicking, a search text field with id "park.outlook.sign.in.client:id/search_text" and a cancel button with id "park.outlook.sign.in.client:id/toolbar_action_cancel" appear on the screen.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/front_layout, (0, 81), click, NULL): Click to navigate to the detailed view of an email. It reveals detailed header 'From: tm auto', subject 'Another rabbit hole', timestamp 'August 8, 2024, 19:42', and options like 'Mark as read', 'Flag', and other sender-related details. This navigation changes to a detailed view with action buttons such as 'Move to Folder', 'Mark as Spam', 'Delete', 'More options' and functionalities like 'Reply or Forward'.
ACTION (android.widget.ImageView, park.outlook.sign.in.client:id/checkbox, (16, 181), click, NULL): Clicking on this control does not navigate to a new page, but a popupMenu which includes edit and delete item appears. the new dialog has a edit button with id "park.outlook.sign.in.client:id/snackbar_action" and a delete item component with id "park.outlook.sign.in.client:id/snackbar_text".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/sender, (88, 176), click, NULL): Open detailed view of the email titled 'Another rabbit hole'. This action displays detailed information about the email with the subject "Automated Software Engineering", including options to reply, forward, mark as read, and deal with other recipients.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/date, (251, 178), click, "8 Aug"): Clicking shows detailed email content and actions related to this email. The next page includes options for managing the email such as 'Mark as read' with id "park.outlook.sign.in.client:id/mailbox_mailmessage_content_readed", and information tiles like 'Automated Software Engineering' subject with id "park.outlook.sign.in.client:id/mailbox_mailmessage_content_theme".
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), click, "ICSTSuperCool"): Click on the subject field to enter the subject for an email. Navigating to the message content creation page, displaying the full details of an email, with interactive controls like "Mark as read," "Flag," and functionalities such as "Mark as Spam" and "Delete".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snippet, (88, 220), click, "Another rabbit hole"): Click to view details of the email. The page after clicking this control shows the full email content, with actions such as reply or forward (ID: park.outlook.sign.in.client:id/fab_expand_menu_button), mark as read (ID: park.outlook.sign.in.client:id/mailbox_mailmessage_content_readed), and options to move, mark as spam, or delete the email presented at the top toolbar.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/center_title, (48, 359), click, "No connection"): Click to reconnect. Clicking on this control displays a retry button with id "park.outlook.sign.in.client:id/repeat".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/repeat, (249, 350), click, NULL): Click to retry the action due to 'No connection'. After clicking, the page navigates or updates with various controls such as 'Reply or Forward' options, message content viewing, and options for marking as read, flagging, or performing other email actions.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_left, (0, 592), click, NULL): Click to navigate to the folders view. After clicking, folders such as Drafts, 存档 (Archive), Outbox, Spam, Inbox, and Sent are displayed, each with their respective text identifiers (e.g., "Drafts", "存档", "Outbox", "Spam", "Inbox", "1", "Sent").
ACTION (android.widget.RelativeLayout, park.outlook.sign.in.client:id/folders_text, (0, 595), click, "Folders"): Click to navigate to folders page. The page after clicking this control shows various folders like Drafts, 存档(Archive), Outbox, Spam, Inbox, and Sent with their respective unique ids and texts.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/folders_text, (0, 623), click, NULL): Click to navigate to the folder selection view. Swiping on this control navigates to a new page showing various folder options including 'Drafts', '存档', 'Outbox', 'Spam', 'Inbox', and 'Sent'. Each folder can be accessed by their clickable area in the new UI layout.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_right, (204, 592), click, "Account"): Clicking on the Account button does not navigate to a new page, but triggers user account options which might include settings or account information. This is an important widget for user account management.
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/account_text, (262, 623), click, NULL): Click to navigate to the account settings page. The page includes options such as adding a new account, managing current accounts, and accessing account settings like "Personal Data" and "Application" settings.
ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Clicking on this control switches the view to the email composing page. The next page includes various editable fields such as "To", "Cc/Bcc", "Subject", and "Body" with corresponding control capabilities for text input and other functionalities like attaching files.
ACTION (android.widget.ImageButton, park.outlook.sign.in.client:id/fab, (136, 585), click, NULL): Click to open list of actions. No navigation happens, still on the mailbox creation page but it enables mbox options like "Folders" with id "park.outlook.sign.in.client:id/folders_text", and "Account" with id "park.outlook.sign.in.client:id/account_text".
ACTION (android.widget.TextView, park.outlook.sign.in.client:id/snackbar_text, (12, 537), click, "Sending... (+4 waiting)"): Click to modify the sending process. Clicking on this control results in the status update to "Sending... (+2 waiting)" indicating continued email sending operation. The widget id of action button is "park.outlook.sign.in.client:id/snackbar_action".
ACTION (android.widget.Button, park.outoutlook.sign.in.client:id/snackbar_action, (236, 529), click, "Edit"): Clicking on this button allows editing of the awaiting emails, changing the status from 'Sending... (+4 waiting)'. On next page, elements to compose and send email are reloaded, ensuring continuity in editing the email draft.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), wait_until_text_presence, "Sent"): Verify that the 'Sent' message is present within 20 seconds.
DONE
~~~
···
assert d(text="Sent").wait(20)
···
````
### Success
````
ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/folder_name, (16, 40), wait_until_text_presence, "Inbox"): Verify that the 'Inbox' text is present within 15 seconds., Exec_Success

ACTION (android.widget.FrameLayout, park.outlook.sign.in.client:id/bottom_bar_middle, (112, 573), click, NULL): Click to open email composition interface., Exec_Success

ASSERT (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), wait_until_element_presence, "park.outoutlook.sign.in.client:id/edit") : Verify that the 'To' field is present within 15 seconds., Exec_Success
ACTION (android.widget.TextView, park.outoutlook.sign.in.client:id/edit, (72, 88), click, NULL): Click to focus on the recipient input field., Exec_Success
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/edit, (72, 88), input, "autotm1234@gmail.com"): Input the recipient email 'autotm1234@gmail.com' into the 'To' field., Exec_Success

ACTION (android.widget.TextView, park.outlook.sign.in.client:id/subject_label, (16, 171), click, NULL):purpose, Exec_Success

ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), click, NULL): Click to focus on the subject input field., Exec_Success

ACTION (android.widget.EditText, park.outlook.sign.in.client:id/subject, (72, 215), input, "ICSTSuperCool"): Input the subject 'ICSTSuperCool' into the 'Subject' field., Exec_Success

ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 264), click, NULL): Click to focus on the email body input field., Exec_Success
ACTION (android.widget.EditText, park.outlook.sign.in.client:id/mailbox_create_new_body, (16, 264), input, "ICSTSuperCoolBody"): Input the body 'ICSTSuperCoolBody' into the 'Message text' field., Exec_Success

ACTION (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), click, NULL): Click to send the email., Exec_Success

ASSERT (android.widget.TextView, park.outlook.sign.in.client:id/toolbar_action_send, (268, 28), wait_until_text_presence, "Sent"): Verify that the 'Sent' message is present within 20 seconds., Exec_Success
DONE
````

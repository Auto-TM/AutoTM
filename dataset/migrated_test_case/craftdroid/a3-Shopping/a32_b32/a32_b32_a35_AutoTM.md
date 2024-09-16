## a32's b32 to a35

### Semantics of Source Test case
> This test case is testing the login functionality of the application, ensuring the correct input of email and password, successful login, and verification of the user's profile name.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ASSERT (EditText, com.contextlogic.wish:id/sign_in_fragment_password_text, (), wait_until_element_presence, "id:sign_in_fragment_password_text") : Verify that the password field is present within 15 seconds.
> 2. ACTION (EditText, com.contextlogic.wish:id/sign_in_fragment_password_text, (), input, "1qaz2wsX") : Input the password '1qaz2wsX' into the password field.
> 3. ACTION (EditText, com.contextlogic.wish:id/sign_in_fragment_email_text, (), input, "uci.seal@gmail.com") : Input the email 'uci.seal@gmail.com' into the email field and hide the keyboard.
> 4. ACTION (TextView, com.contextlogic.wish:id/sign_in_fragment_sign_in_button, (), click, NULL) : Click on the 'Sign In' button to submit the login credentials.
> 5. ASSERT (ImageButton, , (), wait_until_element_presence, "xpath://*[@content-desc=\"Open Menu\"]") : Verify that the 'Open Menu' button is present within 10 seconds after login.
> 6. ACTION (ImageButton, , (), click, NULL) : Click on the 'Open Menu' button to open the user menu.
> 7. ASSERT (TextView, com.contextlogic.wish:id/menu_profile_name, (), wait_until_text_presence, "text:Sealbot") : Verify that the user's profile name 'Sealbot' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): The "Navigate up" control triggers the back function of the application, taking the user back to the previous screen or state of the application. This action does not navigate to a new page but updates the content of the current page according to the selected category from the "Nearby" list in the Yelp app.
ACTION (android.support.v7.widget.RecyclerView, com.yelp.android:id/recycler_view, (0, 80), click, NULL): Click on the 'RecyclerView' at Yelp home page to navigate between categories or view details of a 'Category'. The page remains the same but the contents of the 'RecyclerView' might change based on interaction.
ACTION (android.view.ViewGroup, com.yelp.android:id/category_suggestion, (16, 152), click, "Restaurants"): The user clicks on the "Restaurants" category to browse the restaurants nearby. After this action, the screen navigates to the restaurant listing page where the user can see details such as distance, category, and address of various restaurants.
ACTION (android.widget.TextView, com.yelp.android:id/title, (232, 297), click, "More"): Click to navigate to the category selection. After clicking, a new list of categories appears, including the options "Pizza", "Breakfast", "Chinese", "Burgers" and others for finer category selection in the restaurant search results.
ACTION (android.widget.TextView, com.yelp.android:id/title, (16, 216), click, "Restaurants"): Click on 'Restaurants' to navigate to the 'Reservations Current Location' page which provides details of the reservations available around the current location. The new page contains various controls and information such as a 'Filter' button with id "com.yelp.android:id/toolbar_search_filter", a 'Map' control with id "com.yelp.android:id/toggle", and a list of available reservations with id "android:id/list".
ACTION (android.view.ViewGroup, com.yelp.android:id/category_suggestion, (16, 152), click, NULL): Click to choose a category. Selecting this control filters the business listings on the next page by the chosen category, for example, "Takeout".
ACTION (android.widget.TextView, com.yelp.android:id/title, (16, 297), click, "Movers"): Navigates to the page with the list of 'Movers' in the current location. The next page includes a list of movers with their details such as reviews, address, and other related information. The page also includes search filter options for the user to narrow down their search.
ACTION (android.view.ViewGroup, com.yelp.android:id/category_suggestion, (16, 152), click, "Home Cleaners"): Click to select the 'Home Cleaners' category. The subsequent page displays a list of relevant businesses, with options to filter results, view on map, and request quotes directly from providers.
ACTION (android.widget.TextView, com.yelp.android:id/header_text, (16, 369), click, NULL): Clicks on the 'Featured Collections' header on current page. The next page is similar to the current page, suggesting no significant changes were made due to this interaction.
ACTION (android.widget.TextView, com.yelp.android:id/header_clickable_text, (246, 371), click, "View All"): Click to navigate to the next page which displays collections. The next page contains various collections and options to sign up or log in.
ACTION (android.view.ViewGroup, com.yelp.android:id/shimmer_layout, (16, 410), click, NULL): Click to reveal the featured collections and their associated businesses count. Clicking on this control does not navigate to a new page, but may update the content dynamically within the current view to display detailed information of a selected collection.
ACTION (android.widget.TextView, com.yelp.android:id/collection_biz_count, (262, 525), click, NULL): Clicking on this element transitions to a new page showing details of a collection, including its description, last updated date, and an option to follow the collection.
ACTION (android.widget.ImageView, com.yelp.android:id/search_text_icon, (16, 88), click, NULL): Click to open search bar. The page after clicking this control is the search page, which has a search bar with id "com.yelp.android:id/searchbar".
ACTION (android.widget.EditText, com.yelp.android:id/search_text, (72, 88), click, "Cleaners, movers, delivery, sushi, etc."): User can click on this control to bring up a search menu. After clicking, a search menu appears with a search bar for "Cleaners, movers, delivery…" and location bar for "Current Location". This search interface also provides clickable search suggestions like "Home Cleaners", "Movers", "Reservations", "HVAC", "Restaurants", "Delivery", "Takeout", and "Accountants".
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_nearby, (0, 584), click, "Nearby"): Open the nearby options. The page after clicking this control presents nearby category suggestions like 'Restaurants', 'Reservations', 'Takeout', 'Auto repair' etc. It does not navigate to a new page but the widgets on the existing page become responsive based on nearby category selection.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_search, (64, 584), click, NULL): Clicking leads to the search page. The next page has search bar for searches("Cleaners, movers, delivery…") with id "com.yelp.android:id/searchbar" and also a button for current location search with id "com.yelp.android:id/locationbar". There are suggested search areas like "Home Cleaners", "Movers", "Reservations", "HVAC", "Restaurants", "Delivery", "Takeout", "Accountants", "Plumbers" in the searched list, which can be accessible by "com.yelp.android:id/term".
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_profile, (128, 584), click, NULL): Click to open the User Profile page, after clicking on this control, an user sign-in/up page appears, containing Sign-up and Log-in buttons with respective ids "com.yelp.android:id/sign_up_button" and "com.yelp.android:id/log_in_button".
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_feed, (192, 584), click, NULL): Clicking the 'Activity' tab. Leads to the 'Activity' page displaying a feed of friend activities including reviews and photos.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_collections, (256, 584), click, NULL): Navigates to the 'Collections' page that lists various featured collections, user collections, and allows creating new collections. The new page contains elements like a 'Create' button with id "com.yelp.android:id/create" and a Collection list in a RecyclerView with id "com.yelp.android:id/recycler_view".

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_profile, (128, 584), click, NULL): Click to open the User Profile page
~~~
Certainly, below is the UIAutomator2 code in Python that performs the action described. Since the instructions prefer using coordinates when they are precise, I will use the coordinates provided in the action.

### Input Action:
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_profile, (128, 584), click, NULL): Click to open the User Profile page

### Output Code:
```
d.click(128, 584)
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to navigate up. The page after clicking this control is the home page, which includes new options such as 'Sign Up', 'Log In', and 'Check In'.
```
ACTION (android.widget.Button, com.yelp.android:id/sign_up_button, (8, 399), click, "Sign Up"): Click to start the sign-up process. No new page is loaded and no new widgets are shown as a result of this action based on provided JSON data.
ACTION (android.widget.TextView, No ID, (0, 340), click, "Join the Yelp community in writing reviews, checking into local businesses, and more!"): Click to hide the popup message. Clicking on this control does not navigate to a new page but closes the popup window. This frees up the user interface for better interaction with other underlying controls.
ACTION (android.widget.Button, com.yelp.android:id/log_in_button, (8, 451), click, "Log In"): Click to navigate to the login page. The next page includes GUI elements such as Username and Password fields with ids "com.yelp.android:id/activity_login_editUsername" and "com.yelp.android:id/activity_login_editPassword", a Show Password checkbox with id "com.yelp.android:id/activity_login_unmask_password_checkbox", a Log In button with id "com.yelp.android:id/activity_login_btnLogin", buttons to Log in with Google or Facebook with ids "com.yelp.android:id/google_sign_up" and "com.yelp.android:id/fb_log_in", and a button to create a new Yelp account with id "com.yelp.android:id/activity_login_create_account_question".
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_nearby, (0, 584), click, "Nearby"): Clicking "Nearby" navigates the user away from the current page. There are no new identifiable GUI elements on the subsequent page as per the provided Next Page JSON.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_search, (64, 584), click, "Search"): clicks to initiate a Yelp business search. This opens the search settings page where users can specify search terms and location.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_profile, (128, 584), click, "Me"): This action represents clicking the "Me" button. Initiating this action does not navigate to a new page or introduce new elements. It merely changes the state of the control from "selected" to "deselected".
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_feed, (192, 584), click, "Activity"): Click to view the user activity feed. After clicking on this control, the next page featuring a detailed list of user activities with reviews and ratings appears.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_collections, (256, 584), click, "Collections"): The purpose of this action is to navigate to the collections page which hosts a variety of collections categorized based on location and content. After clicking, users can view or create collections for easy access to categories of their interest and follow collections which align with their preferences.

````

#### Selected Event(s) and Script
````
Based on the provided source test case semantics, the current page's intentions, and the executed action sequence, the next step of the test migration should be to navigate to the login page. The source test case is testing the login functionality, and the current executed action sequence shows that we have successfully opened the User Profile page. However, we need to be on the login page to continue the test case. 

The intention that matches this requirement is: 
```
ACTION (android.widget.Button, com.yelp.android:id/log_in_button, (8, 451), click, "Log In"): Click to navigate to the login page.
```
So, the next step of the test code migration should be to click the 'Log In' button to navigate to the login page. Here is the output:

~~~
ACTION (android.widget.Button, com.yelp.android:id/log_in_button, (8, 451), click, NULL): Click to navigate to the login page.
~~~
Based on the given description, the uiautomator2 code to perform click actions on the login button, using coordinates, can be written as follows:

```python
d.click(8, 451)
d.click(8, 451)
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, com.yelp.android:id/terms_of_service_text, (16, 124), click, NULL): Tapping this control does not navigate to a new page, but likely opens up Yelp's Terms of Service document for the user to read.
ACTION (android.widget.EditText, com.yelp.android:id/activity_login_editUsername, (16, 178), click, "Email"): Interacting with this element allows for input of a user's email as part of the login process. Swiping or other interactions are not indicated as no change in page state is detected between Current Page JSON and Next Page JSON.
ACTION (android.widget.EditText, com.yelp.android:id/activity_login_editPassword, (16, 240), click, "Password"): Interaction with the password field allows for inputting password credentials to proceed with login. There is no change in the page's elements post-interaction, indicating the field only serves as data entry without triggering navigation or any other actions.
ACTION (android.widget.CheckBox, com.yelp.android:id/activity_login_unmask_password_checkbox, (16, 305), click, "Show password"): Clicking on this checkbox does not navigate to a new page, but allows the user to toggle the visibility of the password they are inputting. No additional widgets appear or disappear as a result of this action.
ACTION (android.widget.Button, com.yelp.android:id/activity_login_btnLogin, (222, 295), click, "Log In"): Click to attempt login. An alert dialog is shown, asking for email address confirmation. It includes an 'OK' button with id "android:id/button3".
ACTION (android.widget.Button, com.yelp.android:id/google_sign_up, (16, 382), click, "Log in with Google"): Click to log in using Google. After clicking, it navigates away from the current page to external Google login, leaving no elements on the current page.
ACTION (android.widget.Button, com.yelp.android:id/fb_log_in, (16, 440), click, "Log in with Facebook"): Click to log in with Facebook. The page after clicking this control proceeds to load, as indicated by the presence of a loading message with id "android:id/message".
ACTION (android.widget.TextView, com.yelp.android:id/activity_login_create_account_question, (16, 506), click, "Don't have a Yelp account yet? Sign up."): Clicking prompts no visible change, indicating either a validation step without navigation or a lack of response due to conditions not met.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.EditText, com.yelp.android:id/activity_login_editUsername, (16, 178), wait_until_element_presence, "id:activity_login_editUsername"): Verify that the email field is present.
ACTION (android.widget.EditText, com.yelp.android:id/activity_login_editUsername, (16, 178), input, "uci.seal@gmail.com"): Input the email 'uci.seal@gmail.com' into the email field.
ASSERT (android.widget.EditText, com.yelp.android:id/activity_login_editPassword, (16, 240), wait_until_element_presence, "id:activity_login_editPassword"): Verify that the password field is present.
ACTION (android.widget.EditText, com.yelp.android:id/activity_login_editPassword, (16, 240), input, "1qaz2wsX"): Input the password '1qaz2wsX' into the password field.
ACTION (android.widget.Button, com.yelp.android:id/activity_login_btnLogin, (222, 295), click, NULL): Click on the 'Log In' button to submit the login credentials.
~~~
### Output(The code should be wrapped using '···'):

```python
import time
assert d(resourceId="com.yelp.android:id/activity_login_editUsername").wait(timeout=10)
d(resourceId="com.yelp.android:id/activity_login_editUsername").set_text("uci.seal@gmail.com")
assert d(resourceId="com.yelp.android:id/activity_login_editPassword").wait(timeout=10)
d(resourceId="com.yelp.android:id/activity_login_editPassword").set_text("1qaz2wsX")
d(resourceId="com.yelp.android:id/activity_login_btnLogin").click()
```

Please note that the 'wait_until_element_presence' action was interpreted as a call to the wait() function in uiautomator, which waits until the specified UI element appears or the timeout expires. 'Timeout' parameter was set to 10 seconds, but it can be adjusted according to the app's actual circumstances.
````
#### Contextual Semantics of Widgets
````
ACTION (android.support.v7.widget.RecyclerView, com.yelp.android:id/recycler_view, (0, 24), click, NULL): Clicking on this control navigates to the user profile page where user details and options like 'Write a Review', 'Add Photo', 'Check-In' and various other user activities and statistics are shown. The page also provides a navigation bar at the bottom.
ACTION (android.widget.ImageView, com.yelp.android:id/user_profile_image, (12, 92), click, NULL): User profile image clicked. No significant change detected between the current and next page JSON data after the action, suggesting the click may open an off-screen dialog, initiate an in-place data refresh, or be non-functional in the current context.
ACTION (android.widget.TextView, com.yelp.android:id/user_profile_name, (124, 107), click, "Sealbot L."): Click to view user profile details. Swiping on this control does not navigate to a new page, but the user profile details remain visible with components such as profile image, user location, friend count, review count, and photo count being displayed.
ACTION (android.widget.TextView, com.yelp.android:id/user_profile_location, (124, 134), click, "Mountain View, CA"): Clicking on this control navigates to a new page with the same set of elements, indicating either a refresh or no change in the context of user profile information display.
ACTION (android.widget.TextView, com.yelp.android:id/user_profile_friend_count, NULL, click, "0"): Click on the friend count triggers the display of the user's friends list. No new widget appears but the user is taken to a list showing all friends, or a message indicating no friends if the count is zero.
ACTION (android.widget.TextView, com.yelp.android:id/user_profile_review_count, (149, 155), click, NULL): Clicking this control transitions from the profile view to a view displaying user's Yelp reviews. The next page presents the user's review statistics under the descriptor 'Views' with id "com.yelp.android:id/title".
ACTION (android.widget.TextView, com.yelp.android:id/user_profile_photo_count, (174, 155), click, "0"): The clickable interaction leads to no change in the page. There's no page or widget change after the action on this element.
ACTION (android.widget.LinearLayout, com.yelp.android:id/add_review_ctb_bar, (0, 205), click, "Write a Review"): Clicking navigates to the add review page with a search bar (com.yelp.android:id/search_holder) and listed nearby businesses like "Wemorph" with the address "904 Industrial Ave, Palo Alto".
ACTION (android.widget.TextView, com.yelp.android:id/label, (14, 239), click, "Write a Review"): Initiates the 'Write a Review' process for the user. On click, it leads to a new page where the user can search for businesses to review. This page contains an option to search businesses with identifier "com.yelp.android:id/search_text".
ACTION (android.widget.LinearLayout, com.yelp.android:id/add_photo_ctb_bar, [106, 205], click, NULL): Tap to add photos or videos. Tapping on this control navigates to a new page with a ListView for selecting pictures, indicated by the id "android:id/list", and the header title "Add Photo or Video".
ACTION (android.widget.LinearLayout, com.yelp.android:id/check_in_ctb_bar, (213, 205), click, NULL): Opens a page for users to check-in at different businesses. The next page has a list of business options to check in, each represented by elements with id "com.yelp.android:id/term". The user can also search for a specific business using the search bar with id "com.yelp.android:id/search_text".
ACTION (android.widget.TextView, com.yelp.android:id/label, (130, 239), click, "Add Photo"): A click on this control opens a page where you can add a photo to your Yelp account. The next page contains a ListView with clickable items such as Zareen's, Google Visitor Experience Cafe, and Starbucks, indicating places where you might check in or have visited.
ACTION (android.widget.FrameLayout, com.yelp.android:id/contribution_award_type_component_item, (0, 273), click, NULL): Opens the notifications page. The notifications page lists all user notifications.
ACTION (android.widget.TextView, com.yelp.android:id/contribution_text, (8, 288), click, "All Notifications"): The click action on this element leads to the notifications page which contains various notifications associated with the user's Yelp account. This is evidenced by the modifications in the Next Page JSON which shows the presence of a ListView with id "android:id/list" containing several notification items.
ACTION (android.widget.TextView, com.yelp.android:id/contribution_badge, (154, 291), click, "1"): Click to navigate to notification page. The page after clicking on this control shows all notifications.
ACTION (android.widget.TextView, com.yelp.android:id/contribution_text, (8, 288), click, "All Notifications "): Opens the Messages page. The page after clicking this control includes the feature "Compose New Message" with id "com.yelp.android:id/compose_message".
ACTION (android.widget.TextView, com.yelp.android:id/header_text, (0, 381), click, "My Impact"): Click to view personal impact. Clicking on this control doesn't navigate to a new page but may reveal details about user contributions and their effects within the same screen.
ACTION (android.widget.TextView, , (92, 396), click, "New"): Clicking on this control does not navigate to a new page, but the same elements are present with no significant change detected from the current page to the next page.
ACTION (android.support.v7.app.a, Reviews, (20, 454), click, "Reviews"): Click on 'Reviews' to show Reviews page. The next page contains information about the user profile, user activities, and control menus to go to other options such as 'Nearby', 'Search', 'Me', 'Activity', and 'Collections'.
ACTION (android.widget.TextView, Photos, (90, 454), click, "Photos"): Navigate to Photo gallery. The 'Photos' control, when clicked, selects the corresponding page in the ViewPager, displaying user's photos and likes associated with the account.
ACTION (android.support.v4.view.ViewPager, com.yelp.android:id/view_pager, (0, 488), click, NULL): Clicking this control doesn't navigate to a new page but allows the user to scroll through the impact details such as Reactions and Views for different periods (All Time, Last 90 Days).
ACTION (android.widget.TextView, com.yelp.android:id/title, (16, 512), click, "Reactions"): Clicking on this control does not navigate to a new page, but likely updates the user interaction count related to "Reactions", possibly refreshing or presenting new information related to user's contributions or interactions within the app.
ACTION (android.widget.TextView, com.yelp.android:id/display_value, (16, 529), click, "0"): Click to view details of user reactions. This interaction does not navigate to a new page but may expand to show more information about the reactions within the same view context.
ACTION (android.widget.TextView, com.yelp.android:id/caption, NULL, click, NULL): Click to view 'all time' statistics. This action does not change pages or reveal new widgets, but could refresh or update existing elements with new data.
ACTION (android.widget.ImageButton, , (0, 24), click, NULL): Navigates to the previous page, identified by the 'Navigate up' descriptor and potentially a matching icon asset. The previous page shows a list of menu options, including 'Add Review,' 'Add a Photo or Video,' and 'Check In', alongside other navigation items.
ACTION (android.widget.TextView, Sealbot L., (124, 107), click, NULL): By clicking this control, it gives access to the user's Yelp profile. This does not navigate to a new page but allows the user to scroll through their profile details, including their number of reviews and photos, as well as options to write a review, add a photo, and check in. The user can also view their notifications and messages. At the top of the page, there are options to navigate up or access more options. At the bottom, there are navigation options for Nearby, Search, Me, Activity, and Collections.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to open more options. The next popup-menu appears with the option to 'Find Friends' with id "com.yelp.android:id/title".
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_nearby, (0, 584), click, "Nearby"): Click to navigate to the nearby places page. No new widgets appear, and it seems the next page JSON is empty, which suggests there might have been an issue with loading the page or capturing the page data after the interaction.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_search, (64, 584), click, "Search"): After clicking on the 'Search' button, it navigates to a new search page with an editable textbox with the id 'com.yelp.android:id/searchbar' for typing a search query and another editable textbox with the id 'com.yelp.android:id/locationbar' for specifying the location. On this search page, there are several predefined searchable items listed like 'Home Cleaners', 'Movers', 'Reservations', 'Restaurants', 'Delivery', 'Takeout', 'Accountants', 'Plumbers', and 'Auto Repair'.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_profile, (128, 584), click, "Me"): Clicking on this control navigates to the user's profile page, which displays detailed user information, user's contributions like reviews, photos, and an interface to start writing a review, add a photo, or check in.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_feed, (192, 584), click, NULL): Clicking navigates to the Activity tab where the user can view their feed. The feed contains a list of activities such as notifications and actions performed by friends or nearby users.
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_collections, (256, 584), click, "Collections"): Click to navigate to the Collections page, showcasing various collections including "Featured in Mountain View, CA" and "My Collections" sections with interactive elements for creating and viewing collections.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.widget.TextView, com.yelp.android:id/user_profile_name, (124, 107), click, "Sealbot L."): Click to view user profile details. Swiping on this control does not navigate to a new page, but the user profile details remain visible with components such as profile image, user location, friend count, review count, and photo count being displayed.
DONE
~~~
For the given actions, we can generate the following UIAutomator2 code in Python.

### Output (UIAutomator2 Code in Python):

```python
# Checking if the 'Sealbot' text is present
assert (d.click(124, 107).exists(timeout=10))
``` 
````
### Success
````
ACTION (android.widget.TextView, com.yelp.android:id/hot_button_profile, (128, 584), click, NULL): Click to open the User Profile page, Exec_Success

ACTION (android.widget.Button, com.yelp.android:id/log_in_button, (8, 451), click, "Log In"): Click to navigate to the login page., Exec_Success

ASSERT (android.widget.EditText, com.yelp.android:id/activity_login_editUsername, (16, 178), wait_until_element_presence, "id:activity_login_editUsername"): Verify that the email field is present., Exec_Success
ACTION (android.widget.EditText, com.yelp.android:id/activity_login_editUsername, (16, 178), input, "uci.seal@gmail.com"): Input the email 'uci.seal@gmail.com' into the email field., Exec_Success
ASSERT (android.widget.EditText, com.yelp.android:id/activity_login_editPassword, (16, 240), wait_until_element_presence, "id:activity_login_editPassword"): Verify that the password field is present., Exec_Success
ACTION (android.widget.EditText, com.yelp.android:id/activity_login_editPassword, (16, 240), input, "1qaz2wsX"): Input the password '1qaz2wsX' into the password field., Exec_Success
ACTION (android.widget.Button, com.yelp.android:id/activity_login_btnLogin, (222, 295), click, NULL): Click on the 'Log In' button to submit the login credentials., Exec_Success

ASSERT (android.widget.TextView, com.yelp.android:id/user_profile_name, (124, 107), click, "Sealbot L."): Click to view user profile details. Swiping on this control does not navigate to a new page, but the user profile details remain visible with components such as profile image, user location, friend count, review count, and photo count being displayed., Exec_Success
DONE
````

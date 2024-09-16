## a14's b12 to a12

### Semantics of Source Test case
> This test case is testing the functionality of navigating to different websites and verifying the presence of specific elements, as well as the back button functionality.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (ImageButton, de.baumann.browser:id/floatButton_ok, (), click, NULL) : Click on the floating button to initiate a new action.
> 2. ACTION (EditText, de.baumann.browser:id/main_omnibox_input, (), click, NULL) : Click on the omnibox input field to activate it for text input.
> 3. ACTION (EditText, de.baumann.browser:id/main_omnibox_input, (), input, "https://www.ics.uci.edu") : Input the URL 'https://www.ics.uci.edu' into the omnibox input field and press enter.
> 4. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
> 5. ACTION (EditText, de.baumann.browser:id/main_omnibox_input, (), input, "https://uci.edu") : Input the URL 'https://uci.edu' into the omnibox input field and press enter.
> 6. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc="UCI homepage"]") : Verify that the element with the content description 'UCI homepage' is present within 10 seconds.
> 7. RETURN: Press the back button to return to the previous page.
> 8. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.FrameLayout, com.android.browser:id/iconcombo, (8, 24), click, NULL): Click to view page info. The page after clicking this control is the Page info dialog, which reveals information such as the site's title and address and provides options to view certificate or acknowledge with OK.

ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), click, NULL): Click to refresh the page or type a new URL. The next page includes elements for refreshing the page, starting a voice search, and various Google services.
ACTION (android.widget.ImageButton, com.android.browser:id/tab_switcher, (272, 24), click, NULL): Click to manage open pages. The page after clicking this control is the tab management page, which has controls for refreshing page, voice searching, opening new tabs, and accessing bookmarks.
ACTION (android.webkit.WebView, Google, (0, 76), scroll, NULL): Scroll to view various Google products and services. After this action, the page navigates to "Browse all of Google's products and services" where different Google products can be seen.
ACTION (android.view.View, ?client=ms-android-google&sca_esv=ce82090d53e0c143&source=android-home, (0, 76), click, NULL): Click to navigate to the Google products and services page. The page after clicking this control contains helpful products and Google services, along with a navigation drawer and product support details.
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), click, NULL): Click to input new URL. The page after clicking this control is a new webpage, which displays the information from the newly entered URL.
ACTION (android.view.View, N/A, (99, 76), click, NULL): Clicking to navigate to the Images section of Google. The subsequent page is the Google Images page where users can search for images.
ACTION (android.view.View, Sign in, (234, 87), click, NULL): Click to sign into Google account. The next page prompts for user credentials to log into a Google account.
ACTION (android.widget.Image, googlelogo_tablet_tier1_hp_color_183x64dp, (68, 156), click, NULL): Clicking to refresh or visit the homepage. The page after this action will be the Google homepage.
ACTION (android.view.View, NULL, (102, 632), click, NULL): Click to access the Privacy Policy Page. After clicking this control, the page navigates to the privacy policy of the site, where you can explore the details of the policy and the various information provided within.
ACTION (android.view.View, Terms, (180, 632), click, NULL): Click to view the Terms of Service of Google. The subsequent page would contain the detailed Terms of Service for Google.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), click, NULL): Click to activate the URL input field for text input.
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the URL input field and press enter.
~~~
Based on the provided input, here is the corresponding UIAutomator2 code in Python:

```python
d(resourceId="com.android.browser:id/url").click()
d(resourceId="com.android.browser:id/url").send_keys("https://www.ics.uci.edu")
d.press('enter')
```
The first line of code activates the URL input field for text input by clicking on it. The second line inputs the URL 'https://www.ics.uci.edu' into the URL input field. The third line simulates pressing the 'enter' key.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.FrameLayout, com.android.browser:id/iconcombo, (9, 24), click, NULL): Click to view page details. The subsequent page after this interaction shows detailed information about the current webpage such as title and URL, and also provides functions like viewing the page's certificate.
ACTION (android.widget.EditText, com.android.browser:id/url, (53, 24), click, NULL): The user clicks this Widget to input a new URL or change the existing one. On the next page, this triggers a change in state where the interface shows controls "refresh page" and "start voice search" to provide the user with flexibility in how to navigate.
ACTION (android.widget.ImageButton, com.android.browser:id/tab_switcher, (272, 24), click, NULL): The tab switcher button when clicked opens the tab management page which allows navigation between open tabs, closing existing tabs, or creating new tabs.
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 76), scroll, NULL): Scroll to configure the website options of the UC Irvine Donald Bren School of Information & Computer Sciences home page. The next page remains the home page, with available options like Accessibility Tools, Toggle site search form & navigation, and sections related to Accessing STEM in Higher Education.
ACTION (android.widget.Button, Accessibility Tools, (268, 126), click, NULL): Click to open the Accessibility Tools section. There is no change in the page after the interaction, indicating the button might not be functioning correctly.
ACTION (android.view.View, UCI ICS logo, (16, 97), click, NULL): Click to navigate to the UCI ICS homepage. The page after clicking this control stays the same because the UCI ICS logo on the homepage is generally used as a home shortcut.
ACTION (android.widget.Spinner, Toggle site search form & navigation, (264, 84), click, NULL): Clicks to toggle the site search form and navigation. The page after clicking this control is the home page with expanded search form and navigation.
ACTION (android.view.View, NULL, (16, 312), click, NULL): Click to access the "Accessing STEM in Higher Education" section. The next page after interaction remains the same, suggesting that the interaction results in some in-place change or the loaded content is identical.
ACTION (android.view.View, NULL, (16, 451), click, NULL): Click to learn more about high school students who are blind or low vision visiting ICS & learning about college life. After this view is clicked, the next page remains consistent with the current page as per the Next Page JSON, suggesting either more information has been loaded on the same page or perhaps a modal with details has been opened.
ACTION (android.view.View, NULL, (16, 619), click, NULL): Click to read more about "Accessing STEM in Higher Education". Upon clicking, you are redirected to a detailed page about the topic with extra sharing functionalities and further navigation controls.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 140), click, NULL): Click to view the portrait image related to the AccessSTEM program. The page after clicking this control remains the same and retains the same set of clickable elements.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 76), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
ACTION (android.widget.EditText, com.android.browser:id/url, (53, 24), click, NULL): Click to activate the URL input field for text input.
ACTION (android.widget.EditText, com.android.browser:id/url, (53, 24), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the URL input field and press enter.
~~~
The following is the conversion of the test semantic descriptions into UIAutomator2 code in Python.

```python
# Assertion
assert d(description="Donald Bren School of Information and Computer Sciences", className="android.webkit.WebView").wait(timeout=10)

# Actions
d(resourceId="com.android.browser:id/url", className="android.widget.EditText").click()
d(resourceId="com.android.browser:id/url", className="android.widget.EditText").set_text("https://uci.edu")
d.press('enter')
```
The above code first asserts that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds. Then it clicks the URL input field to activate it for text input. After that, it inputs the URL 'https://uci.edu' into the URL input field and presses enter.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/alertTitle, (72, 259), NULL, NULL): Display a security warning title. The next page is the same security warning page with the options to go back, view the certificate, or continue.
ACTION (android.widget.TextView, android:id/message, (16, 308), NULL, NULL): The control shows a text message about the security issue of the site. There is no action performed on this control and it has no effect on the next page elements.
ACTION (android.widget.Button, android:id/button2, (16, 373), click, NULL): "Go back" button clicked. The subsequent page after this action is the previous webpage, indicating that the former site was left due to a security certificate issue.
ACTION (android.widget.Button, android:id/button3, (99, 373), click, NULL): Click to view security certificate details. The page after clicking displays extensive information about the security certificate, including its validity and issuing authority.
ACTION (android.widget.Button, android:id/button1, (221, 373), click, NULL): The "Continue" button is clicked to proceed despite the security warning. The next page loaded after this interaction changes the URL and brings user to the UC Irvine homepage with varied navigational options and widgets.

````

#### Selected Event(s) and Script
````
Based on the executed action sequence and the current page's intent description, it seems that the test case has navigated to a security warning page after trying to access 'https://uci.edu'. The next step in the test case is to verify the presence of an element on the UCI homepage, but we are currently on a security warning page. 

Given the options on the current page, the most appropriate action would be to click the "Continue" button to proceed despite the security warning. This should bring us to the UCI homepage, where we can then verify the presence of the required element.

Here is the next step:

~~~
ACTION (android.widget.Button, android:id/button1, (221, 373), click, NULL): Click the "Continue" button to proceed despite the security warning.
~~~
Based on the provided information, the corresponding UIAutomator2 code in Python would be:

```python
d(resourceId="android:id/button1", className="android.widget.Button").click()
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.FrameLayout, com.android.browser:id/iconcombo, (9, 24), click, NULL): Clicking on this control leads to a page containing information about the web page, such as its title and URL. There are also buttons for "view certificate" and "OK" on the next page.
ACTION (android.widget.EditText, com.android.browser:id/url, (53, 24), click, NULL): Click to edit the website URL. Following this, the changes would be reflected as new page is loaded based on the edited URL.
ACTION (android.widget.ImageButton, com.android.browser:id/tab_switcher, (272, 24), click, NULL): Click to manage the opened tabs. The next page after clicking this control is the tab management page, which includes options to open new tab, close current tab, and access bookmarks.
ACTION (android.webkit.WebView, Home | UC Irvine, (0, 76), scroll, NULL): Scroll to view the content of UC Irvine's homepage. However, a security warning alert will pop up next, asking the user whether they want to continue with the site due to potential security certificate problems.
ACTION (android.view.View, NULL, (14, 75), click, NULL): Clicking this control will skip through to the main content of the UC Irvine website. The subsequent screen has the main content including a search bar, navigation menu, and various clickable elements like 'News', 'Who We Are', 'Visit', and more.
ACTION (android.view.View, Skip to main content, (14, 75), click, NULL): Click to skip to the main content of the website. It leads to an information page containing details on website certificate and actions of "view certificate" and "ok".
ACTION (android.view.View, Primary navigation, (0, 77), click, NULL): Click to toggle primary navigation. The subsequent page after clicking this control is a security warning page, with options to 'Go back', 'View certificate', or 'Continue'.
ACTION (android.widget.Button, NULL, (261, 85), click, NULL): The clicked button serves to toggle primary navigation on the page. The subsequent page presented after the action remains the UC Irvine homepage with various clickable elements for navigation including options for "Top", "The Buzz", "News", "Who We Are", "Visit" etc.
ACTION (android.view.View, UC Irvine homepage, (0, 77), click, NULL): Click to access the UC Irvine homepage. The next page after this interaction remains the homepage with optional navigational elements like "Search", "Page navigation", and "Campus announcement".
ACTION (android.view.View, University of California, Irvine, (17, 144), click, NULL): Click to navigate to the University of California, Irvine section. The next page showed a security warning about the site’s certificate, it provides options to go back, view the certificate, or continue to the site.
ACTION (android.view.View, NULL, (7, 242), click, NULL): Click to use the search function. The interactions with this control lead to a page with search inputs, along with options for 'Web' and 'People' search.
ACTION (android.widget.EditText, "", (8, 243), click, NULL): Click to input search keywords. The next page after clicking this input field is still the same UC Irvine homepage, indicating that it is expecting user input.
ACTION (android.widget.Button, "", (179, 243), click, NULL): The purpose of this interaction is to initiate a web search. The subsequent screen after using this control will contain the search results based on the input given in the search bar.
ACTION (android.widget.Button, NULL, (235, 243), click, NULL): Click to search for people. The upcoming page after clicking this button is the UCI directory search page, which consists of search controls like name, ucinetid, e-mail or phone extension search entry, and advanced search option.
ACTION (android.view.View, NULL, (0, 297), click, NULL): Interacts with the page navigation. The subsequent page post-interaction has the same layout indicating the page navigation has been interacted with but no significant UI change has occurred.
ACTION (android.view.View, NULL, (10, 297), click, NULL): Action clicks the "Top" link, leading to the top of the page. The subsequent page remains the same, meaning it's a webpage internal navigation link.
ACTION (android.view.View, NULL, (47, 297), click, NULL): Navigation to "The Buzz" page. After clicking, it navigates to the subsequent page with the URL https://uci.edu/.
ACTION (android.view.View, "", (118, 297), click, NULL): Click to view news content. The page after clicking this control is the News page, which contains various news articles and announcements.
ACTION (android.view.View, NULL, (167, 297), click, NULL): Navigate to the 'Who We Are' page. This page provides information about UC Irvine, including its founding history, accolades, student number, degree programs, and contributions to the local and statewide economy.
ACTION (android.view.View, NULL, (256, 297), click, NULL): Click to visit. The page after clicking this control is the Visit page, which has information about visiting the campus, the campus map, and further details about the University of California, Irvine.
ACTION (android.view.View, NULL, (10, 337), click, NULL): Click to navigate to the events page.
ACTION (android.view.View, NULL, (65, 337), click, NULL): Click to navigate to the 'Arts & Athletics' section. The subsequent page is the 'Arts & Athletics' page, displaying related content and navigational controls.
ACTION (android.view.View, Initiatives, (174, 337), click, NULL): Click to access 'Initiatives' section on the website. The next page will contain related information and options for this section.
ACTION (android.view.View, NULL, (248, 337), click, NULL): Click to navigate to the health section. The page after clicking this control is the health section page, which has various health-related controls and elements.
ACTION (android.view.View, NULL, (10, 377), click, NULL): Click on "Alumni & Giving" to navigate to the relative information page. The next page contains sections for "Visit" and "Events".
ACTION (android.view.View, Resources, (121, 377), click, NULL): Click to access the Resources page. The page presented after clicking this control is the Resources page.
ACTION (android.view.View, NULL, (0, 417), click, NULL): Click to view the campus announcement. The next page after clicking this control provides detailed information about the campus announcement.
ACTION (android.widget.Image, Alumni David Smith (left) and Tara Prentice (right), NULL, click, NULL): Click to view information about Alumni David Smith and Tara Prentice. The page after clicking this image remains the home page of UC Irvine.
ACTION (android.view.View, Olympics central, (16, 635), click, NULL): Click to access the Olympics central. The page after clicking this control remains the same with an updated webpage URL.

````

#### Selected Event(s) and Script
````
ASSERT (android.webkit.WebView, Home | UC Irvine, (0, 76), wait_until_element_presence, "UCI homepage"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds.
RETURN: Press the back button to return to the previous page.
~~~
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 76), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page.
DONE
~~~
Based on the provided information, the UIAutomator2 code in Python would be:

···
d(resourceId="Home - UC Irvine Donald Bren School of Information & Computer Sciences").wait(timeout=10)
···

````
### Success
````

ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), click, NULL): Click to activate the URL input field for text input., Exec_Success
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the URL input field and press enter., Exec_Success


ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 76), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds., Exec_Success
ACTION (android.widget.EditText, com.android.browser:id/url, (53, 24), click, NULL): Click to activate the URL input field for text input., Exec_Success
ACTION (android.widget.EditText, com.android.browser:id/url, (53, 24), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the URL input field and press enter., Exec_Success
ASSERT (android.webkit.WebView, Home | UC Irvine, (0, 76), wait_until_element_presence, "UCI homepage"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds.
RETURN: Press the back button to return to the previous page., Exec_Success
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 76), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds., Exec_Success

DONE
````

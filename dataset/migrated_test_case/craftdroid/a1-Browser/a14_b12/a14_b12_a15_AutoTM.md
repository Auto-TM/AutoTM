## a14's b12 to a15

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
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click to input or search for a web address. The page after clicking this control remains the same as the function of this control is to enable text input.
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), longClick, NULL): Long click to interact with the address bar. The next page contains a 'Paste' button to paste copied text into the address bar for quick searching or website access.
ACTION (android.widget.FrameLayout, org.mozilla.focus:id/menuView, (272, 33), click, NULL): Click to open the options menu. The subsequent page contains options like "What's New", "Help", and "Settings".
ACTION (android.widget.ImageView, Firefox Focus, (70, 210), click, NULL): Click to start private browsing. The page after clicking is the same, indicating the app stays in the homepage after the click.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click on the address bar to activate it for text input.
~~~
### Output:

The code should be wrapped using '···':

···
d(resourceId="org.mozilla.focus:id/urlView").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click to input or search for a web address. The page after clicking this control remains the same as the function of this control is to enable text input.
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), longClick, NULL): Long click to interact with the address bar. The next page contains a 'Paste' button to paste copied text into the address bar for quick searching or website access.
ACTION (android.widget.FrameLayout, org.mozilla.focus:id/menuView, (272, 33), click, NULL): Click to open the options menu. The subsequent page contains options like "What's New", "Help", and "Settings".
ACTION (android.widget.ImageView, Firefox Focus, (70, 210), click, NULL): Click to start private browsing. The page after clicking is the same, indicating the app stays in the homepage after the click.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the address bar and press enter.
~~~
Based on the given parameters, the corresponding UIAutomator2 code in Python would be:

```python
d(resourceId="org.mozilla.focus:id/urlView").send_keys("https://www.ics.uci.edu")
d.press('enter')
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageView, org.mozilla.focus:id/security_info, (16, 40), click, NULL): Click to view the security information of the site. The next page shows detailed information about the site's security state verified by Internet2.
ACTION (android.widget.TextView, org.mozilla.focus:id/display_url, (50, 24), click, NULL): Clicking the display URL will open the input field for URL, which has options to edit URL and clear input.
ACTION (android.widget.TextView, org.mozilla.focus:id/display_url, (50, 24), long_click, NULL): Long click to display the URL. The page after long-clicking this control is the custom URL page, which includes the option to add a custom URL.
ACTION (android.widget.ImageButton, org.mozilla.focus:id/menuView, (268, 28), click, NULL): Click to open the options menu. The next page contains multiple controls including security settings, tracking blocker, share, add to home screen, find in page, open with other browsers, app settings, and request desktop site options.
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), scroll, NULL): Scroll to explore more content on the website. The next page after scrolling contains similar elements with additional content about "Accessing STEM in Higher Education" and "High school students who are blind or low vision visit ICS & learn about college life."

ACTION (android.widget.Button, Accessibility Tools, (268, 130), click, NULL): Click to open Accessibility Tools. The page after clicking this control remains the same, indicating that the Accessibility Tools feature may have been triggered in the background or displaying on the same page.
ACTION (android.view.View, NULL, (16, 101), click, NULL): Click on the UCI ICS logo can maybe lead to the home page of UC Irvine Donald Bren School of Information & Computer Sciences. The next page after clicking this control seems to remain on the current page with no changes observed in the page's GUI elements.
ACTION (android.widget.Spinner, NULL, (264, 86), click, NULL): Click to toggle the site search form and navigation. The page after clicking this control remains similar with minor changes in navigation bar height.
ACTION (android.view.View, Accessing STEM in Higher Education, (16, 363), click, NULL): Click to access information on STEM in Higher Education. The next page remains the same after clicking, implying the information is displayed without changing the page.
ACTION (android.view.View, NULL, (16, 502), click, NULL): Click to learn about the experiences of high school students who are blind or low vision visiting ICS & learning about college life. The subsequent page remains the same, indicating the information may appear on the same page or open in a new dialog.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 144), click, NULL): Click to access more information on the "Accessing STEM in Higher Education" topic. The next page remains the same since it's probably an informational pop-up or redirect to another part of the site.
ACTION (android.widget.ImageButton, org.mozilla.focus:id/erase, (248, 568), click, NULL): Click to erase browsing history. The page after clicking this control shows the main interface of the app, where users can enter a new address for browsing.

````

#### Selected Event(s) and Script
````
Based on the executed action sequence and the current page's intent description, the next steps should be:

~~~
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
ACTION (android.widget.TextView, org.mozilla.focus:id/display_url, (50, 24), click, NULL): Clicking the display URL will open the input field for URL, which has options to edit URL and clear input.
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the address bar and press enter.
~~~
Based on the provided instructions, here is the converted UIAutomator2 code in Python:

```python
# Assertion
assert d(description="Donald Bren School of Information and Computer Sciences").wait(timeout=10)

# Actions
d(resourceId="org.mozilla.focus:id/display_url").click()
d(resourceId="org.mozilla.focus:id/urlView").send_keys("https://uci.edu")
d.press('enter')
```

Please note that this code assumes that the device variable name is 'd' and that you have already connected to the device using `d = u2.connect('ip')`.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageView, org.mozilla.focus:id/security_info, (16, 40), click, NULL): Click to inspect the security info of the site. The next page after clicking this control remains the same, and no new components appear.

ACTION (android.widget.TextView, org.mozilla.focus:id/display_url, (50, 24), click, NULL): Click to visit the webpage. The subsequent page has the same element since we're visiting the same page, along with other clickable elements for navigation, interaction and accessing services offered by the website.
ACTION (android.widget.TextView, org.mozilla.focus:id/display_url, (50, 24), long click, NULL): Long click to display options related to the URL. The subsequent page presents a view to edit or clear the input in the URL field.
ACTION (android.widget.ImageButton, org.mozilla.focus:id/menuView, (268, 28), click, NULL): Click to open the menu options. The page after clicking this control is the menu page, which includes multiple options such as "Navigate forward", "Stop loading", "Trackers blocked", "Share", "Add to Home screen", "Find in Page", "Open in…", "Settings", and "Request desktop site".
ACTION (android.webkit.WebView, N/A, (0, 80), scroll, NULL): Scroll to navigate through UC Irvine's homepage. The page after scrolling could reveal further information or different sections of the site like news, events, or resources.
ACTION (android.view.View, Skip to, (0, 79), click, NULL): Click to skip to the main content of the page. The page after clicking this control is the main content page, which shows various sections like 'University of California, Irvine', 'Search', 'Page navigation', and 'Campus announcement'.
ACTION (android.view.View, Skip to main content, (14, 79), click, NULL): Click to skip to the main content of the page. The next page has the same structure and navigation options, with clickable controls that lead to various sections of the website.
ACTION (android.view.View, Primary navigation, (0, 81), click, NULL): Click to expand the primary navigation menu. The next page presented is the UC Irvine homepage with clickable options for the homepage, search, and page navigation.
ACTION (android.widget.Button, Toggle primary navigation, (261, 89), click, NULL): Click to toggle the primary navigation. The next page after clicking this control shows the UC Irvine homepage.
ACTION (android.view.View, NULL, (0, 81), click, NULL): After clicking on the UC Irvine homepage, there were navigation options being displayed for the top news, events and sections such as Arts & Athletics, Initiatives and Health. This action refreshes the homepage and showcases the recent updates.
ACTION (android.view.View, University of California, Irvine, (17, 148), click, NULL): The click to navigate information about the University of California, Irvine. The subsequent page interactions provide additional details about the university including news, events, arts & athletics, health, and resource controls.
ACTION (android.view.View, Search, (7, 246), click, NULL): Click to activate the search function on the website. After clicking, the website remains on the same page, but the focus is on the search bar.
ACTION (android.view.View, Search..., (8, 247), click, NULL): Click to search for content. The next page after clicking this control contains a web search field control, options to search for "Web" and "People", and others controls related to the UC Irvine homepage.
ACTION (android.widget.Button, null, (179, 247), click, NULL): Clicking the Web button switches to the Web search view on the current page.
ACTION (android.widget.Button, People, (235, 247), click, NULL): Click to navigate from the homepage to the UCI directory for searching people. The subsequent page is the UC Irvine directory search page.
ACTION (android.view.View, NULL, (0, 301), click, NULL): Navigate through the different sections of the UC Irvine website such as "The Buzz", "News", "Who We Are", and "Visit". After interacting with this module, the page stays the same but with a different focus depending on the selected section.
ACTION (android.view.View, Top, (10, 301), click, NULL): Click to scroll to the top of the page.
ACTION (android.view.View, The Buzz, (47, 301), click, NULL): Click to navigate to the 'The Buzz' page. The page after clicking this control contains information about 'The Buzz', such as 'An anticancer camera?' and 'Accessing STEM in higher education'.
ACTION (android.view.View, News, (136, 332), click, NULL): Click to navigate to the 'News' section on the UC Irvine homepage. After clicking, the page stays the same as no new elements appear.
ACTION (android.view.View, NULL, (167, 301), click, NULL): Click to navigate to the "Who We Are" section. The following page contains detailed information about UC Irvine including its history, achievements, and contribution to the local economy.
ACTION (android.view.View, Visit, (256, 301), click, NULL): Click to visit the UC Irvine introduction page. The page after clicking this control is the UC Irvine home page, which contains various navigation options such as "Top", "The Buzz", "News", "Who We Are", "Events", "Arts & Athletics", "Initiatives", "Health", "Alumni & Giving", and "Resources".
ACTION (android.view.View, Events, (10, 341), click, NULL): Click to view the Events page. The next page contains options to navigate to top, news, and other details, along with a campus announcement section.
ACTION (android.view.View, NULL, (65, 341), click, NULL): Click on 'Arts & Athletics' to navigate to the corresponding page. The page after clicking this control displays further information about 'Arts & Athletics' at UC Irvine.
ACTION (android.view.View, Initiatives, (174, 341), click, NULL): Click to access the 'Initiatives' page. The next page after clicking this control displays specific information about "Who We Are" at UC Irvine, along with options related to the About UC Irvine section.
ACTION (android.view.View, Health, (248, 341), click, NULL): Click to access Health section. The subsequent page does not show new widgets related to the Health click action as it would require a refresh.
ACTION (android.view.View, Alumni & Giving, (10, 381), click, NULL): Click to access the alumni and giving resources. After clicking, it leads to a page with options for the user to interact with the site's functionality.
ACTION (android.view.View, Resources, (121, 381), click, NULL): Click to access resources. The page after clicking this control is the resources page with site security, display url, menu for more options, and a control to erase browsing history.
ACTION (android.view.View, Campus announcement, (0, 421), click, NULL): The announcement on the campus is clickable and will redirect the user to detailed announcement page upon clicking.
ACTION (android.widget.Image, Alumni David Smith (left) and Tara Prentice (right), (0, 421), click, NULL): Clicking the image initiates a page redirection to display more detailed information about the Alumni David Smith and Tara Prentice. The next page only contains functional controls - site security, display URL, more options, and erase browsing history.
ACTION (android.view.View, Olympics central, (16, 639), click, NULL): Click to access the Olympics central. The page after clicking showcases the achievements of Alumni David Smith and Tara Prentice in the Olympics.
ACTION (android.widget.ImageButton, org.mozilla.focus:id/erase, (248, 568), click, NULL): Click to erase browsing history. The next page after clicking this control is a new search page where one can enter an address or search term.

````

#### Selected Event(s) and Script
````
ASSERT (android.webkit.WebView, Home - University of California, Irvine, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc="UCI homepage"]"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds.
ACTION (android.widget.ImageButton, org.mozilla.focus:id/back, (8, 33), click, NULL): Click the back button to return to the previous page.
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page.
DONE
~~~
The following is the UIAutomator2 code in Python that corresponds to the provided test semantic descriptions:

```python
d.xpath('//android.view.View[@content-desc="UCI homepage"]').wait(timeout=10)
d.press('back')
d.xpath('//android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]').wait(timeout=10)
```

Please note that the 'wait' function in UIAutomator2 is used to wait for the specified element to appear within the given timeout (in seconds). If the element does not appear within the timeout, an exception will be thrown.
````
### Success
````
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click on the address bar to activate it for text input., Exec_Success

ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the address bar and press enter., Exec_Success

ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds., Exec_Success
ACTION (android.widget.TextView, org.mozilla.focus:id/display_url, (50, 24), click, NULL): Clicking the display URL will open the input field for URL, which has options to edit URL and clear input., Exec_Success
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the address bar and press enter., Exec_Success

ASSERT (android.webkit.WebView, Home - University of California, Irvine, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc="UCI homepage"]"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds., Exec_Success
ACTION (android.widget.ImageButton, org.mozilla.focus:id/back, (8, 33), click, NULL): Click the back button to return to the previous page., Exec_Success
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page., Exec_Success
DONE
````

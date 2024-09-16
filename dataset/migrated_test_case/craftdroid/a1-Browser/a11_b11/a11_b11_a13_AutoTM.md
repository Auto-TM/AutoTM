## a11's b11 to a13

### Semantics of Source Test case
> This test case is testing the search functionality that tests navigation to a website and verifying the presence of a specific element.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (EditText, acr.browser.lightning:id/search, (), click, NULL) : Click on the search field to activate it for text input.
> 2. ACTION (EditText, acr.browser.lightning:id/search, (), input, "https://www.ics.uci.edu") : Input the URL 'https://www.ics.uci.edu' into the search field and press enter.
> 3. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc=\"Donald Bren School of Information and Computer Sciences\"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to open the navigation drawer. The next page consists of various navigation options such as home, forward, history, downloads, domains, settings, guide, about and clear and exit.
ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click to check a website's SSL certificate. The page appearing after clicking this control shows a detailed analysis of the SSL certificate, including domain, issuer and valid date information.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click to input a URL or search directly. The subsequent page remains the same except that the focus is on the URL EditText and the keyboard is expected to be visible.
ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): Toggles the JavaScript setting. After clicking this control, there is no change of page, but the JavaScript setting of the current page can be changed, improving user browsing experience.
ACTION (android.widget.ImageView, "", (280, 28), click, NULL): Click to open more options. The subsequent page after clicking displays various options such as: "Add Domain Settings", "First-Party Cookies", "Third-Party Cookies", "DOM Storage", "Form Data", "Clear Data", "Font Size - 100%", "Display Images", "Share", "Find on Page", "Print", and "View Source".
ACTION (android.webkit.WebView, DuckDuckGo, (0, 80), scroll, NULL): Scroll operation on DuckDuckGo web page. The page after interaction remains the same.
ACTION (android.view.View, NULL, (77, 192), click, NULL): Clicking the "About DuckDuckGo" description leads to the 'About' page of DuckDuckGo. This page features information about DuckDuckGo's privacy policy, their mission, and their services.
ACTION (android.widget.Button, Search, (259, 362), click, NULL): Click to search. The subsequent page after clicking is the search results page.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click on the search field to activate it for text input.
~~~
### Output(The code should be wrapped using '···'):
···
d(resourceId="com.stoutner.privacybrowser.standard:id/url_edittext").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, null, (0, 24), click, NULL): Click to open the navigation drawer. The next page has various navigation options like Home, Back, Forward, History, Downloads, Domains, Settings, Guide, About, and Clear and Exit.
ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click to add this page to favorites. The page after clicking this control is an SSL Certificate information page showing details about the page's security certificate.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click to enter or edit URL. The subsequent page after interaction remains unchanged, indicating the user can perform a search or navigate to the URL entered.

ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): Click to toggle JavaScript. The page after clicking stays the same showing the JavaScript component status (enabled/disabled) without transitioning to a new page.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): Click to open the options menu. The next page after clicking displays a list of different settings and actions including 'Add Domain Settings', 'First-Party Cookies', 'Third-Party Cookies', 'DOM Storage', 'Form Data', 'Clear Data', 'Font Size - 100%', 'Display Images', 'Share', 'Find on Page', 'Print', 'View Source'.
ACTION (android.webkit.WebView, DuckDuckGo, (0, 80), scroll, NULL): Scroll to navigate through the DuckDuckGo webview. The subsequent page after scrolling has similar elements with slight changes in their positions.
ACTION (android.view.View, About DuckDuckGo, (49, 150), click, NULL): Clicking this control navigates to the About DuckDuckGo page with further details about the company including their privacy policy and business principles.
ACTION (android.widget.Button, "", (259, 231), click, NULL): Click the Search button to initiate the search function. The next page remains the same, suggesting that search results are being loaded on the same page.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter.
~~~
Based on the provided parameters, the UIAutomator2 code in Python would be:

```python
d(resourceId="com.stoutner.privacybrowser.standard:id/url_edittext").send_keys("https://www.ics.uci.edu")
d.press('enter')
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to open the navigation drawer. The page after clicking this control allows access to different parts of the website such as Home, Back, Forward, History, Downloads, Domains, Settings, Guide, About, and Clear and Exit functions.
ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click to add the current webpage to favorites. The page appearing after interacting with this widget shows SSL certificate details of the page.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click to edit URL. The page after clicking this control remains unchanged, indicating the action is likely to prompt the keyboard for URL input or edit.
ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): Enables or disables JavaScript on the page. The subsequent page content might change depending on the JavaScript dependencies.
ACTION (android.widget.ImageView, NULL, (280, 28), click, NULL): Click to view more options. The page after this control is clicked contains different settings options like 'Add Domain Settings', 'First-Party Cookies', 'Third-Party Cookies', 'DOM Storage', 'Form Data', 'Clear Data', 'Font Size - 100%', 'Display Images', 'Share', 'Find on Page', 'Print', and 'View Source'.
ACTION (android.webkit.WebView, NONE, (0,80), click, NULL): User scrolls through 'Home - UC Irvine Donald Bren School of Information & Computer Sciences' page. The next page is the same page as the interaction does not navigate to another page.
ACTION (android.view.View, NULL, (16, 112), click, NULL): Click to navigate to UCI ICS homepage. The page remains the same after clicking this control.
ACTION (android.widget.Spinner, NULL, (264, 90), click, NULL): Click to toggle the site search form & navigation. The page after clicking this control remains the same, retaining all functionality and features.
ACTION (android.view.View, Accessing STEM in Higher Education, (16, 314), click, NULL): Click to access information about STEM in Higher Education. The subsequent page contains additional details about how high school students who are blind or have low vision can learn about college life.
ACTION (android.view.View, NULL, (16, 452), click, NULL): Click to access more details about High school students who are blind or low vision visit ICS & learn about college life. The next page appears to be the same as the current page, indicating this may have opened a dialog or updated an element on the page dynamically.
ACTION (android.view.View, NULL, (16, 620), click, NULL): Click "Read More" to navigate to a detailed page about "Accessing STEM in Higher Education". The next page contains an article with more details, including sharing options for social media and email.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 144), click, NULL): Click to view the AccessSTEM_PeterGroup_portrait picture. The page remains the same after clicking.
ACTION (android.widget.Button, NULL, (268, 130), click, NULL): Click to open Accessibility Tools. The page after clicking this control remains the same. Only that the Accessibility Tools settings are now opened.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.webkit.WebView, NONE, (0,80), wait_until_element_presence, "Home - UC Irvine Donald Bren School of Information & Computer Sciences"): Verify that the element with the content description 'Home - UC Irvine Donald Bren School of Information & Computer Sciences' is present within 10 seconds.
DONE
~~~
Based on your provided information, here's the UIAutomator2 code in Python:

···
assert (d(resourceId="android.webkit.WebView").wait(timeout=10).info.get('contentDescription') == "Home - UC Irvine Donald Bren School of Information & Computer Sciences")
···
````
### Success
````
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click on the search field to activate it for text input., Exec_Success

ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter., Exec_Success

ASSERT (android.webkit.WebView, NONE, (0,80), wait_until_element_presence, "Home - UC Irvine Donald Bren School of Information & Computer Sciences"): Verify that the element with the content description 'Home - UC Irvine Donald Bren School of Information & Computer Sciences' is present within 10 seconds., Exec_Success
DONE
````

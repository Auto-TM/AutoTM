## a15's b11 to a13

### Semantics of Source Test case
> This test case is testing the search functionality that tests navigation to a website and verifying the presence of a specific element in the Mozilla Focus browser.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (Button, org.mozilla.focus:id/skip, (), click, NULL) : Click on the 'Skip' button to bypass any onboarding or introduction screens.
> 2. ACTION (EditText, org.mozilla.focus:id/urlView, (), click, NULL) : Click on the search field with the text 'Search or enter address' to activate it for text input.
> 3. ACTION (EditText, org.mozilla.focus:id/urlView, (), input, "https://www.ics.uci.edu") : Input the URL 'https://www.ics.uci.edu' into the search field and press enter.
> 4. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc=\"Donald Bren School of Information and Computer Sciences\"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to open navigation drawer. The page after clicking this button contains options for Home, Back, Forward, History, Downloads, Domains, Settings, Guide, About, and Clear and Exit.
ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click to open the SSL Certificate page. The page after clicking this control shows the SSL Certificate details of the site domain, issue information and valid dates.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click to enter a URL. The subsequent page after clicking this control is DuckDuckGo Search, which includes search components and search results.
ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): Click to toggle JavaScript setting. After clicking, the state of JavaScript either enabled or disabled is reflected on the page.
ACTION (android.widget.ImageView, NULL, (280, 28), click, NULL): Click to see more options. The subsequent page contains various settings and functionalities such as Add Domain Settings, First-Party Cookies, Third-Party Cookies, DOM Storage, Form Data, Clear Data, Font Size - 100%, Display Images, Share, Find on Page, Print, and View Source.
ACTION (android.webkit.WebView, DuckDuckGo, (0, 80), scroll, NULL): User might scroll to view or access other elements on the webpage. No distinct changes on the next page indicate the action might be limited to viewing content on DuckDuckGo.

ACTION (android.view.View, NULL, (77, 192), click, NULL): Click to open "About DuckDuckGo" page. The subsequent page provides detailed information about DuckDuckGo, including its commitment to user privacy and its various features.
ACTION (android.widget.Button, Search, (259, 362), click, NULL): Click to search for the entered query. The page after clicking this control shows the search results on the DuckDuckGo webpage.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click on the search field to activate it for text input, similar to the 'Skip' button action in the source test case.
~~~
Based on the provided input, the corresponding UIAutomator2 code in Python should be:

···
d(resourceId="com.stoutner.privacybrowser.standard:id/url_edittext").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Open the navigation drawer to reach different options including Home, Back, Forward, History, Downloads, Domains, Settings, Guide, About and Clear and Exit.
ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click to add current page to favorites. The next page represents additional information on the selected website, displaying data such as domain name, SSL Certificate information, the organization it's issued to, valid dates and closes with a button.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): This interaction indicates clicking the URL text field to enter a new search or website URL. The same page is being maintained with the URL text field in focus to facilitate user input.
ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): The toggle for the JavaScript engine in the browser. When clicked, the JavaScript setting is toggled, enabling or disabling JavaScript execution on web pages. The new state of this setting is reflected in the visual update of this toggle. No new GUI elements are introduced in the next page after the interaction.
ACTION (android.widget.ImageView, None, (280,28), click, NULL): Click to expand more options. The page after clicking this control is the options page, which includes settings such as 'Add Domain Settings', 'First-Party Cookies', 'Third-Party Cookies', 'DOM Storage', 'Form Data', 'Clear Data', 'Font Size - 100%', 'Display Images', 'Share', 'Find on Page', 'Print', and 'View Source'.
ACTION (android.webkit.WebView, DuckDuckGo, (0, 80), scroll, NULL): Scrolling on the DuckDuckGo web view. The subsequent page remains similar with the search bar and About DuckDuckGo clickable link.
ACTION (android.view.View, NULL, (49, 150), click, NULL): Clicks to learn about DuckDuckGo. The resulting page changes the URL to DuckDuckGo's about page and provides detailed information about the privacy offered by DuckDuckGo, including several clickable views describing their approach to user data and privacy.
ACTION (android.widget.Button, Search, (259, 231), click, NULL): Clicking the search button directs towards search result page. The page after clicking this button represents the list of search results, which can then be clicked for further navigation.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter, similar to the third action in the source test case.
~~~
Based on the given actions, the UIAutomator2 code in Python is as follows:

```python
d(resourceId="com.stoutner.privacybrowser.standard:id/url_edittext").set_text("https://www.ics.uci.edu")
d.press('enter')
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, "", (0, 24), click, NULL): Click to open the navigation drawer. The page after clicking this control is the navigation page, which has various action controls like Home, Back, Forward, History etc.

ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click to view details of SSL certificate for the current website. The page after clicking this control shows detailed SSL certificate information for the website.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click to enter or edit a web URL. After interacting with this control, the page remains the same, but the user is able to input or change the web URL.
ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): Toggles Javascript setting on the page. The next page after interacting with this control doesn't change, since it only modifies the Javascript setting without navigating away from the current page.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): The action brings up a menu of additional options, which includes Add Domain Settings, Cookies Control, Form Data Handling, Clear Data options, Font Size adjustments, Image Display settings, Sharing options, Find on Page functionality, Printing, and Source Code Viewing as per the Next Page JSON.
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), scroll, NULL): The user can scroll through the page of UC Irvine's Donald Bren School of Information & Computer Sciences. This page includes clickable controls such as the UCI ICS logo, a navigation toggle, article links, and accessibility tools.
ACTION (android.view.View, NULL, (16, 112), click, NULL): Clicks on the UCI ICS logo. The page after clicking is the Home page of UCI Irvine Donald Bren School of Information & Computer Sciences, containing controls like site search form & navigation toggle, Accessibility Tools button, and clickable content related to Accessing STEM in Higher Education.
ACTION (android.widget.Spinner, NULL, (264, 90), click, NULL): Click to toggle site navigation and search form. The following page contains tools for website accessibility and has various clickable text and image elements that can be interacted with.
ACTION (android.view.View, NULL, (16, 314), click, NULL): Click to access information on STEM in Higher Education. The next page continues the information about Accessing STEM in Higher Education with more details.
ACTION (android.view.View, NULL, (16, 452), click, NULL): Click to learn about the experience of high school students who are blind or low vision visiting ICS & learning about college life. After clicking this control, the page remains the same as it presumably loads more content relating to this topic.
ACTION (android.view.View, NULL, (16, 620), click, NULL): Click to read more about "Accessing STEM in Higher Education." The next page after clicking this control details the article including share options and publication date.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 144), click, NULL): Click to open AccessSTEM in Higher Education page. The next page contains information about high school students who are blind or low vision visiting ICS and learning about college life.
ACTION (android.widget.Button, Accessibility Tools, (268, 130), click, NULL): Click to access accessibility tools. The page after clicking this control remains the UC Irvine Donald Bren School of Information & Computer Sciences home page with the information about Accessing STEM in Higher Education, which stays consistent across interactions.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc=\"Donald Bren School of Information and Computer Sciences\"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds, similar to the fourth action in the source test case.
DONE
~~~
Based on the information you provided, here is the UIAutomator2 code in Python:

```python
assert (d.xpath('//android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]').wait(timeout=10))
```

This code verifies that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
````
### Success
````
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click on the search field to activate it for text input, similar to the 'Skip' button action in the source test case., Exec_Success

ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter, similar to the third action in the source test case., Exec_Success

ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 80), wait_until_element_presence, "xpath://android.view.View[@content-desc=\"Donald Bren School of Information and Computer Sciences\"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds, similar to the fourth action in the source test case., Exec_Success
DONE
````

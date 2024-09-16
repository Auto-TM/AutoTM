## a11's b11 to a15

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
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click to input a URL or conduct a search. The same page remains afterward, indicating that the user can type in this box without navigating to a new page.
ACTION (android.widget.FrameLayout, org.mozilla.focus:id/menuView, (272, 33), click, NULL): Click to open the more options menu. The page after clicking this control shows the "What's New", "Help", and "Settings" options.
ACTION (android.widget.ImageView, Firefox Focus, (70, 210), NULL, NULL): Activates the Firefox Focus app for automatic private browsing. The subsequent page remains the same as the current page because the action does not entail any noticeable transition.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click on the search field to activate it for text input.
~~~
Based on the given parameters, the corresponding UIAutomator2 code in Python would be:

···
d(resourceId="org.mozilla.focus:id/urlView").click()
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click to focus the input field for searching or entering an address. No change in the GUI elements on the next page as it remains the same in the JSON data provided.
ACTION (android.widget.FrameLayout, org.mozilla.focus:id/menuView, (272, 33), click, NULL): Click to open the options menu. The next page after clicking this control is the menu page, which contains 'What's New', 'Help', and 'Settings' options.
ACTION (android.widget.ImageView, No ID, (70, 210), click, NULL): Firefox Focus has been clicked for automatic private browsing. The subsequent page doesn't have new controls, it looks identical to the current page.

````

#### Selected Event(s) and Script
````
Based on the provided information, the next action should be to input the URL 'https://www.ics.uci.edu' into the search field and press enter. This action aligns with the intention of the original test case, which is to navigate to a specific website and verify the presence of a specific element. The search field has already been activated for text input, so the URL can be entered directly.

~~~
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter.
~~~
Based on your given parameters, here is the UIAutomator2 code in Python:

···
d(resourceId="org.mozilla.focus:id/urlView", className="android.widget.EditText").set_text("https://www.ics.uci.edu")
d.press('enter')
···

This code will input the URL 'https://www.ics.uci.edu' into the search field identified by the ID 'org.mozilla.focus:id/urlView' and press enter.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageView, org.mozilla.focus:id/security_info, (16, 40), click, NULL): Click to view site security information. The page after clicking this control is the site security page, which displays information about the secure connection, site identity title, and verification details.
ACTION (android.widget.TextView, org.mozilla.focus:id/display_url, (50, 24), click, NULL): The purpose of clicking this element is to view the complete URL. After clicking, the URL becomes editable in a text box, providing an option to modify or clear the input.
ACTION (android.widget.ImageButton, org.mozilla.focus:id/menuView, (268, 28), click, NULL): Click to open the options menu. The next page after the click presents a variety of usable controls including navigation, refreshing, tracking options, share, 'Add to Home screen,' 'Find in Page,' 'Open with…', settings, and 'Request desktop site'.
ACTION (android.webkit.WebView, NULL, (0, 80), scroll, NULL): Scroll the webpage to view content of "Home - UC Irvine Donald Bren School of Information & Computer Sciences". The 'Next Page JSON' indicates that this action doesn't change the page elements but might update their positions.
ACTION (android.widget.Button, Accessibility Tools, (268, 130), click, NULL): Clicking this "Accessibility Tools" button leads to the next page, which seems to lack specific elements indicating the purpose of interaction. One can infer the page mainly allows user to navigate or browse through the content.
ACTION (android.view.View, NULL, (16, 101), click, NULL): Click to access UCI ICS logo. The page after clicking this control is the UCI ICS website, which has more information about UCI ICS.
ACTION (android.widget.Spinner, NULL, (264, 86), click, NULL): Click to toggle the site search form and navigation. After clicking this control, the website page remains on https://ics.uci.edu/ but the navigation is altered.
ACTION (android.view.View, NULL, (16, 363), click, NULL): Click to reveal article about Accessing STEM in Higher Education. The page after clicking this control is the specific article page which does not carry any actionable item as viewed from the Next Page JSON.

ACTION (android.view.View, NULL, (16, 502), click, NULL): Click to read about the high school students who are blind or low vision visiting ICS & learning about college life. The page after clicking this control remains the same, with various interactive elements including an image of the students, an Accessibility Tools button, and additional information about ICS.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 144), click, NULL): Click to view the full image related to STEM education in higher education. The page after clicking this control remains the same, preserving the context of the current webpage.
ACTION (android.widget.ImageButton, org.mozilla.focus:id/erase, (248, 568), click, NULL): Click to erase browsing history. After clicking this control, the current browsing page will be closed and return to the homepage.

````

#### Selected Event(s) and Script
````
Based on the executed action sequence, the search field has been activated and the URL "https://www.ics.uci.edu" has been entered successfully. The next step in the source application's test case is to verify the presence of a specific element, "Donald Bren School of Information and Computer Sciences". 

Looking at the current page's intent description, there is no direct action to verify the presence of a specific element. However, there are several actions that allow us to interact with the page content. For example, we can scroll the webpage or click on various elements to navigate through the content. 

Given this information, the next logical step would be to scroll the webpage to view the content and look for the specific element. 

Here is the next action to be executed:

~~~
ACTION (android.webkit.WebView, NULL, (0, 80), scroll, NULL): Scroll the webpage to view content of "Home - UC Irvine Donald Bren School of Information & Computer Sciences".
~~~
Based on the provided information, the UIAutomator2 code in Python will be:

```python
d.swipe(0, 80, 0, 0)
```

The code above represents the action of scrolling the webpage. The swipe method in uiautomator2 is used to perform a swipe action on the screen. The parameters (0, 80, 0, 0) represent the starting and ending coordinates of the swipe action. It starts from (0, 80) and ends at (0, 0), which means the action is a scroll from bottom to top.
````
#### Contextual Semantics of Widgets
````
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 0), scroll, NULL): Scroll to browse through the ICS information on the UC Irvine home page. The subsequent page after this scroll interaction remains the same, indicating no significant change in the elements or user interface.
ACTION (android.widget.Button, NULL, (268, 1), click, NULL): Click on the 'Accessibility Tools' button. The following page does not provide specific GUI elements which indicates that a page change has likely occurred.
ACTION (android.view.View, '', (16, 234), click, NULL): Click to view more details about 'Accessing STEM in Higher Education'. The next page is the detailed information page related to the selected topic.
ACTION (android.view.View, NULL, (16, 373), click, NULL): Click to learn about high school students who are blind or low vision visit ICS & learning about college life. The subsequent page after the click action is mainly blank, indicating it may be loading information related to the clicked topic or it may take the user to an expanded article or more details.

ACTION (android.view.View, NULL, (16, 541), click, NULL): Click to read more about 'High school students who are blind or low vision visit ICS & learn about college life'. The next page is the detail information page which is blank and scrollable.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 15), click, NULL): Click to open the picture. The next page after clicking may provide a larger view of the picture or additional information related to it.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 0), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within the page.
DONE
~~~
Based on the given parameters, the UIAutomator2 code in Python is:

···
assert d(description="Donald Bren School of Information and Computer Sciences", className="android.webkit.WebView").exists
···
````
### Success
````
ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), click, NULL): Click on the search field to activate it for text input., Exec_Success

ACTION (android.widget.EditText, org.mozilla.focus:id/urlView, (8, 33), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter., Exec_Success

ACTION (android.webkit.WebView, NULL, (0, 80), scroll, NULL): Scroll the webpage to view content of "Home - UC Irvine Donald Bren School of Information & Computer Sciences"., Exec_Success

ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 0), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within the page., Exec_Success
DONE
````

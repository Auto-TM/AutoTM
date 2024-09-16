## a12's b11 to a11

### Semantics of Source Test case
> This test case is testing the URL navigation functionality in the browser application. It verifies the ability to navigate to a specific website and checks the presence of a specific element on the webpage.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (EditText, com.android.browser:id/url, (), click, NULL) : Click on the URL field to activate it for text input.
> 2. ACTION (EditText, com.android.browser:id/url, (), input, "https://www.ics.uci.edu") : Input the URL 'https://www.ics.uci.edu' into the URL field and press enter.
> 3. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc=\"Donald Bren School of Information and Computer Sciences\"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.webkit.WebView, Homepage, (0, 82), scroll, NULL): The homepage does not change after interaction, indicating it's a scrollable viewing area for the app's content. The homepage contains clickable elements like 'Search' button and 'More options'.
ACTION (android.widget.Button, NULL, (241, 374), click, NULL): Clicking the search button activates the search function. In the next page, a search field and a search button are displayed, allowing users to type and submit their search query.
ACTION (android.widget.FrameLayout, acr.browser.lightning:id/arrow_button, (0, 26), click, NULL): Click to navigate to a different page. The subsequent page contains elements to open a new tab, move back or forward and access more options.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): Click to perform a search. The page after clicking this control is the search results page, which has a search button, an editable search bar, and search result components.
ACTION (android.widget.ImageView, More options, (272, 30), click, NULL): Click to access more options. The subsequent page contains a list of actions such as 'New tab', 'History', 'Downloads' etc.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): Click on the URL field to activate it for text input.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the URL field and press enter.
~~~
The following is the generated UIAutomator2 code:

```python
d(resourceId="acr.browser.lightning:id/search").click()
d(resourceId="acr.browser.lightning:id/search").send_keys("https://www.ics.uci.edu")
d.press('enter')
```
````
#### Contextual Semantics of Widgets
````
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 82), loadURL, "https://ics.uci.edu"): Navigates to the UCI ICS homepage. The next page displays information about the UCI ICS, along with several clickable elements such as the UCI ICS logo, Accessing STEM in Higher Education, and High school students who are blind or low vision visit ICS & learn about college life.
ACTION (android.widget.Button, Accessibility Tools, (268, 132), click, NULL): Click to access Accessibility Tools. The next page is the same as the current page, no further components are affected by this action.
ACTION (android.view.View, UCI ICS logo, (16, 103), click, NULL): Click to go to the homepage. After clicking this control, the page does not change as it already display the home page.
ACTION (android.widget.Spinner, Toggle site search form & navigation, (264, 90), click, NULL): Click to toggle between the site search form and navigation. The page after clicking this control is similar with an option to toggle search form & navigation.
ACTION (android.view.View, Accessing STEM in Higher Education, (16, 365), click, NULL): Click to access information about STEM in higher education. The subsequent page after the interaction is the detailed educational resources page notating specifics in regard to students who are blind or have low vision, visiting ICS & learning about college life.
ACTION (android.view.View, NULL, (16, 504), click, NULL): Click to provide blind or low vision high school students information about college life at UC Irvine Donald Bren School of Information & Computer Sciences. After clicking, the page remains the same with the content potentially loaded within the WebView.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 146), click, NULL): Click to view the 'AccessSTEM_PeterGroup_portrait'. The page after clicking this control is the same homepage, as the image does not lead to a different page or open a new interface.
ACTION (android.widget.FrameLayout, acr.browser.lightning:id/arrow_button, (0, 26), click, NULL): Click to go back to the previous page. The next page contains the browser's tab management and navigation options.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): The purpose is to enter a search query. The subsequent page listed the query results.
ACTION (android.widget.ImageView, More options, (272, 30), click, NULL): Click to open a drop-down list offering various options such as creating a new tab, accessing the browsing history, sharing the page, etc. on the subsequent page.

````

#### Selected Event(s) and Script
````
Based on the executed actions and the current page's intent description, the next step is to verify that we have successfully navigated to the correct URL and that the required element is present on the page. The element we are looking for, according to the function description, is a view with the content description "Donald Bren School of Information and Computer Sciences". 

From the current page's intent description, there isn't an exact match for the element we are looking for. However, there is a view with the text "Home - UC Irvine Donald Bren School of Information & Computer Sciences" which seems to be the closest match. We can assert the presence of this view to confirm that we have navigated to the correct URL.

~~~
ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 82), wait_until_element_presence, "Home - UC Irvine Donald Bren School of Information & Computer Sciences"): Verify that the element with the content description 'Home - UC Irvine Donald Bren School of Information & Computer Sciences' is present within 10 seconds.
DONE
~~~
Here is the UIAutomator2 code corresponding to the given action:

```python
import time
start_time = time.time()
while time.time() - start_time < 10:
    if d(description="Home - UC Irvine Donald Bren School of Information & Computer Sciences").exists:
        break
    time.sleep(1)
else:
    assert False, "Element with description 'Home - UC Irvine Donald Bren School of Information & Computer Sciences' not found within 10 seconds."
```

In the above code, we are continuously checking for the presence of the element with the given content description for 10 seconds. If the element is not found within this time, an assertion error is raised.
````
### Success
````
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): Click on the URL field to activate it for text input., Exec_Success
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the URL field and press enter., Exec_Success

ASSERT (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 82), wait_until_element_presence, "Home - UC Irvine Donald Bren School of Information & Computer Sciences"): Verify that the element with the content description 'Home - UC Irvine Donald Bren School of Information & Computer Sciences' is present within 10 seconds., Exec_Success
DONE
````

## a14's b12 to a11

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
ACTION (android.webkit.WebView, Homepage, (0, 82), scroll, NULL): Scroll to navigate through the Homepage. The next page after this action remains the Homepage, maintaining similar elements and their respective functionalities.
ACTION (android.widget.Image, google, (80, 298), click, NULL): The action of clicking on the "Google" logo is typically associated with redirecting to the homepage. In the next page JSON, we see that our elements maintain the same layout reinforcing that we are still on the same homepage indicating no significant changes have occurred.
ACTION (android.widget.Button, Search, (241, 374), click, NULL): Click to perform a search. After clicking this control, the search results will be displayed on the same page, and the search box and search button will be moved to different coordinates.
ACTION (android.widget.FrameLayout, acr.browser.lightning:id/arrow_button, (0, 26), click, NULL): Click to go to the tabs interface where the user can interact with the current tabs, add a new tab or return to the homepage.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): The action represents clicking on the search bar. After this action, the webpage stays the same but the UI changes to focus on the search bar, allowing the user to type in their search query.
ACTION (android.widget.ImageView, More options, (272, 30), click, NULL): Click to view more options. The next page contains a list of actions such as "New tab", "New incognito tab", "Share", "History", "Downloads", "Find in page", "Copy link", "Add to home screen", "Bookmarks", "Add Bookmark", "Reader mode", "Settings".

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.FrameLayout, acr.browser.lightning:id/arrow_button, (0, 26), click, NULL): Click to go to the tabs interface to initiate a new action similar to the source test case.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): Click on the search bar to activate it for text input.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search bar and press enter.
ASSERT (android.webkit.WebView, Homepage, (0, 82), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the search bar and press enter.
ASSERT (android.webkit.WebView, Homepage, (0, 82), wait_until_element_presence, "UCI homepage"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds.
RETURN: Press the back button to return to the previous page.
ASSERT (android.webkit.WebView, Homepage, (0, 82), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page.
DONE
~~~
Based on the provided requirements and actions, the corresponding UIAutomator2 code in Python would look like this:

```python
# Click to go to the tabs interface to initiate a new action similar to the source test case.
d(resourceId="acr.browser.lightning:id/arrow_button").click()

# Click on the search bar to activate it for text input.
d(resourceId="acr.browser.lightning:id/search").click()

# Input the URL 'https://www.ics.uci.edu' into the search bar and press enter.
d(resourceId="acr.browser.lightning:id/search").send_keys("https://www.ics.uci.edu")
d.press('enter')

# Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
assert d(description="Donald Bren School of Information and Computer Sciences").wait(timeout=10)

# Input the URL 'https://uci.edu' into the search bar and press enter.
d(resourceId="acr.browser.lightning:id/search").send_keys("https://uci.edu")
d.press('enter')

# Verify that the element with the content description 'UCI homepage' is present within 10 seconds.
assert d(description="UCI homepage").wait(timeout=10)

# Press the back button to return to the previous page.
d.press('back')

# Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page.
assert d(description="Donald Bren School of Information and Computer Sciences").wait(timeout=10)
```

Please note that the `wait_until_element_presence` action was translated into `wait(timeout=10)` in the code. This will wait for the specified element to be present within the given timeout (in seconds).
````
### Success
````
, Exec_Success
ACTION (android.widget.FrameLayout, acr.browser.lightning:id/arrow_button, (0, 26), click, NULL): Click to go to the tabs interface to initiate a new action similar to the source test case., Exec_Success
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): Click on the search bar to activate it for text input., Exec_Success
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search bar and press enter., Exec_Success
ASSERT (android.webkit.WebView, Homepage, (0, 82), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds., Exec_Success
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the search bar and press enter., Exec_Success
ASSERT (android.webkit.WebView, Homepage, (0, 82), wait_until_element_presence, "UCI homepage"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds., Exec_Success
RETURN: Press the back button to return to the previous page., Exec_Success
ASSERT (android.webkit.WebView, Homepage, (0, 82), wait_until_element_presence, "Donald Bren School of Information and Computer Sciences"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page., Exec_Success
DONE
````

## a15's b11 to a11

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
ACTION (android.webkit.WebView, Homepage, (0, 82), scroll, NULL): The user is on the homepage and is able to scroll through it. Post interaction with the home page, the options remain the same indicating no change in the GUI elements, thus the user likely just browsed without clicking anything significant.
ACTION (android.widget.Button, Search, (241, 374), click, NULL): Click to perform a search. The next page after clicking this control is the search result page, which contains google image and search button.
ACTION (android.widget.FrameLayout, acr.browser.lightning:id/arrow_button, (0, 26), click, NULL): Click to open the tab management page. After the click, tabs can be viewed, new tabs can be opened, and the current tab can be closed.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): Click to trigger the search function. The page after clicking this control is the search result page, containing the Google logo and the search text input field.
ACTION (android.widget.ImageView, '', (272, 30), click, NULL): Click to open the menu options. The next page features a ListView comprising various options such as creating a new tab, incognito tab, share, history, downloads, find in page, copy link, add to home screen, bookmarks, add bookmark, reader mode, and settings.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.Button, Search, (241, 374), click, NULL): Click on the 'Search' button to activate the search field.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter.
~~~
Based on your provided information, here is the UIAutomator2 code in Python:

···
d(resourceId="Search", className="android.widget.Button").click()
d(resourceId="acr.browser.lightning:id/search", className="android.widget.EditText").send_keys("https://www.ics.uci.edu")
d.press('enter')
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 82), scroll, NULL): Scroll to interact with the UCI ICS website. The page after scrolling remains the same with accessible options for interacting with news, a search bar, navigation toggle, and a UCI ICS logo.
ACTION (android.widget.Button, Accessibility Tools, (268, 132), click, NULL): Click to navigate to the Accessibility Tools page. The page after clicking this control is the same as the current page, as it's a toggle button for accessibility tools.
ACTION (android.view.View, UCI ICS logo, (16, 103), click, NULL): Click to navigate to UCI ICS logo. After clicking, the page remains same, there is no transition.
ACTION (android.widget.Spinner, NULL, (264, 90), click, NULL): Toggle the search form and navigation. After the interaction, the page remains the same implying the interface adjusts allowing users to search the site or navigate the website through the opened menu.
ACTION (android.view.View, NULL, (16, 365), click, NULL): The interaction is the click action on a view component titled "Accessing STEM in Higher Education". The view item is associated with an event to offer details about how high school students who are blind or low vision can visit the ICS and learn about college life upon clicking the view.
~~~
ACTION (android.view.View, "", (16, 504), click, NULL): Click to learn about high school students who are blind or low vision visit ICS and learn about college life. The next page retains the same content, but the focus moves to the section about the students' experiences.
~~~
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 146), click, NULL): Click to view the Image. The next page remains the same as the current page, indicating the image might have been opened in the same page or in a new layer overlaying the current page.
ACTION (android.widget.FrameLayout, acr.browser.lightning:id/arrow_button, (0, 26), click, NULL): Click to navigate to the previous page. The page after clicking this control is the tab management page, which presents options for creating a new tab, navigating forward, backward, or home.
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), click, NULL): Click to search or enter URL. After the operation, the page displays the search results or the contents of the URL entered.
ACTION (android.widget.ImageView, More options, (272, 30), click, NULL): Click to reveal further options. The next page contains a list of various options such as opening a new tab, sharing, accessing history, searching within the page, adjusting settings, etc.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 82), scroll, NULL): Scroll to interact with the UCI ICS website to reveal more elements.
ASSERT (android.view.View, UCI ICS logo, (16, 103), wait_until_element_presence, NULL): Verify that the UCI ICS logo is present, indicating that the website has been successfully loaded.
DONE
~~~
Based on your instructions, the UIAutomator2 code in Python should be:

```python
d(className="android.webkit.WebView", description="Home - UC Irvine Donald Bren School of Information & Computer Sciences").scroll(steps=10)
assert d(className="android.view.View", description="UCI ICS logo").wait(timeout=10)
```

In the code above, we first scroll the WebView element to reveal more elements on the UCI ICS website. Then we assert that the UCI ICS logo is present, which would indicate that the website has been successfully loaded.
````
### Success
````
ACTION (android.widget.Button, Search, (241, 374), click, NULL): Click on the 'Search' button to activate the search field., Exec_Fail
ACTION (android.widget.EditText, acr.browser.lightning:id/search, (58, 32), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the search field and press enter., Exec_Success

ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 82), scroll, NULL): Scroll to interact with the UCI ICS website to reveal more elements., Exec_Success
ASSERT (android.view.View, UCI ICS logo, (16, 103), wait_until_element_presence, NULL): Verify that the UCI ICS logo is present, indicating that the website has been successfully loaded., Exec_Success
DONE
````

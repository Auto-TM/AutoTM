## a14's b11 to a13

### Semantics of Source Test case
> This test case is testing the search functionality that tests navigation to a website and verifying the presence of a specific element.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (ImageButton, de.baumann.browser:id/floatButton_ok, (), click, NULL) : Click on the floating button to activate the search field.
> 2. ACTION (EditText, de.baumann.browser:id/main_omnibox_input, (), click, NULL) : Click on the search field to activate it for text input.
> 3. ACTION (EditText, de.baumann.browser:id/main_omnibox_input, (), input, "https://www.ics.uci.edu") : Input the URL 'https://www.ics.uci.edu' into the search field and press enter.
> 4. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to open the navigation drawer. The page after clicking this control is the navigation drawer page, which contains various controls such as Home, Back, Forward, History, Downloads, Domains, Settings, Guide, About, and Clear and Exit.
ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click to open the SSL certificate information page. The next page after clicking this control is the SSL certificate information page, which contains certificate details and a close button.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click to enter or edit the URL. The page after clicking this control retains the same structure but might redisplay based on the type of URL entered.
ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): Click to toggle JavaScript. After clicking, the state of JavaScript (enabled/disabled) for the current web page or application is toggled.
ACTION (android.widget.ImageView, More options, (280, 28), click, NULL): The 'More options' button provides various additional settings to be tailored to the user's preference. Clicking this button will take the user to a menu with options such as "Add Domain Settings", "First-party Cookies", "Third-party Cookies", "DOM Storage", "Clear Data", "Share" among other settings.
ACTION (android.webkit.WebView, NULL, (0, 80), scroll, NULL) : Scroll to interact with the DuckDuckGo search engine. The next page is still the DuckDuckGo search page where users can learn about DuckDuckGo, enter a search query, and click on the search button.
ACTION (android.view.View, NULL, (77, 192), click, NULL): Click to navigate to the About DuckDuckGo page. The next page contains information about DuckDuckGo and its privacy policy, with various clickable elements providing more details.
ACTION (android.widget.Button, N/A, (259, 362), click, NULL): Click to initiate the search query. The page after clicking this control is a search results page, which displays the results based on the entered search query in the EditText field.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click on the URL field to activate it for text input.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the URL field and press enter.
~~~
The following is the corresponding UIAutomator2 code in Python for your actions:

···
d.click(102, 29)
d(resourceId="com.stoutner.privacybrowser.standard:id/url_edittext").set_text("https://www.ics.uci.edu")
d.press('enter')
···
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, NULL, (0, 24), click, NULL): Click to open the navigation drawer. Opens up navigation options like Home, Back, Forward, History, Downloads, Domains, Settings, Guide, About, and Clear and Exit.
ACTION (android.widget.ImageView, com.stoutner.privacybrowser.standard:id/favorite_icon, (76, 39), click, NULL): Click the favorite icon to view the SSL certificate of the current website. The next page provides detailed information about the SSL certificate of the loaded domain.
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): The 'url_edittext' widget is designed to enable the user to enter URLs, for which the page shows the respective website once clicked. Evidently, it hasn't undergone a change in the subsequent page indicating that it might not have been interacted with.
ACTION (android.widget.TextView, com.stoutner.privacybrowser.standard:id/toggle_javascript, (230, 28), click, NULL): Click to toggle JavaScript settings. The page after clicking this control remains the same, indicating that the JavaScript setting has been toggled but does not navigate away from the current page.
ACTION (android.widget.ImageView, NULL, (280, 28), click, NULL): Click to view more options. The page after clicking this control is the options page, which contains various controls for adjusting the settings like cookies, display images, font size, etc.
ACTION (android.webkit.WebView, NULL, (0, 80), click, NULL): Click to visit the UC Irvine Donald Bren School of Information & Computer Sciences home page. The next page is an extended version of the ICS home page, containing a UCI ICS logo, site search form & navigation toggle, article about Accessing STEM in Higher Education, "Read More" button, and Accessibility Tools button.
~~~
ACTION (android.view.View, NULL, (16, 112), click, NULL): Click the UCI ICS logo to refresh the home page. The next page is same as current page i.e. "Home - UC Irvine Donald Bren School of Information & Computer Sciences".
~~~
ACTION (android.widget.Spinner, NULL, (264, 90), click, NULL): Click to toggle site navigation and search form. Even though the screen stays on the same page, toggling changes the view within the app, making features like site navigation and search form available for interaction.
ACTION (android.view.View, NULL, (16, 314), click, NULL): The action and its purpose is to click on the "Accessing STEM in Higher Education" section, which provides information about high school students who are blind or have low vision visiting ICS and learning about college life. After interacting with this element, the same page is displayed with the same widgets.
ACTION (android.view.View, NULL, (16, 452), click, NULL): Click to read about "High school students who are blind or low vision visit ICS & learn about college life.". The page after clicking this control remains the same, signifying no changes in page details or GUI elements upon this action.
ACTION (android.view.View, NULL, (16, 620), click, NULL): Click to read more about "Accessing STEM in Higher Education". The subsequent page is the detail information page of the article, which contains the full content of the article and share buttons.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 144), click, NULL): Clicking the image 'AccessSTEM_PeterGroup_portrait' provides more information about STEM. Navigating to the next page provides additional resources related to STEM in higher education.
ACTION (android.widget.Button, NULL, (268, 130), click, NULL): Click to access the Accessibility Tools. The page after clicking this control remains the same as no changes were mentioned in the Next Page JSON.

````

#### Selected Event(s) and Script
````
~~~
ASSERT (android.webkit.WebView, NULL, (0, 80), wait_until_element_presence, "UC Irvine Donald Bren School of Information & Computer Sciences"): Verify that the element 'UC Irvine Donald Bren School of Information & Computer Sciences' is present within 10 seconds.
DONE
~~~
Based on the given input, the corresponding UIAutomator2 code in Python would be:

```python
assert d.xpath('//android.webkit.WebView').wait(timeout=10.0).exists
```

This code will wait for 10 seconds to verify that the WebView element is present on the screen.
````
### Success
````
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), click, NULL): Click on the URL field to activate it for text input., Exec_Success
ACTION (android.widget.EditText, com.stoutner.privacybrowser.standard:id/url_edittext, (102, 29), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the URL field and press enter., Exec_Success

ASSERT (android.webkit.WebView, NULL, (0, 80), wait_until_element_presence, "UC Irvine Donald Bren School of Information & Computer Sciences"): Verify that the element 'UC Irvine Donald Bren School of Information & Computer Sciences' is present within 10 seconds., Exec_Success
DONE
````

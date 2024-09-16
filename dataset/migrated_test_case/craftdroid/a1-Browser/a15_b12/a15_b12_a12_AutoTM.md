## a15's b12 to a12

### Semantics of Source Test case
> This test case is testing the navigation functionality in the Mozilla Focus browser that tests skipping the initial screen, entering a URL, navigating to a different URL, and then returning to the previous page.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (Button, org.mozilla.focus:id/skip, (), click, NULL) : Click on the 'Skip' button to bypass the initial screen.
> 2. ACTION (EditText, org.mozilla.focus:id/urlView, (), click, NULL) : Click on the address bar to activate it for text input.
> 3. ACTION (EditText, org.mozilla.focus:id/urlView, (), input, "https://www.ics.uci.edu") : Input the URL 'https://www.ics.uci.edu' into the address bar and press enter.
> 4. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds.
> 5. ACTION (TextView, org.mozilla.focus:id/display_url, (), input, "https://uci.edu") : Input the URL 'https://uci.edu' into the address bar and press enter.
> 6. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc="UCI homepage"]") : Verify that the element with the content description 'UCI homepage' is present within 10 seconds.
> 7. RETURN: Press the back button to return to the previous page.
> 8. ASSERT (View, , (), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]") : Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.FrameLayout, com.android.browser:id/iconcombo, (8, 24), click, NULL): Click to view page information. The page after clicking this control is the Page Info page, which includes page title, address, and options to view certificate or confirm the information.
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), click, NULL): Click to enter a new web address or edit the existing one. The next page after clicking this will be the same page with the url text box selected for input.
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), long click, NULL): Long click to load the URL. The next page after this interaction shows a new loaded URL "https://www.google.com/webhp?client=ms-android-google&source=android-home" in this same EditText field.
ACTION (android.widget.ImageButton, com.android.browser:id/tab_switcher, (272, 24), click, NULL): Click to switch the page. The next page contains the page refresh option and tab management features including adding a new tab or bookmarking the current tab.
ACTION (android.webkit.WebView, Home - UC Irvine Donald Bren School of Information & Computer Sciences, (0, 76), scroll, NULL): Scroll on the webpage to view content. After scrolling, the user navigates to another website page, 'Browse all of Google's products and services - Google'.
ACTION (android.widget.Button, Accessibility Tools, (268, 126), click, NULL): Click to access Accessibility Tools. The next page after clicking this control is a sign-in page for Google Accounts.
ACTION (android.view.View, NULL, (16, 97), click, NULL): Click to navigate to the home page of UC Irvine Donald Bren School of Information & Computer Sciences. After clicking this control, the next page is the Home page with various clickable navigation drawers and a product support section.
ACTION (android.widget.Spinner, Toggle site search form & navigation, (264, 84), click, NULL): Click to toggle the site search form and navigation. The next page after clicking this control is a sign-in page for Google Accounts, which requires email or phone for signing in.
ACTION (android.view.View, NULL, (16, 312), click, NULL): Click to access the "Accessing STEM in Higher Education" section. The page after clicking this control is Google's homepage.
ACTION (android.view.View, NULL, (16, 451), click, NULL): The action opens a link about a program where high school students who are visually impaired can learn about college life. This action redirects the user to a Google homepage where they can perform further searches or actions.
ACTION (android.view.View, Read More, (16, 619), click, NULL): Click to read more about the Accessing STEM in Higher Education initiative. The next page navigates to Google main page, suggesting that a full search on the topic might be initiated.
ACTION (android.widget.Image, AccessSTEM_PeterGroup_portrait, (0, 140), click, NULL): Clicking this image takes the user to the Google homepage.

````

#### Selected Event(s) and Script
````
~~~
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), click, NULL): Click on the address bar to activate it for text input, similar to the 'Skip' button in the source application.
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the address bar and press enter, similar to the action in the source application.
ASSERT (android.view.View, NULL, (16, 97), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds, similar to the assertion in the source application.
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the address bar and press enter, similar to the action in the source application.
ASSERT (android.view.View, NULL, (16, 312), wait_until_element_presence, "xpath://android.view.View[@content-desc="UCI homepage"]"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds, similar to the assertion in the source application.
RETURN: Press the back button to return to the previous page, similar to the action in the source application.
ASSERT (android.view.View, NULL, (16, 97), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page, similar to the assertion in the source application.
DONE
~~~
### Output:

Based on the input actions, the corresponding UIAutomator2 code in Python is as follows:

···
d(resourceId="com.android.browser:id/url").click()
d(resourceId="com.android.browser:id/url").send_keys("https://www.ics.uci.edu")
d.press('enter')
assert d.xpath('//android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]').wait(timeout=10)
d(resourceId="com.android.browser:id/url").send_keys("https://uci.edu")
d.press('enter')
assert d.xpath('//android.view.View[@content-desc="UCI homepage"]').wait(timeout=10)
d.press('back')
assert d.xpath('//android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]').wait(timeout=10)
···
````
### Success
````
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), click, NULL): Click on the address bar to activate it for text input, similar to the 'Skip' button in the source application., Exec_Success
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), input, "https://www.ics.uci.edu"): Input the URL 'https://www.ics.uci.edu' into the address bar and press enter, similar to the action in the source application., Exec_Success
ASSERT (android.view.View, NULL, (16, 97), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds, similar to the assertion in the source application., Exec_Success
ACTION (android.widget.EditText, com.android.browser:id/url, (52, 24), input, "https://uci.edu"): Input the URL 'https://uci.edu' into the address bar and press enter, similar to the action in the source application., Exec_Success
ASSERT (android.view.View, NULL, (16, 312), wait_until_element_presence, "xpath://android.view.View[@content-desc="UCI homepage"]"): Verify that the element with the content description 'UCI homepage' is present within 10 seconds, similar to the assertion in the source application., Exec_Success
RETURN: Press the back button to return to the previous page, similar to the action in the source application., Exec_Success
ASSERT (android.view.View, NULL, (16, 97), wait_until_element_presence, "xpath://android.view.View[@content-desc="Donald Bren School of Information and Computer Sciences"]"): Verify that the element with the content description 'Donald Bren School of Information and Computer Sciences' is present within 10 seconds after returning to the previous page, similar to the assertion in the source application., Exec_Success
DONE
````

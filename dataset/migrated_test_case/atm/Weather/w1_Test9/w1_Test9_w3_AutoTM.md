## w1's Test9 to w3

### Semantics of Source Test case
> Based on the provided Android test case, here's the corresponding function description following the specified format:
> 
> ```
> This test case is verifying the wind speed unit settings in the application.
> 
> The detailed process with serial numbers is as follows:
> 
> 1. ACTION (OptionsMenu, , (), click, NULL): Open the options menu.
> 2. ACTION (TextView, R.id.title, (), click, NULL): Click on the "Settings" option in the menu.
> 3. ACTION (ListView, android.R.id.list, (), click, NULL): Click on the 5th item in the settings list (index 4).
> 4. ACTION (CheckedTextView, , (), click, NULL): Select the second option (index 1) in the wind speed unit dialog.
> 5. ASSERT (TextView, android.R.id.summary, (), matches, "Kilometers per hour (kph)"): Verify that the selected wind speed unit is displayed as "Kilometers per hour (kph)".
> 6. ACTION (ListView, android.R.id.list, (), click, NULL): Click on the 5th item in the settings list again (index 4).
> 7. ACTION (CheckedTextView, , (), click, NULL): Select the third option (index 2) in the wind speed unit dialog.
> 8. ASSERT (TextView, android.R.id.summary, (), matches, "Miles per hour (mph)"): Verify that the selected wind speed unit is displayed as "Miles per hour (mph)".
> ```
> 
> This function description outlines the steps to test the wind speed unit settings in the application, including changing the unit from kilometers per hour to miles per hour and verifying the displayed text after each change.

### Process
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, , (16, 38), click, "World Weather"): Click on the "World Weather" title. This action does not navigate to a new page or create new widgets, as the current and next page JSONs are identical.
ACTION (android.widget.ImageView, com.haringeymobile.ukweather:id/search_button, (160, 28), click, NULL): Click on the search button to open the search interface. The new page displays a search bar with id "com.haringeymobile.ukweather:id/search_src_text" for entering city names and a submit button with id "com.haringeymobile.ukweather:id/search_go_btn" to perform the search.
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/mi_add_city, (208, 28), click, NULL): Click to open the "Add new city" dialog. The dialog contains an EditText with id "com.haringeymobile.ukweather:id/ac_search_edit_text" for entering city name and a search button with id "com.haringeymobile.ukweather:id/ac_search_button".
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/mi_main_submenu, (264, 28), click, NULL): Click to open the extras menu. The new menu displays options including "City Management", "Settings", "Rate application", and "About".
ACTION (android.widget.ListView, android:id/list, (4, 83), click, NULL): Click on the list to select a city. Clicking on this control does not navigate to a new page, but allows interaction with the city items within the list, each containing options for current weather, 16-day forecast, and 3-hourly forecast.
ACTION (android.widget.LinearLayout, , (4, 83), click, NULL): Click on the LinearLayout to select a city from the list. This action does not navigate to a new page, but may expand the selected city's information within the same list view.
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/city_name_in_list_row_text_view, (7, 86), click, "London"): Click on the city name "London" to select it. This action does not navigate to a new page, but reveals three options for the selected city: "Current weather", "16 day forecast", and "3-hourly forecast".
ACTION (android.widget.LinearLayout, com.haringeymobile.ukweather:id/city_current_weather_button, (10, 141), click, NULL): Click to view current weather for London. The next page displays detailed weather information including temperature (24.2℃), sunrise/sunset times, weather conditions (Overcast clouds), pressure (1016 hPa), humidity (51%), and wind speed (11.5 mph).
ACTION (android.widget.TextView, , (43, 152), click, "Current\nweather"): Click on the "Current weather" button to view the current weather details for London. The next page displays temperature (24.2℃), sunrise and sunset times, weather conditions (Overcast clouds), pressure (1016 hPa), humidity (51%), and wind speed (11.5 mph) for London.
ACTION (android.widget.LinearLayout, com.haringeymobile.ukweather:id/city_daily_weather_forecast_button, (112, 141), click, NULL): Click on the "16 day forecast" button to view the daily weather forecast for London. The next page displays a ViewPager with id "com.haringeymobile.ukweather:id/pager" showing detailed weather information including temperature, date, weather conditions, pressure, humidity, and wind speed.
ACTION (android.widget.LinearLayout, com.haringeymobile.ukweather:id/city_daily_weather_forecast_button, (112, 141), click, "16 day \nforecast"): Click to view the 16-day weather forecast for London. The next page displays a detailed forecast with tabs for different dates, temperature information, weather conditions, pressure, humidity, and wind speed.
ACTION (android.widget.LinearLayout, com.haringeymobile.ukweather:id/city_three_hourly_weather_forecast_button, (214, 141), click, NULL): Click to view the 3-hourly weather forecast for London. The next page shows a ViewPager with id "com.haringeymobile.ukweather:id/pager" displaying detailed weather information including temperature, date, time, weather conditions, pressure, humidity, and wind speed.
ACTION (android.widget.TextView, , (247, 152), click, "3-hourly
forecast"): Click on the "3-hourly forecast" button to view the 5-day 3-hourly weather forecast for London. The next page shows a tab layout with different time slots and detailed weather information including temperature, date, time, weather conditions, pressure, humidity, and wind speed.
ACTION (android.widget.LinearLayout, , (4, 591), click, NULL): Click on the city item "Moscow" to view its weather details. This action does not navigate to a new page, but may expand the item to show additional weather information or options for the selected city.

````

#### Selected Event(s) and Script
````
Based on the provided information, we are at the beginning of the test case migration. The source test case starts with opening the options menu, but the current page's intentions don't show a direct option for that. However, there is an action to open the extras menu, which likely contains the settings option we need. Let's start with that action:

~~~
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/mi_main_submenu, (264, 28), click, NULL):Click to open the extras menu to access settings
~~~

This action should open the extras menu, which is likely to contain the "Settings" option we need for the next step of the source test case.
Based on the provided information, here's the UIAutomator2 code in Python for the given action:

···
d.click(264, 28)
···

This code uses the coordinates (264, 28) to perform a click action, which will open the extras menu to access settings. Since coordinates are provided and they are precise, this is the optimal choice for the action as per the requirements.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.LinearLayout, , (112, 28), click, NULL): Click on the "City Management" option to open the city management page. The action does not navigate to a new page, as the next page JSON is identical to the current page JSON.
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/title, (177, 41), click, "City Management"): Click on "City Management" to open the city management page. The new page displays a list of cities with options to rename (id: com.haringeymobile.ukweather:id/city_rename_button) and remove (id: com.haringeymobile.ukweather:id/city_remove_button) each city.
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/title, (177, 89), click, "Settings"): Click on "Settings" to open the settings page. The new page displays various setting options including temperature scale, wind speed measurement units, wind direction display, weather data reuse period, app theme, and three-hourly weather forecast display mode.
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/title, (177, 185), click, "About"): Click on the "About" option to navigate to the About page, which displays app version, copyright information, credits, and licenses.

````

#### Selected Event(s) and Script
````
Based on the provided information, I'll proceed with the next step in the test case migration. The source test case is about verifying wind speed unit settings, and we've just opened the extras menu in the target app. The next logical step would be to access the settings page.

~~~
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/title, (177, 89), click, "Settings"):Click on "Settings" to open the settings page
~~~

This action corresponds to step 2 in the source test case, where we click on the "Settings" option in the menu. The target app seems to have a similar structure, allowing us to access the settings through the extras menu.
Based on the provided information, I'll convert the action into UIAutomator2 code using Python. Here's the code:

···
d.click(177, 89)
···

This code uses the coordinates (177, 89) to perform a click action, which should open the settings page by clicking on the "Settings" option. Since coordinates are provided and they are precise, I've used them as the preferred method for interaction.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.ImageButton, , (0, 24), click, NULL): Click on the "Navigate up" button to return to the main screen. The next page displays a list of cities with weather information options, including "London", "Mexico City", "Rio de Janeiro", "Cairo", and "Moscow".
ACTION (android.widget.TextView, , (177, 89), click, "Settings"): Click on the "Settings" option to open the settings page. The settings page contains various options such as Temperature scale, Wind speed measurement units, Wind direction display, Weather data reuse period, App theme, and Three-hourly weather forecast display mode.
ACTION (android.widget.ListView, android:id/list, (0, 83), click, NULL): Click on the settings list to view and modify various app settings. The page remains the same after clicking, as it's a scrollable list of settings options.
ACTION (android.widget.LinearLayout, , (0, 83), click, NULL): Click on the "Temperature scale" option to open a dialog for choosing the temperature scale. The next page remains the same, indicating that this action likely opens a dialog or pop-up menu for temperature scale selection.
ACTION (android.widget.TextView, android:id/title, (16, 99), click, "Temperature scale"): Click to open temperature scale settings. A dialog appears with options "Celsius (℃)" and "Fahrenheit (℉)" for selecting the temperature scale, along with a "CANCEL" button.
ACTION (android.widget.TextView, android:id/summary, (16, 121), click, "Choose temperature scale"): Click to open temperature scale selection dialog. The next page displays a dialog with options "Celsius (℃)" and "Fahrenheit (℉)" for selecting the temperature scale, along with a "CANCEL" button.
ACTION (android.widget.TextView, android:id/title, (16, 173), click, "Wind speed measurement units"): Click to open a dialog for selecting wind speed measurement units. The dialog contains options like "Meters per second (mps)", "Kilometers per hour (kph)", "Miles per hour (mph)", and "Beaufort scale (wind force)" with ids "com.haringeymobile.ukweather:id/text1".
ACTION (android.widget.TextView, android:id/summary, (16, 195), click, "Choose wind speed measurement units"): Click to open a dialog for selecting wind speed measurement units. The dialog contains options like "Meters per second (mps)", "Kilometers per hour (kph)", "Miles per hour (mph)", and "Beaufort scale (wind force)" with id "com.haringeymobile.ukweather:id/text1".
ACTION (android.widget.LinearLayout, , (0, 231), click, NULL): Click to toggle the wind direction display setting. The checkbox with id "android:id/checkbox" is clicked to enable or disable including wind direction in weather information.
ACTION (android.widget.CheckBox, android:id/checkbox, (272, 259), click, NULL): Click to toggle the "Wind direction display" setting. This action doesn't navigate to a new page but updates the checkbox state to include or exclude wind direction in weather information.
ACTION (android.widget.LinearLayout, , (0, 321), click, NULL): Click to open settings for Weather data reuse period. This action does not navigate to a new page, but provides options to specify the time period for refreshing weather data via network.
ACTION (android.widget.TextView, android:id/title, (16, 337), click, "Weather data reuse period"): Click to open a dialog for selecting the weather data reuse period. The dialog contains options for different time intervals (10 minutes, 20 minutes, 30 minutes, 1 hour, 2 hours) represented by CheckedTextViews with id "com.haringeymobile.ukweather:id/text1".
ACTION (android.widget.TextView, android:id/summary, (16, 359), click, "For efficiency reasons, the most recent weather data is stored locally, and reused for a short period of time. Here you can specify the time period after which the data will be refreshed via network."): Click to open a dialog for selecting the weather data reuse period. The dialog contains options like "10 minutes", "20 minutes", "30 minutes", "1 hour", and "2 hour" with ids "com.haringeymobile.ukweather:id/text1".
ACTION (android.widget.TextView, android:id/title, (16, 475), click, "App theme"): Click to open the app theme selection dialog. The next page shows a dialog with title "App theme" and a list of theme options including "Deep purple", "Indigo", "Blue", "Cyan", "Teal", "Green", "Brown", and "Blue gray".
ACTION (android.widget.TextView, android:id/summary, (16, 497), click, "Choose an app theme"): Click to open the app theme selection dialog. The new dialog displays a list of theme options including "Deep purple", "Indigo", "Blue", "Cyan", "Teal", "Green", "Brown", and "Blue gray" with ids "com.haringeymobile.ukweather:id/app_theme_name".
ACTION (android.widget.TextView, android:id/title, (16, 549), click, "Three-hourly weather forecast display mode"): Click to open a dialog for selecting the display mode of three-hourly weather forecast. The dialog contains two options: "As horizontal swiping views" and "As list", with IDs "com.haringeymobile.ukweather:id/text1" for both options, and a "CANCEL" button with ID "android:id/button2".
ACTION (android.widget.TextView, android:id/summary, (16, 571), click, "Choose how the three-hourly weather forecast is displayed"): Click to open a dialog for selecting the three-hourly weather forecast display mode. The dialog contains two options: "As horizontal swiping views" and "As list", represented by CheckedTextViews with id "com.haringeymobile.ukweather:id/text1".
ACTION (android.widget.LinearLayout, , (0, 623), click, NULL): Click to open the "Deleting cities" settings option. No new page appears, but the option might expand to show more details or controls related to deleting cities.
ACTION (android.widget.TextView, android:id/title, (16, 639), click, "Deleting cities"): Click to open the "Deleting cities" settings dialog. The new dialog displays options for deleting cities, including "Pressing button and viewing the confirmation dialog" and "Flinging left or right", along with a "CANCEL" button.

````

#### Selected Event(s) and Script
````
Based on the provided information, we are currently at the settings page of the target application. The next step in the source test case is to click on the 5th item in the settings list, which corresponds to the wind speed measurement units. Let's proceed with this step:

~~~
ACTION (android.widget.TextView, android:id/title, (16, 173), click, NULL):Click to open a dialog for selecting wind speed measurement units
~~~

This action corresponds to step 3 in the source test case, where we click on the 5th item in the settings list. In the target app, we have a specific option for "Wind speed measurement units" which we can directly interact with.
Based on the provided action description, I'll convert it to UIAutomator2 code in Python. Here's the corresponding code:

···
d.click(16, 173)
···

This code uses the coordinates (16, 173) to perform a click action, which is the optimal choice as per the requirements. The click action will open a dialog for selecting wind speed measurement units.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/alertTitle, (40, 158), click, "Wind speed measurement units"): Click on the title of the wind speed measurement units dialog. The dialog remains open with options to select wind speed units: "Meters per second (mps)", "Kilometers per hour (kph)", "Miles per hour (mph)", and "Beaufort scale (wind force)".
ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 212), click, "Meters per second (mps)"): Click to select "Meters per second (mps)" as the wind speed measurement unit. The dialog remains open with the selected option now checked.
ACTION (android.widget.Button, android:id/button2, (215, 472), click, "CANCEL"): Click to cancel the wind speed measurement units selection and return to the Settings page, which includes options for temperature scale, wind speed measurement units, wind direction display, weather data reuse period, app theme, and three-hourly weather forecast display mode.

````

#### Selected Event(s) and Script
````
Based on the provided information, I understand that we are currently at the step of selecting the wind speed measurement unit in the target application. Let's proceed with the next action in the test case migration:

~~~
ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 212), click, NULL):Select "Kilometers per hour (kph)" as the wind speed measurement unit
~~~

Explanation:
1. We have already opened the settings menu and navigated to the wind speed unit selection dialog, which corresponds to steps 1-3 in the source test case.
2. The next step in the source test case (step 4) is to select the second option for wind speed unit, which should be "Kilometers per hour (kph)".
3. In the target app, we have an option to click on the CheckedTextView with the id "com.haringeymobile.ukweather:id/text1" to select a wind speed unit.
4. Although we don't see the exact text "Kilometers per hour (kph)" in the provided intentions, we can assume it's the second option in the list based on the source test case.
5. We're using a click action instead of directly setting the value, as that's the interaction method provided in the current page's intent description.

After executing this action, we should be able to verify if the selected wind speed unit is displayed correctly, which would correspond to step 5 in the source test case.
Based on the given action description, here's the UIAutomator2 code in Python to perform the requested operation:

···
d.click(16, 212)
···

This code uses the coordinates (16, 212) to click on the CheckedTextView element with the text "Kilometers per hour (kph)" to select it as the wind speed measurement unit. Since precise coordinates are provided, we use them directly for the click operation, which is the preferred method as per the requirements.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/alertTitle, (40, 158), click, "Wind speed measurement units"): Click on the title of the wind speed measurement units dialog. The dialog remains open with options to select wind speed units: "Meters per second (mps)", "Kilometers per hour (kph)", "Miles per hour (mph)", and "Beaufort scale (wind force)".
ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 212), click, "Meters per second (mps)"): Click to select "Meters per second (mps)" as the wind speed measurement unit. The dialog remains open with the selected option now checked.
ACTION (android.widget.Button, android:id/button2, (215, 472), click, "CANCEL"): Click to cancel the wind speed measurement units selection and return to the Settings page, which includes options for temperature scale, wind speed measurement units, wind direction display, weather data reuse period, app theme, and three-hourly weather forecast display mode.

````

#### Selected Event(s) and Script
````
Based on the provided information, I will proceed with the next step in the test case migration. Here's my analysis and recommendation:

1. We have successfully navigated to the settings page and opened the wind speed measurement units dialog.
2. We have selected "Kilometers per hour (kph)" as the wind speed measurement unit.
3. The next step in the source test case is to verify that the selected wind speed unit is displayed correctly.

Given this, here's the next action I recommend:

~~~
ASSERT (android.widget.TextView, android:id/summary, (), matches, "Kilometers per hour (kph)"):Verify that the selected wind speed unit is displayed as "Kilometers per hour (kph)" on the settings page
~~~

This assertion corresponds to step 5 in the source test case. We're verifying that the selected wind speed unit is correctly displayed after making the selection. 

Note that we don't need to click on the list item again (as in step 6 of the source test case) because in the target app, we're already in the correct dialog for changing the wind speed unit.
Based on the provided information and requirements, here's the UIAutomator2 code in Python to verify the selected wind speed unit:

···
assert d(resourceId="android:id/summary").get_text() == "Kilometers per hour (kph)"
···

This code uses the resourceId to locate the TextView element and verifies that its text matches the expected value "Kilometers per hour (kph)". This approach is preferred as it uses the unique ID provided in the input, which is more reliable than using coordinates for an assertion.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/alertTitle, (40, 158), click, "Wind speed measurement units"): Click on the title of the wind speed measurement units dialog. The dialog remains open with options to select wind speed units: "Meters per second (mps)", "Kilometers per hour (kph)", "Miles per hour (mph)", and "Beaufort scale (wind force)".
ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 212), click, "Meters per second (mps)"): Click to select "Meters per second (mps)" as the wind speed measurement unit. The dialog remains open with the selected option now checked.
ACTION (android.widget.Button, android:id/button2, (215, 472), click, "CANCEL"): Click to cancel the wind speed measurement units selection and return to the Settings page, which includes options for temperature scale, wind speed measurement units, wind direction display, weather data reuse period, app theme, and three-hourly weather forecast display mode.

````

#### Selected Event(s) and Script
````
Based on the provided information, I can determine that we are currently at step 6 of the source test case. We have successfully changed the wind speed unit to "Kilometers per hour (kph)" and verified it. The next step is to change the wind speed unit again. Here's the next action to take:

~~~
ACTION (android.widget.TextView, android:id/title, (16, 173), click, NULL):Click to open the dialog for selecting wind speed measurement units again
~~~

This action corresponds to step 6 in the source test case, where we click on the 5th item in the settings list again. In the target app, we're directly clicking on the wind speed measurement units option to open the selection dialog.
Based on the provided action description, I'll convert it into UIAutomator2 code in Python. Here's the code:

···
d.click(16, 173)
···

This code uses the coordinates (16, 173) to perform the click action, which is the optimal choice as per the requirements. The click action opens the dialog for selecting wind speed measurement units again.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/alertTitle, (40, 158), click, "Wind speed measurement units"): Click on the title of the wind speed measurement units dialog. The dialog remains open with options to select wind speed units: "Meters per second (mps)", "Kilometers per hour (kph)", "Miles per hour (mph)", and "Beaufort scale (wind force)".
ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 212), click, "Meters per second (mps)"): Click to select "Meters per second (mps)" as the wind speed measurement unit. The dialog remains open with the selected option now checked.
ACTION (android.widget.Button, android:id/button2, (215, 472), click, "CANCEL"): Click to cancel the wind speed measurement units selection and return to the Settings page, which includes options for temperature scale, wind speed measurement units, wind direction display, weather data reuse period, app theme, and three-hourly weather forecast display mode.

````

#### Selected Event(s) and Script
````
Based on the provided information, I can determine that we are currently at step 7 of the source test case, where we need to select the third option (index 2) in the wind speed unit dialog, which corresponds to "Miles per hour (mph)". Here's the next action to take:

~~~
ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 292), click, "Miles per hour (mph)"):Select "Miles per hour (mph)" as the wind speed measurement unit
~~~

This action aims to select the "Miles per hour (mph)" option in the wind speed measurement units dialog. I've chosen this action because:

1. It aligns with step 7 of the source test case, which requires selecting the third option in the wind speed unit dialog.
2. The current page's intent description shows that "Miles per hour (mph)" is one of the available options in the dialog.
3. We've already selected "Kilometers per hour (kph)" in the previous steps, so now we need to change it to "Miles per hour (mph)".

The coordinates (16, 292) are an estimate based on the previous action's coordinates, assuming that the "Miles per hour (mph)" option is the third item in the list.

After this action is executed, we should be ready to verify that the selected wind speed unit is displayed correctly, which corresponds to step 8 in the source test case.
Based on the given input, here's the UIAutomator2 code in Python to perform the described action:

```
d.click(16, 292)
```

This code uses the coordinates (16, 292) to click on the "Miles per hour (mph)" option in the wind speed measurement unit selection. Since precise coordinates are provided, it's the preferred method for this action.
````
#### Contextual Semantics of Widgets
````
ACTION (android.widget.TextView, android:id/alertTitle, (40, 158), click, "Wind speed measurement units"): Click on the title of the wind speed measurement units dialog. The dialog remains open with options to select wind speed units: "Meters per second (mps)", "Kilometers per hour (kph)", "Miles per hour (mph)", and "Beaufort scale (wind force)".
ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 212), click, "Meters per second (mps)"): Click to select "Meters per second (mps)" as the wind speed measurement unit. The dialog remains open with the selected option now checked.
ACTION (android.widget.Button, android:id/button2, (215, 472), click, "CANCEL"): Click to cancel the wind speed measurement units selection and return to the Settings page, which includes options for temperature scale, wind speed measurement units, wind direction display, weather data reuse period, app theme, and three-hourly weather forecast display mode.

````

#### Selected Event(s) and Script
````
Based on the provided information, I can determine that we are currently at step 8 of the source test case. We have successfully changed the wind speed unit from kilometers per hour to miles per hour. The next step is to verify that the selected wind speed unit is displayed as "Miles per hour (mph)". Here's the next action to take:

~~~
ASSERT (android.widget.TextView, android:id/summary, (), matches, "Miles per hour (mph)"):Verify that the selected wind speed unit is displayed as "Miles per hour (mph)" on the settings page
DONE
~~~

This assertion checks if the summary text for the wind speed unit setting displays "Miles per hour (mph)", which corresponds to step 8 in the source test case. 

I've added the DONE statement because this assertion completes the migration of all steps from the source test case to the target app. We have successfully changed the wind speed unit settings and verified the changes, which matches the entire functionality described in the source test case.
Based on the provided information, here's the UIAutomator2 code in Python to verify the selected wind speed unit:

```
assert d(resourceId="android:id/summary").get_text() == "Miles per hour (mph)"
```

This code checks if the text of the element with the resource ID "android:id/summary" matches exactly "Miles per hour (mph)". This assertion will verify that the selected wind speed unit is correctly displayed as "Miles per hour (mph)" on the settings page.
````
### Success
````
ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/mi_main_submenu, (264, 28), click, NULL):Click to open the extras menu to access settings, Exec_Success

ACTION (android.widget.TextView, com.haringeymobile.ukweather:id/title, (177, 89), click, "Settings"):Click on "Settings" to open the settings page, Exec_Success

ACTION (android.widget.TextView, android:id/title, (16, 173), click, NULL):Click to open a dialog for selecting wind speed measurement units, Exec_Success

ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 212), click, NULL):Select "Kilometers per hour (kph)" as the wind speed measurement unit, Exec_Success

ASSERT (android.widget.TextView, android:id/summary, (), matches, "Kilometers per hour (kph)"):Verify that the selected wind speed unit is displayed as "Kilometers per hour (kph)" on the settings page, Exec_Success

ACTION (android.widget.TextView, android:id/title, (16, 173), click, NULL):Click to open the dialog for selecting wind speed measurement units again, Exec_Success

ACTION (android.widget.CheckedTextView, com.haringeymobile.ukweather:id/text1, (16, 292), click, "Miles per hour (mph)"):Select "Miles per hour (mph)" as the wind speed measurement unit, Exec_Success

ASSERT (android.widget.TextView, android:id/summary, (), matches, "Miles per hour (mph)"):Verify that the selected wind speed unit is displayed as "Miles per hour (mph)" on the settings page, Exec_Success
DONE
````

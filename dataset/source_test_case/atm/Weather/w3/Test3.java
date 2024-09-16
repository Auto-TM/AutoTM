package com.haringeymobile.ukweather;


import android.support.test.espresso.ViewInteraction;
import android.support.test.rule.ActivityTestRule;
import android.support.test.runner.AndroidJUnit4;
import android.test.suitebuilder.annotation.LargeTest;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewParent;

import org.hamcrest.Description;
import org.hamcrest.Matcher;
import org.hamcrest.TypeSafeMatcher;
import org.hamcrest.core.IsInstanceOf;
import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import static android.support.test.espresso.Espresso.onData;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.scrollTo;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withContentDescription;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.CoreMatchers.anything;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.is;

@LargeTest
@RunWith(AndroidJUnit4.class)
public class WorldWeatherTest3 {

    @Rule
    public ActivityTestRule<MainActivity> mActivityTestRule = new ActivityTestRule<>(MainActivity.class);

    @Test
    public void worldWeatherTest3() {
        ViewInteraction actionMenuItemView = onView(
                allOf(withId(R.id.mi_main_submenu), withContentDescription("Extras"),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.general_toolbar),
                                        1),
                                2),
                        isDisplayed()));
        actionMenuItemView.perform(click());

        ViewInteraction appCompatTextView = onView(
                allOf(withId(R.id.title), withText("City Management"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.support.v7.view.menu.ListMenuItemView")),
                                        1),
                                0),
                        isDisplayed()));
        appCompatTextView.perform(click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        ViewInteraction appCompatButton = onView(
                allOf(withId(android.R.id.button1), withText("OK"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.ScrollView")),
                                        0),
                                3)));
        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(0)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(1)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(1)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        onData(anything())
                .inAdapterView(withId(R.id.city_list_container))
                .atPosition(1)
                .onChildView(withId(R.id.city_remove_button))
                .perform(click());

        appCompatButton.perform(scrollTo(), click());

        ViewInteraction textView = onView(
                allOf(withId(R.id.city_name_in_list_row_text_view), withText("Los Angeles"),
                        childAtPosition(
                                childAtPosition(
                                        IsInstanceOf.<View>instanceOf(android.view.ViewGroup.class),
                                        0),
                                1),
                        isDisplayed()));
        textView.check(matches(withText("Los Angeles")));

    }

    private static Matcher<View> childAtPosition(
            final Matcher<View> parentMatcher, final int position) {

        return new TypeSafeMatcher<View>() {
            @Override
            public void describeTo(Description description) {
                description.appendText("Child at position " + position + " in parent ");
                parentMatcher.describeTo(description);
            }

            @Override
            public boolean matchesSafely(View view) {
                ViewParent parent = view.getParent();
                return parent instanceof ViewGroup && parentMatcher.matches(parent)
                        && view.equals(((ViewGroup) parent).getChildAt(position));
            }
        };
    }
}

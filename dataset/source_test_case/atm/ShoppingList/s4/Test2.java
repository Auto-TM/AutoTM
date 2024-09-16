package org.openintents.shopping;


import android.support.test.espresso.DataInteraction;
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
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.action.ViewActions.scrollTo;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.is;

@LargeTest
@RunWith(AndroidJUnit4.class)
public class ShoppingListTest2 {

    @Rule
    public ActivityTestRule<ShoppingActivity> mActivityTestRule = new ActivityTestRule<>(ShoppingActivity.class);

    @Test
    public void shoppingListTest2() {
        ViewInteraction spinner = onView(
                allOf(withId(R.id.spinner_listfilter),
                        childAtPosition(
                                allOf(withId(R.id.filters),
                                        childAtPosition(
                                                withId(R.id.background),
                                                0)),
                                0),
                        isDisplayed()));
        spinner.perform(click());

        DataInteraction checkedTextView = onData(anything())
                .inAdapterView(childAtPosition(
                        withClassName(is("android.widget.PopupWindow$PopupBackgroundView")),
                        0))
                .atPosition(0);
        checkedTextView.perform(click());

        ViewInteraction textView = onView(
                allOf(withId(R.id.name), withText("item2"),
                        childAtPosition(
                                allOf(withId(R.id.description),
                                        childAtPosition(
                                                withClassName(is("android.widget.LinearLayout")),
                                                1)),
                                4),
                        isDisplayed()));
        textView.perform(click());

        ViewInteraction editText = onView(
                allOf(withId(R.id.editquantity),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.quantity_and_price),
                                        0),
                                1)));
        editText.perform(replaceText("3"), closeSoftKeyboard());

        ViewInteraction editText2 = onView(
                allOf(withId(R.id.editprice),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.quantity_and_price),
                                        2),
                                1)));
        editText2.perform(replaceText("2.37"), closeSoftKeyboard());

        ViewInteraction button3 = onView(
                allOf(withId(android.R.id.button1), withText("OK"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.ScrollView")),
                                        0),
                                3)));
        button3.perform(click());

        ViewInteraction textView3 = onView(
                allOf(withId(R.id.quantity), withText("3 ")));
        textView3.check(matches(isDisplayed()));

        ViewInteraction textView5 = onView(
                allOf(withId(R.id.price), withText("7.11")));
        textView5.check(matches(isDisplayed()));
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

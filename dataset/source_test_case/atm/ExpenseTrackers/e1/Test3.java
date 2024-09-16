package com.benoitletondor.easybudgetapp.view;


import android.support.test.espresso.ViewInteraction;
import android.support.test.rule.ActivityTestRule;
import android.support.test.runner.AndroidJUnit4;
import android.test.suitebuilder.annotation.LargeTest;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewParent;

import com.benoitletondor.easybudgetapp.R;

import org.hamcrest.Description;
import org.hamcrest.Matcher;
import org.hamcrest.TypeSafeMatcher;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withParent;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.is;

@LargeTest
@RunWith(AndroidJUnit4.class)
public class EasyBudgetTest3 {

    @Rule
    public ActivityTestRule<MainActivity> mActivityTestRule = new ActivityTestRule<>(MainActivity.class);

    @Test
    public void easyBudgetTest3() {
        ViewInteraction viewInteraction = onView(
                allOf(withId(R.id.fab_expand_menu_button),
                        childAtPosition(
                                allOf(withId(R.id.fab_choices),
                                        childAtPosition(
                                                withId(R.id.coordinatorLayout),
                                                0)),
                                2),
                        isDisplayed()));
        viewInteraction.perform(click());

        ViewInteraction addFloatingActionButton = onView(
                allOf(withId(R.id.fab_new_expense),
                        childAtPosition(
                                allOf(withId(R.id.fab_choices),
                                        childAtPosition(
                                                withId(R.id.coordinatorLayout),
                                                0)),
                                1),
                        isDisplayed()));
        addFloatingActionButton.perform(click());

        ViewInteraction textInputEditText = onView(
                allOf(withId(R.id.description_edittext),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.description_inputlayout),
                                        0),
                                0),
                        isDisplayed()));
        textInputEditText.perform(replaceText("Entertainment"), closeSoftKeyboard());

        ViewInteraction textInputEditText1 = onView(
                allOf(withId(R.id.amount_edittext),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.amount_inputlayout),
                                        0),
                                0),
                        isDisplayed()));
        textInputEditText1.perform(replaceText("45"), closeSoftKeyboard());

        ViewInteraction appCompatButton4 = onView(withId(R.id.date_button));
        appCompatButton4.perform(click());

        ViewInteraction appCompatButton5 = onView(
                allOf(withId(android.R.id.button1), withText("OK"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.ScrollView")),
                                        0),
                                3)));
        appCompatButton5.perform(click());

        ViewInteraction floatingActionButton = onView(
                allOf(withId(R.id.save_expense_fab),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.ScrollView")),
                                        0),
                                1)));
        floatingActionButton.perform(click());

        ViewInteraction textView1 = onView(
                allOf(withId(R.id.grid_cell_tv2), withText("-45"),
                        isDisplayed()));
        textView1.check(matches(withText("-45")));

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

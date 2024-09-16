package me.writeily;


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

import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.action.ViewActions.scrollTo;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withContentDescription;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.is;

@LargeTest
@RunWith(AndroidJUnit4.class)
public class WriteilyTest9 {

    @Rule
    public ActivityTestRule<PromptPinActivity> mActivityTestRule = new ActivityTestRule<>(PromptPinActivity.class);

    @Test
    public void writeilyTest9() {
        ViewInteraction viewInteraction2 = onView(
                allOf(withId(R.id.fab_expand_menu_button),
                        childAtPosition(
                                allOf(withId(R.id.fab),
                                        childAtPosition(
                                                withClassName(is("android.widget.RelativeLayout")),
                                                3)),
                                2),
                        isDisplayed()));
        viewInteraction2.perform(click());

        ViewInteraction floatingActionButton2 = onView(
                allOf(withId(R.id.create_note),
                        childAtPosition(
                                allOf(withId(R.id.fab),
                                        childAtPosition(
                                                withClassName(is("android.widget.RelativeLayout")),
                                                3)),
                                0),
                        isDisplayed()));
        floatingActionButton2.perform(click());

        ViewInteraction appCompatTextView = onView(
                allOf(withId(R.id.keyboard_shortcut), withText("*"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                0)));
        appCompatTextView.perform(click());

        ViewInteraction appCompatTextView2 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText("-"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                1)));
        appCompatTextView2.perform(click());

        ViewInteraction appCompatTextView3 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText("_"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                2)));
        appCompatTextView3.perform(click());

        ViewInteraction appCompatTextView4 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText("#"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                3)));
        appCompatTextView4.perform(click());

        ViewInteraction appCompatTextView5 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText("!"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                4)));
        appCompatTextView5.perform(click());

        ViewInteraction appCompatTextView6 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText(":"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                5)));
        appCompatTextView6.perform(click());

        ViewInteraction appCompatTextView7 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText(">"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                6)));
        appCompatTextView7.perform(click());

        ViewInteraction appCompatTextView8 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText("("),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                7)));
        appCompatTextView8.perform(click());

        ViewInteraction appCompatTextView9 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText(")"),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                8)));
        appCompatTextView9.perform(click());

        ViewInteraction appCompatTextView10 = onView(
                allOf(withId(R.id.keyboard_shortcut), withText("["),
                        childAtPosition(
                                allOf(withId(R.id.keyboard_bar),
                                        childAtPosition(
                                                withId(R.id.keyboard_bar_scroll),
                                                0)),
                                9)));
        appCompatTextView10.perform(click());

        ViewInteraction appCompatImageButton = onView(
                allOf(withContentDescription("Navigate up"),
                        isDisplayed()));
        appCompatImageButton.perform(click());

        ViewInteraction textView = onView(
                allOf(withId(R.id.note_title), withText("-_#!()[")));
        textView.check(matches(withText("-_#!()[")));

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

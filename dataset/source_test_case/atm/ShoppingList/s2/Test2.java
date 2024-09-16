package br.com.vansact;


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

import br.com.activity.R;

import static android.support.test.espresso.Espresso.onData;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.longClick;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withContentDescription;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.is;

@LargeTest
@RunWith(AndroidJUnit4.class)
public class ShoppingListTest2 {

    @Rule
    public ActivityTestRule<MainApp> mActivityTestRule = new ActivityTestRule(MainApp.class);

    @Test
    public void shoppingListTest2() {
        onData(anything()).inAdapterView(withId(R.id.lvShoppingList)).
                atPosition(0).onChildView(withId(R.id.nameShoppingList)).perform(longClick());

        DataInteraction linearLayout2 = onData(anything())
                .inAdapterView(childAtPosition(
                        withId(android.R.id.content),
                        0))
                .atPosition(3);
        linearLayout2.perform(click());

        ViewInteraction button2 = onView(
                allOf(withId(R.id.schedule_notificatin_cancel), withText("Cancel"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.LinearLayout")),
                                        3),
                                0),
                        isDisplayed()));
        button2.perform(click());

        ViewInteraction textView = onView(
                allOf(withId(R.id.nameShoppingList), withText("list"),
                        isDisplayed()));
        textView.check(matches(withText("list")));

        onData(anything()).inAdapterView(withId(R.id.lvShoppingList)).
                atPosition(0).onChildView(withId(R.id.nameShoppingList)).perform(longClick());

        DataInteraction linearLayout3 = onData(anything())
                .inAdapterView(childAtPosition(
                        withId(android.R.id.content),
                        0))
                .atPosition(3);
        linearLayout3.perform(click());

        ViewInteraction button3 = onView(
                allOf(withId(R.id.schedule_notificatin_schedule), withText("Schedule"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.LinearLayout")),
                                        3),
                                2),
                        isDisplayed()));
        button3.perform(click());

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

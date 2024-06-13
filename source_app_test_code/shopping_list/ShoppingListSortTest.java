package org.openintents.shopping;


import static android.support.test.InstrumentationRegistry.getInstrumentation;
import static android.support.test.espresso.Espresso.onData;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.Espresso.openActionBarOverflowOrOptionsMenu;
import static android.support.test.espresso.Espresso.pressBack;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.longClick;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.action.ViewActions.typeText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.intent.Intents.intending;
import static android.support.test.espresso.intent.matcher.IntentMatchers.isInternal;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.isEnabled;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withParent;
import static android.support.test.espresso.matcher.ViewMatchers.withResourceName;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.CoreMatchers.not;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.is;

import android.app.Activity;
import android.app.Instrumentation;
import android.support.test.espresso.DataInteraction;
import android.support.test.espresso.NoMatchingViewException;
import android.support.test.espresso.ViewAssertion;
import android.support.test.espresso.ViewInteraction;
import android.support.test.espresso.action.ViewActions;
import android.support.test.espresso.assertion.ViewAssertions;
import android.support.test.espresso.contrib.RecyclerViewActions;
import android.support.test.espresso.intent.Intents;
import android.support.test.espresso.matcher.BoundedMatcher;
import android.support.test.espresso.matcher.ViewMatchers;
import android.support.test.rule.ActivityTestRule;
import android.support.test.runner.AndroidJUnit4;
import android.test.suitebuilder.annotation.LargeTest;
import android.view.View;
import android.view.ViewGroup;
import android.view.ViewParent;
import android.widget.RelativeLayout;
import android.widget.TextView;

import org.hamcrest.Description;
import org.hamcrest.Matcher;
import org.hamcrest.MatcherAssert;
import org.hamcrest.TypeSafeMatcher;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

@LargeTest
@RunWith(AndroidJUnit4.class)
public class ShoppingListTest12 {

    @Rule
    public ActivityTestRule<ShoppingActivity> mActivityTestRule = new ActivityTestRule<>(ShoppingActivity.class);

    @Test
    public void testShoppingListPriceDescSort() {
        onView(withText("Family")).perform(click());

        openActionBarOverflowOrOptionsMenu(getInstrumentation().getTargetContext());

        ViewInteraction settingView = onView(withText("Settings"));
        settingView.perform(click());

        ViewInteraction orderSelectView = onView(withText("Sort order"));
        orderSelectView.perform(click());

        ViewInteraction priceDescendingView = onView(withText("most expensive first"));
        priceDescendingView.perform(click());

        pressBack();

        String[] orders = {"Meat", "Egg", "Noodles"};
        onView(withId(R.id.list_items)).check(new ViewTextOrderAssertion(orders));
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
    public static Matcher<View> withIndex(final Matcher<View> matcher, final int index) {
        return new TypeSafeMatcher<View>() {
            int currentIndex = 0;

            @Override
            public void describeTo(Description description) {
                description.appendText("with index: ");
                description.appendValue(index);
                matcher.describeTo(description);
            }

            @Override
            public boolean matchesSafely(View view) {
                return matcher.matches(view) && currentIndex++ == index;
            }
        };
    }
    private static class ViewTextOrderAssertion implements ViewAssertion {
        private final String[] expectedTexts;

        public ViewTextOrderAssertion(String[] expectedTexts) {
            this.expectedTexts = expectedTexts;
        }




        @Override
        public void check(View view, NoMatchingViewException noViewFoundException) {
            if (noViewFoundException != null) {
                throw noViewFoundException;
            }

            if (!(view instanceof ViewGroup)) {
                throw new IllegalStateException("The asserted view is not a ViewGroup");
            }

            ViewGroup viewGroup = (ViewGroup) view;
            int childCount = viewGroup.getChildCount();
            if (childCount < expectedTexts.length) {
                throw new AssertionError("ViewGroup does not contain enough children");
            }

            for (int i = 0; i < expectedTexts.length; i++) {
                View childView = viewGroup.getChildAt(i);
                if (childView instanceof ViewGroup) {
                    TextView textView = childView.findViewById(R.id.name);
                    if (textView == null) {
                        throw new AssertionError("Child view at index " + i + " does not contain a TextView with the specified ID");
                    }
                    MatcherAssert.assertThat("Child view at index " + i, textView.getText().toString(), is(expectedTexts[i]));
                } else {
                    throw new AssertionError("Child view at index " + i + " is not a ViewGroup");
                }
            }
        }


    }

}
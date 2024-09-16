package privacyfriendlyshoppinglist.ui.main;


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

import privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist.R;

import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.action.ViewActions.scrollTo;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.contrib.RecyclerViewActions.actionOnItemAtPosition;
import static android.support.test.espresso.matcher.ViewMatchers.isCompletelyDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withContentDescription;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.is;

@LargeTest
@RunWith(AndroidJUnit4.class)
public class ShoppingListTest4 {

    @Rule
    public ActivityTestRule<SplashActivity> mActivityTestRule = new ActivityTestRule<>(SplashActivity.class);

    @Test
    public void shoppingListTest4() {
        onView(withId(R.id.recyclerView))
                .perform(actionOnItemAtPosition(0, click()));

        ViewInteraction floatingActionButton1 = onView(
                allOf(withId(R.id.fab_new_product),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.RelativeLayout")),
                                        2),
                                1),
                        isDisplayed()));
        floatingActionButton1.perform(click());

        ViewInteraction appCompatAutoCompleteTextView1 = onView(
                allOf(withId(R.id.product_name),
                        isDisplayed()));
        appCompatAutoCompleteTextView1.perform(replaceText("tomato"), closeSoftKeyboard());

        ViewInteraction textInputEditText1 = onView(
                allOf(withId(R.id.quantity),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.support.design.widget.TextInputLayout")),
                                        0),
                                0),
                        isDisplayed()));
        textInputEditText1.perform(replaceText("2"), closeSoftKeyboard());

        ViewInteraction textInputEditText3 = onView(
                allOf(withId(R.id.product_price),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.product_price_input_layout),
                                        0),
                                0),
                        isDisplayed()));
        textInputEditText3.perform(replaceText("2.13"), closeSoftKeyboard());

        ViewInteraction textInputEditText4 = onView(
                allOf(withId(R.id.product_notes),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.support.design.widget.TextInputLayout")),
                                        0),
                                0),
                        isDisplayed()));
        textInputEditText4.perform(replaceText("organic"), closeSoftKeyboard());

        ViewInteraction appCompatButton1 = onView(
                allOf(withId(android.R.id.button1), withText("Okay"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.ScrollView")),
                                        0),
                                3)));
        appCompatButton1.perform(click());

        ViewInteraction textView = onView(
                allOf(withId(R.id.textview_product_name), withText("tomato"),
                        childAtPosition(
                                allOf(withId(R.id.summary_layout),
                                        childAtPosition(
                                                IsInstanceOf.<View>instanceOf(android.widget.LinearLayout.class),
                                                0)),
                                0)));
        textView.check(matches(allOf(isDisplayed(), withText("tomato"))));

        ViewInteraction textView1 = onView(
                allOf(withId(R.id.textview_prod_quantity), withText("2")));
        textView1.check(matches(allOf(isDisplayed(), withText("2"))));

        ViewInteraction actionMenuItemView = onView(
                allOf(withId(R.id.imageview_sort), withContentDescription("Sort"),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.action_bar),
                                        2),
                                1),
                        isDisplayed()));
        actionMenuItemView.perform(click());

        ViewInteraction appCompatRadioButton1 = onView(
                allOf(withId(R.id.radiobutton_descending), withText("Descending"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.LinearLayout")),
                                        1),
                                1)));
        appCompatRadioButton1.perform(click());

        ViewInteraction appCompatButton2 = onView(
                allOf(withId(android.R.id.button1), withText("Okay"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.ScrollView")),
                                        0),
                                3)));
        appCompatButton2.perform(click());

        ViewInteraction textView3 = onView(
                allOf(withId(R.id.textview_product_name), withText("tomato"),
                        childAtPosition(
                                allOf(withId(R.id.summary_layout),
                                        childAtPosition(
                                                IsInstanceOf.<View>instanceOf(android.widget.LinearLayout.class),
                                                0)),
                                0),
                        isDisplayed()));
        textView3.check(matches(allOf(isDisplayed(), withText("tomato"))));

        ViewInteraction textView4 = onView(
                allOf(withId(R.id.textview_product_name), withText("yogurt"),
                        childAtPosition(
                                allOf(withId(R.id.summary_layout),
                                        childAtPosition(
                                                IsInstanceOf.<View>instanceOf(android.widget.LinearLayout.class),
                                                0)),
                                0),
                        isDisplayed()));
        textView4.check(matches(allOf(isDisplayed(), withText("yogurt"))));

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

package chan.android.app.pocketnote;


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
import org.junit.Ignore;
import org.junit.Rule;
import org.junit.Test;
import org.junit.runner.RunWith;

import static android.support.test.espresso.Espresso.onData;
import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.Espresso.pressBack;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
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
@Ignore
@LargeTest
@RunWith(AndroidJUnit4.class)
public class NoteTakingTest2 {

    @Rule
    public ActivityTestRule<MainActivity> mActivityTestRule = new ActivityTestRule<>(MainActivity.class);

    @Test
    public void noteTakingTest2() {
        DataInteraction relativeLayout = onData(anything())
                .inAdapterView(allOf(withId(R.id.notes_$_listview),
                        childAtPosition(
                                withId(R.id.notes_$_viewflipper),
                                0)))
                .atPosition(0);
        relativeLayout.perform(click());

        ViewInteraction editText8 = onView(
                allOf(withId(R.id.editor_$_edittext_title),
                        isDisplayed()));
        editText8.perform(replaceText("to-do list"), closeSoftKeyboard());

        pressBack();

        ViewInteraction textView = onView(
                allOf(withId(R.id.note_item_$_textview_title), withText("to-do list"),
                        childAtPosition(
                                allOf(withId(R.id.note_item_$_parent),
                                        childAtPosition(
                                                withId(R.id.notes_$_listview),
                                                0)),
                                1)));
        textView.check(matches(allOf(withText("to-do list"), isDisplayed())));

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

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
import static android.support.test.espresso.action.ViewActions.longClick;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.anything;
import static org.hamcrest.Matchers.is;
@Ignore
@LargeTest
@RunWith(AndroidJUnit4.class)
public class NoteTakingTest3 {

    @Rule
    public ActivityTestRule<MainActivity> mActivityTestRule = new ActivityTestRule<>(MainActivity.class);

    @Test
    public void noteTakingTest3() {
        DataInteraction relativeLayout = onData(anything())
                .inAdapterView(allOf(withId(R.id.notes_$_listview),
                        childAtPosition(
                                withId(R.id.notes_$_viewflipper),
                                0)))
                .atPosition(0);
        relativeLayout.perform(longClick());

        DataInteraction linearLayout2 = onData(anything())
                .inAdapterView(allOf(withId(R.id.purple_dialog_$_listview_items),
                        childAtPosition(
                                withClassName(is("android.widget.LinearLayout")),
                                1)))
                .atPosition(3);
        linearLayout2.perform(click());

        ViewInteraction spinner = onView(
                allOf(withId(R.id.reminder_$_spinner_type),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.RelativeLayout")),
                                        0),
                                1),
                        isDisplayed()));
        spinner.perform(click());

        DataInteraction linearLayout3 = onData(anything())
                .inAdapterView(childAtPosition(
                        withClassName(is("android.widget.PopupWindow$PopupBackgroundView")),
                        0))
                .atPosition(1);
        linearLayout3.perform(click());

        ViewInteraction spinner2 = onView(
                allOf(withId(R.id.reminder_$_spinner_time_alarm_when),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.reminder_$_spinner_god_father),
                                        1),
                                1),
                        isDisplayed()));
        spinner2.perform(click());

        DataInteraction linearLayout4 = onData(anything())
                .inAdapterView(childAtPosition(
                        withClassName(is("android.widget.PopupWindow$PopupBackgroundView")),
                        0))
                .atPosition(1);
        linearLayout4.perform(click());

        ViewInteraction spinner3 = onView(
                allOf(withId(R.id.reminder_$_spinner_time_alarm_repetition),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.reminder_$_spinner_god_father),
                                        1),
                                5),
                        isDisplayed()));
        spinner3.perform(click());

        DataInteraction linearLayout5 = onData(anything())
                .inAdapterView(childAtPosition(
                        withClassName(is("android.widget.PopupWindow$PopupBackgroundView")),
                        0))
                .atPosition(1);
        linearLayout5.perform(click());

        ViewInteraction button = onView(
                allOf(withId(R.id.reminder_$_button_save), withText("Save"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("android.widget.RelativeLayout")),
                                        1),
                                2),
                        isDisplayed()));
        button.perform(click());

        ViewInteraction imageView = onView(
                allOf(withId(R.id.note_item_$_imageview_reminder),
                        isDisplayed()));
        imageView.check(matches(isDisplayed()));

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

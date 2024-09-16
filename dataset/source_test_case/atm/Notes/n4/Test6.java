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
public class NoteTakingTest6 {

    @Rule
    public ActivityTestRule<MainActivity> mActivityTestRule = new ActivityTestRule<>(MainActivity.class);

    @Test
    public void noteTakingTest6() {
        ViewInteraction actionMenuItemView = onView(
                allOf(withId(R.id.notes_menu_$_add), withContentDescription("Add"),
                        childAtPosition(
                                childAtPosition(
                                        withClassName(is("com.android.internal.widget.ActionBarView")),
                                        1),
                                1),
                        isDisplayed()));
        actionMenuItemView.perform(click());

        ViewInteraction editText1 = onView(
                allOf(withId(R.id.editor_$_edittext_title),
                        childAtPosition(
                                allOf(withId(R.id.editor_$_linearlayout_border),
                                        childAtPosition(
                                                withClassName(is("android.widget.LinearLayout")),
                                                0)),
                                0),
                        isDisplayed()));
        editText1.perform(replaceText("CS200"), closeSoftKeyboard());

        ViewInteraction noteEditor1 = onView(
                allOf(withId(R.id.editor_$_note_editor),
                        childAtPosition(
                                childAtPosition(
                                        withId(android.R.id.content),
                                        0),
                                1),
                        isDisplayed()));
        noteEditor1.perform(replaceText("Session1"), closeSoftKeyboard());

        pressBack();

        ViewInteraction imageView3 = onView(
                allOf(withId(R.id.notes_$_imageview_sticky),
                        childAtPosition(
                                childAtPosition(
                                        withId(R.id.content),
                                        0),
                                1),
                        isDisplayed()));
        imageView3.perform(click());

        ViewInteraction linearLayout = onView(
                allOf(childAtPosition(
                        allOf(withId(android.R.id.tabs),
                                childAtPosition(
                                        withClassName(is("android.widget.LinearLayout")),
                                        0)),
                        0),
                        isDisplayed()));
        linearLayout.perform(click());

        DataInteraction linearLayout3 = onData(anything())
                .inAdapterView(allOf(withId(R.id.tab_host_$_listview_sort_by),
                        childAtPosition(
                                withId(android.R.id.tabcontent),
                                0)))
                .atPosition(1);
        linearLayout3.perform(click());

        ViewInteraction textView = onView(
                allOf(withId(R.id.note_item_$_textview_title), withText("CS100"),
                        childAtPosition(
                                allOf(withId(R.id.note_item_$_parent),
                                        childAtPosition(
                                                withId(R.id.notes_$_listview),
                                                1)),
                                1)));
        textView.check(matches(allOf(withText("CS100"), isDisplayed())));

        ViewInteraction textView2 = onView(
                allOf(withId(R.id.note_item_$_textview_title), withText("CS200"),
                        childAtPosition(
                                allOf(withId(R.id.note_item_$_parent),
                                        childAtPosition(
                                                withId(R.id.notes_$_listview),
                                                0)),
                                1)));
        textView2.check(matches(allOf(withText("CS200"), isDisplayed())));

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

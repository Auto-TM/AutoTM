package chan.android.app.pocketnote;


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
import static android.support.test.espresso.Espresso.pressBack;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.pressImeActionButton;
import static android.support.test.espresso.action.ViewActions.replaceText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.isCompletelyDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.isDisplayed;
import static android.support.test.espresso.matcher.ViewMatchers.withClassName;
import static android.support.test.espresso.matcher.ViewMatchers.withContentDescription;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;
import static org.hamcrest.Matchers.allOf;
import static org.hamcrest.Matchers.is;
@Ignore
@LargeTest
@RunWith(AndroidJUnit4.class)
public class NoteTakingTest5 {

    @Rule
    public ActivityTestRule<MainActivity> mActivityTestRule = new ActivityTestRule<>(MainActivity.class);

    @Test
    public void noteTakingTest5() {
        ViewInteraction linearLayout = onView(
                allOf(withId(R.id.notes_$_linearlayout_empty),
                        childAtPosition(
                                allOf(withId(R.id.notes_$_viewflipper),
                                        childAtPosition(
                                                withClassName(is("android.widget.RelativeLayout")),
                                                0)),
                                2),
                        isDisplayed()));
        linearLayout.perform(click());

        ViewInteraction editText2 = onView(
                allOf(withId(R.id.editor_$_edittext_title),
                        childAtPosition(
                                allOf(withId(R.id.editor_$_linearlayout_border),
                                        childAtPosition(
                                                withClassName(is("android.widget.LinearLayout")),
                                                0)),
                                0),
                        isDisplayed()));
        editText2.perform(replaceText("CS100"), closeSoftKeyboard());

        ViewInteraction noteEditor2 = onView(
                allOf(withId(R.id.editor_$_note_editor),
                        childAtPosition(
                                childAtPosition(
                                        withId(android.R.id.content),
                                        0),
                                1),
                        isDisplayed()));
        noteEditor2.perform(replaceText("Session1"), closeSoftKeyboard());

        pressBack();

        ViewInteraction textView = onView(
                allOf(withId(R.id.note_item_$_textview_title),
                        withText("CS100")));
        textView.check(matches(isCompletelyDisplayed()));

        ViewInteraction textView2 = onView(
                allOf(withId(R.id.note_item_$_textview_content),
                        withText("Session1")));
        textView2.check(matches(isCompletelyDisplayed()));

        ViewInteraction imageView = onView(
                allOf(withClassName(is("android.widget.ImageView")), withContentDescription("Search"),
                        childAtPosition(
                                allOf(withClassName(is("android.widget.LinearLayout")),
                                        childAtPosition(
                                                withId(R.id.notes_menu_$_search),
                                                0)),
                                1),
                        isDisplayed()));
        imageView.perform(click());

        ViewInteraction searchAutoComplete2 = onView(
                allOf(withClassName(is("android.widget.SearchView$SearchAutoComplete")),
                        childAtPosition(
                                allOf(withClassName(is("android.widget.LinearLayout")),
                                        childAtPosition(
                                                withClassName(is("android.widget.LinearLayout")),
                                                1)),
                                0),
                        isDisplayed()));
        searchAutoComplete2.perform(replaceText("cs"), pressImeActionButton());

        ViewInteraction textView4 = onView(
                allOf(withId(R.id.note_item_$_textview_title), withText("CS100"),
                        childAtPosition(
                                allOf(withId(R.id.note_item_$_parent),
                                        childAtPosition(
                                                withId(R.id.notes_$_listview),
                                                0)),
                                1)));
        textView4.check(matches(isDisplayed()));

        ViewInteraction textView5 = onView(
                allOf(withId(R.id.note_item_$_textview_content), withText("Session1")));
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

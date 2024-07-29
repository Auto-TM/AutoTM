import openai

def analyze(gpt, previous_json, current_widget_id, current_page, next_page):
    openai.api_key = gpt.key
    openai.api_base = gpt.api_base

    response = openai.ChatCompletion.create(
        model = gpt.model,
        messages=[
            {
                "role": "system",
                "content": "You are currently conducting a test case migration for the Android app, You hope to identify all proper elements and describe their possible intentions for me, in order to provide a basis for path matching of subsequent event sequences."
            },
            {
                "role": "user", 
                "content":"""
Assist in generating formal responses of Output Format below for interactions with a widget on a given page. This involves analyzing JSON data from the previous, current, and subsequent pages obtained after interacting with the widget.

### Input Description

**Previous Page JSON**:

- JSON data describing the GUI elements on the page preceding the current interaction.

**Current Page JSON**:

- JSON data for the current page, detailing the GUI elements including the target widget. This includes element attributes such as text, description, ID, type, index, coordinates (x, y), supported behaviors, and child elements.

**Next Page JSON**:

- JSON data describing the GUI elements on the page that appears after interacting with the widget on the current page.

**Widget ID**:

- The identifier of the widget being interacted with on the current page.

### Output Format

Only output the specified widget below(Widget ID) interaction using the format below, outlining the executed action and its purpose with widgets of next page by Next Page JSON:

```
~~~
ACTION (element_type, element_id, (x, y), action, value): purpose
~~~
```

### Example

#### Input

**Widget ID of Current Page**:

```
"privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/imageview_delete"
```

**Previous Page JSON**:

```json
{
    "elements": [
        {
            "id": "back_button",
            "type": "android.widget.Button",
            "x": 10,
            "y": 10,
            "control": [
                "clickable"
            ],
            "desc": "Go back"
        },
        ...
    ]
}
```

**Current Page JSON**:

```json
{
    "elements": [
        {
            "text": "Delete",
            "desc": "Deletes the selected list",
            "id": "privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/imageview_delete",
            "type": "android.widget.TextView",
            "index": 1,
            "x": 272,
            "y": 28,
            "control": [
                "clickable",
                "longClickable"
            ],
            "children": [
                
            ]
        },
        ...
    ]
}
```

**Next Page JSON**:

```json
{
    "elements": [
        {
            "id": "confirmation_dialog",
            "type": "android.widget.Dialog",
            "x": 50,
            "y": 50,
            "control": [
                "visible"
            ],
            "desc": "Confirm deletion"
        },
        ...
    ]
}
```

#### Output Format(Containing only the following ACTION text, only no need to reply to others. Just one line, which specifies the executed action and its purpose with widgets of the next page by Next Page JSON for the designated Widget ID:):
ACTION (android.widget.TextView, privacyfriendlyshoppinglist.secuso.org.privacyfriendlyshoppinglist:id/imageview_delete, (272, 28), click, NULL): Click to delete the list. The page after clicking this control is the delete list page, which has a delete button and a delete item component.


The following is the parameter information that will be entered soon，Just one line of your response, which specifies the executed action and its purpose with widgets of the next page by Next Page JSON for the designated Widget ID below:
## Widget ID:
"""+current_widget_id+"""
## Previous Page JSON:
"""+previous_json+"""
## Current Page JSON:
"""+current_page+"""
## Next Page JSON:
"""+next_page
             },
        ],
        temperature=0,
    )
    return list(response.choices)[0].to_dict()["message"]['content']


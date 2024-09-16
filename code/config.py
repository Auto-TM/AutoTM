class Gpt:
    def __init__(self, key, model):
        self.key = key
        self.model = model

device_name = 'emulator-5568'
model = "gpt-4"
openai_api_config = Gpt("sk-3BRJiWgZuN4JsLHp6bC5De7a81C12166A87d13AaC6E2B212", model)

operate_list = ["clickable", "longClickable", "swipe_to_right", "swipe_to_left"]
# operate_list = ["clickable"]
not_swipe_types = ["android.widget.ImageButton", "android.widget.Button",
                   'android.widget.ImageView', 'android.widget.ListView']
MAX_RETRY_TIMES = 5
MAX_AGENT_RETRY_TIMES = 20

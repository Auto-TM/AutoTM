class Gpt:
    def __init__(self, key, model):
        self.key = key
        self.model = model



MAX_RETRY_TIMES = 5
MAX_AGENT_RETRY_TIMES = 20
openai_api_config = Gpt("sk-I8dkcz5YVLpyr9nK679010902fFb479c9bDdFbEe1a82A893", "gpt-4")
openai_api_config.api_base = "https://xa.blackbox.red/v1"

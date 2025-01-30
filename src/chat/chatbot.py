from src.models import MODEL_MAPPING
from src.config.settings import DEFAULT_PROVIDER

class ChatBot:
    def __init__(self, provider=DEFAULT_PROVIDER):
        self.model = MODEL_MAPPING[provider]()

    def chat(self, message, history):
        system_message = "You are a helpful assistant in a clothes store. Encourage customers to check items on sale."

        if 'belt' in message:
            system_message += " The store does not sell belts; suggest other sale items."

        messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
        return self.model.chat(messages)
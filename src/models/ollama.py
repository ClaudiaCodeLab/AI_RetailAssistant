from openai import OpenAI
from .base import ChatModel
import os

class OllamaModel(ChatModel):
    def __init__(self):
        self.client = OpenAI(base_url=os.getenv("OLLAMA_API_URL"), api_key=os.getenv("API_KEY"))

    def chat(self, messages):
        stream = self.client.chat.completions.create(model=os.getenv("MODEL"), messages=messages, stream=True)
        response = ""
        for chunk in stream:
            response += chunk.choices[0].delta.content or ''
        return response
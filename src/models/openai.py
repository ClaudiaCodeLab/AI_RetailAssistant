import openai
from .base import ChatModel
import os

class OpenAIModel(ChatModel):
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def chat(self, messages):
        response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
        return response["choices"][0]["message"]["content"]
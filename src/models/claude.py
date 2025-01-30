# Example structure for Claude API (Anthropic)
import anthropic
from .base import ChatModel
import os

class ClaudeModel(ChatModel):
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.getenv("CLAUDE_API_KEY"))

    def chat(self, messages):
        response = self.client.completions.create(model="claude-2", messages=messages)
        return response.completion
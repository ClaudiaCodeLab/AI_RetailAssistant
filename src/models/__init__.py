from .ollama import OllamaModel
from .openai import OpenAIModel
from .claude import ClaudeModel

MODEL_MAPPING = {
    "ollama": OllamaModel,
    "openai": OpenAIModel,
    "claude": ClaudeModel
}
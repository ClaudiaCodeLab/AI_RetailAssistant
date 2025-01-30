import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY", "ollama")
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/v1")
MODEL = os.getenv("MODEL", "llama3.2")
DEFAULT_PROVIDER = os.getenv("DEFAULT_PROVIDER", "ollama")
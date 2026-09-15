# config.py

# Model settings (Using qwen2.5:7b or llama3.1:8b for native tool calling in Ollama)
OLLAMA_MODEL = "qwen2.5:7b"
OLLAMA_BASE_URL = "http://localhost:11434"

# Guardrail Configuration
MAX_INPUT_LENGTH = 300
ALLOWLIST_GREETINGS = ["hi", "hello", "hey", "how are you", "good morning", "good evening"]

# Default Guardrail Responses
GREETING_RESPONSE = "Hello! I am a specialized Weather & Temperature Assistant. How can I help you with weather information today?"
DENIAL_RESPONSE = "I am restricted to answering questions related to weather information and temperature conversions only."
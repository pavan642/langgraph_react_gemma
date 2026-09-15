# guardrails.py
import re
import config

def validate_input(user_input: str) -> dict:
    """
    Validates user input against strict guardrails:
    1. Maximum context length.
    2. Intercepts generic greetings with a default response.
    3. Gibberish and character noise detection.
    4. Topic restriction (Weather & Temperature domain enforcement).
    """
    cleaned_input = user_input.strip().lower()

    # 1. Input Context Length Check
    if len(user_input) > config.MAX_INPUT_LENGTH:
        return {
            "is_valid": False,
            "response": f"Input exceeds maximum allowed length of {config.MAX_INPUT_LENGTH} characters."
        }

    # 2. Block Generic Greetings with Default Response
    if cleaned_input in config.ALLOWLIST_GREETINGS or any(cleaned_input == g for g in config.ALLOWLIST_GREETINGS):
        return {
            "is_valid": False,
            "response": config.GREETING_RESPONSE
        }

    # 3. Gibberish & Noise Detection
    if re.search(r'[^\w\s\?°C°F\.\,-]', user_input) or _is_gibberish_text(cleaned_input):
        return {
            "is_valid": False,
            "response": "Your input appears to be invalid or unintelligible. Please ask a clear weather-related question."
        }

    # 4. Domain Enforcement (Weather/Temperature Topics Only)
    weather_keywords = [
        "weather", "temperature", "celsius", "fahrenheit", "forecast", 
        "convert", "degree", "rain", "sunny", "cloudy", "tokyo", "london", "new york"
    ]
    if not any(keyword in cleaned_input for keyword in weather_keywords):
        return {
            "is_valid": False,
            "response": config.DENIAL_RESPONSE
        }

    return {"is_valid": True, "response": None}

def _is_gibberish_text(text: str) -> bool:
    """Detects repeated random consonant streams."""
    consonants_regex = re.compile(r'[bcdfghjklmnpqrstvwxyz]{6,}', re.IGNORECASE)
    return bool(consonants_regex.search(text))
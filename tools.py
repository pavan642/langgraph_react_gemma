# tools.py
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    weather_data = {
        "london": "15°C, cloudy",
        "tokyo": "22°C, sunny",
        "new york": "8°C, rain",
    }
    city_key = city.strip().lower()
    return weather_data.get(city_key, f"No weather data available for '{city}'")

@tool
def convert_temperature(celsius: float) -> str:
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return f"{celsius}°C = {fahrenheit}°F"

weather_tools = [get_weather, convert_temperature]
import requests
import logging
from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger("todo_app")

BLUE = "#99ccff"
YELLOW_ORANGE = "#ffcc99"
RED = "#ff6666"
WHITE = "#ffffff"

weather_to_color_mapping = {
    "Clear": RED,
    "Clouds": YELLOW_ORANGE,
    "Snow": BLUE,
    "Atmosphere": BLUE,
    "Snow": BLUE,
    "Rain": BLUE,
    "Drizzle": BLUE,
    "Thunderstorm": BLUE,
}


def get_weather_code_and_temp_for_city(city):
    ret = get_weather_data(city.location[0], city.location[1])
    weather, temperature = ret
    return (
        weather_to_color_mapping.get(weather, WHITE),
        temperature,
    )


def get_weather_data(longitude, latitude):
    # Check if the data is already cached
    cache_key = f"weather_data_{latitude}_{longitude}"
    cached_data = cache.get(cache_key)

    if cached_data:
        # If cached data exists, return it and save on calling the API
        logger.debug("Using cached data")
        return cached_data

    # Make a request to OpenWeatherMap API using your API key
    api_key = settings.OPENWEATHER_API_KEY
    api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=metric&appid={api_key}"

    try:
        response = requests.get(api_url)
        response_data = response.json()
        temperature = response_data["main"]["temp"]
        weather = response_data["weather"][0]["main"]
    except Exception as e:
        print(e)
        return None, None

    ret = (weather, temperature)

    # Cache the data with the specified timeout
    cache.set(cache_key, ret, settings.CACHE_TIMEOUT_SECONDS)
    return ret

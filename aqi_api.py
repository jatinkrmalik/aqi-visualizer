import logging
import requests
from utils import filter_english_characters


def get_aqi_data(city_name, token):
    logging.info(f"Fetching AQI data for {city_name}")
    aqi_url = f"https://api.waqi.info/feed/{city_name}/"
    params = {"token": token}
    response = requests.get(aqi_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "ok":
            logging.info(
                f"Successfully retrieved AQI data: {data['data']['aqi']} for city: {data['data']['city']['name']}"
            )
            if city_name == "here":
                city_name = filter_english_characters(data["data"]["city"]["name"])
            return city_name, data["data"]["aqi"]

    logging.error(f"Failed to retrieve data, status code: {response.status_code}")
    response.raise_for_status()

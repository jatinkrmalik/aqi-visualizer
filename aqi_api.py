import logging
import requests

def get_aqi_data(city_name, token):
    logging.info(f"Fetching AQI data for {city_name}")
    aqi_url = f"https://api.waqi.info/feed/{city_name}/"
    params = {'token': token}
    response = requests.get(aqi_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "ok":
            logging.info(f"Successfully retrieved AQI data: {data['data']['aqi']}")
            return data["data"]["aqi"]
    logging.error(f"Failed to retrieve data, status code: {response.status_code}")
    response.raise_for_status()

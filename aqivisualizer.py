import os
import requests
import shutil
import argparse
import logging
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from collections import Counter
from openai import OpenAI

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to fetch AQI data
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

# Function to generate image prompt
def generate_image_prompt(city_name, aqi):
    logging.info(f"Generating image prompt for city: {city_name}, with AQI: {aqi}")
    return (
        "Create a realistic landscape image of a famous landmark or popular destination from {}. "
        "The image should be altered to reflect an Air Quality Index based on AQI value: {}. "
        "The artistic style should be a hyper-realistic render, closely resembling a high-resolution photograph. "
        "The aspect ratio of the image should be 16:9 to provide a wide landscape view"
    ).format(city_name, aqi)

# Function to create image with OpenAI
def create_image_with_openai(api_key, prompt):
    logging.info(f"Requesting image generation with prompt: {prompt}")
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",
        quality="standard",
        n=1,
    )
    if response.data:
        logging.info("Image generated successfully")
        return response.data[0].url
    else:
        logging.error(f"Image generation failed, status code: {response.status_code}")
        response.raise_for_status()

# Function to download image
def download_image(image_url):
    logging.info(f"Downloading image from URL: {image_url}")
    response = requests.get(image_url)
    if response.status_code == 200:
        logging.info("Image downloaded successfully")
        return Image.open(BytesIO(response.content))
    else:
        logging.error(f"Failed to download image, status code: {response.status_code}")
        response.raise_for_status()

# Function to add text to image
def add_text_to_image(image, city_name, aqi, custom_text=None):
    logging.info("Adding text overlay to image")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    text = custom_text if custom_text else f"{city_name} // {aqi}"
    text_size = draw.textlength(text, font=font)
    position = (image.width - text_size - 50, 50)
    most_common_color = Counter(image.getdata()).most_common(1)[0][0]
    draw.text(position, text, font=font, fill=most_common_color)
    logging.info("Text overlay added successfully")
    return image

# Function to save and copy the image
def save_and_copy_image(image, city_name, aqi, user_path):
    logging.info("Saving and copying image to the specified path")
    temp_path = f"/tmp/{city_name}_{aqi}.png"
    image.save(temp_path)
    logging.info(f"Image saved to temporary path: {temp_path}")
    shutil.copy(temp_path, user_path)
    logging.info(f"Image copied to user-specified path: {user_path}")

# Argument parser setup
parser = argparse.ArgumentParser(description='Generate an image with AQI data overlay.')
parser.add_argument('--city', type=str, default='here', help='City name to fetch the AQI data and generate image.')
parser.add_argument('--text', type=str, help='Custom text to overlay on the image.')
args = parser.parse_args()

# Constants
OPEN_AI_TOKEN = os.getenv('OPEN_AI_TOKEN')
AQICN_TOKEN = os.getenv('AQICN_TOKEN')
FONT_PATH = '/System/Library/Fonts/Avenir Next.ttc'  # Path to a .ttf font file
FONT_SIZE = 50

# Use the arguments
CITY_NAME = args.city
CUSTOM_TEXT = args.text

# Main function to orchestrate the script
def main(user_path):
    try:
        # Fetch AQI data
        aqi = get_aqi_data(CITY_NAME, AQICN_TOKEN)
        
        # Generate the image prompt
        prompt = generate_image_prompt(CITY_NAME, aqi)
        logging.info(f"Generated prompt: {prompt}")

        # Create the image with OpenAI
        logging.info("Requesting image generation from OpenAI")
        image_url = create_image_with_openai(OPEN_AI_TOKEN, prompt)

        # Download the generated image
        logging.info("Downloading the generated image")
        image = download_image(image_url)

        # Add text to the image
        logging.info("Adding text to the image")
        image = add_text_to_image(image, CITY_NAME, aqi, CUSTOM_TEXT)

        # Save and copy the image to the user-provided path
        save_and_copy_image(image, CITY_NAME, aqi, user_path)

    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    user_provided_path = input("Please enter the path to save the image: ") or os.getcwd()
    main(user_provided_path)

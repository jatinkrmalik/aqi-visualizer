import os
import requests
import shutil
import argparse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from collections import Counter
from openai import OpenAI

# Function to fetch AQI data
def get_aqi_data(city_name, token):
    aqi_url = f"https://api.waqi.info/feed/{city_name}/"
    params = {'token': token}
    response = requests.get(aqi_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "ok":
            return data["data"]["aqi"]
    response.raise_for_status()

# Function to generate image prompt
def generate_image_prompt(city_name, aqi):
    return (
        "Create a realistic landscape image of a famous landmark or popular destination from {}. "
        "The image should be altered to reflect an Air Quality Index based on AQI value: {}. "
        "The artistic style should be a hyper-realistic render, closely resembling a high-resolution photograph. "
        "The aspect ratio of the image should be 16:9 to provide a wide landscape view"
    ).format(city_name, aqi)

# Function to create image with OpenAI
def create_image_with_openai(api_key, prompt):
    client = OpenAI(api_key=api_key)
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1792x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url

# Function to download image
def download_image(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))

# Function to add text to image
def add_text_to_image(image, city_name, aqi, custom_text=None):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    text = custom_text if custom_text else f"{city_name} // {aqi}"
    text_size = draw.textlength(text, font=font)
    position = (image.width - text_size - 50, 50)
    most_common_color = Counter(image.getdata()).most_common(1)[0][0]
    draw.text(position, text, font=font, fill=most_common_color)
    return image

# Function to save and copy the image
def save_and_copy_image(image, city_name, aqi, user_path):
    # Save the image to a temp location
    temp_path = f"/tmp/{city_name}_{aqi}.png"
    image.save(temp_path)
    print(f"Image saved to {temp_path}")

    # Copy the image to the user-provided path
    shutil.copy(temp_path, user_path)
    print(f"Image copied to {user_path}")

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
        print(f"{CITY_NAME} AQI: {aqi}")

        # Generate the image prompt
        prompt = generate_image_prompt(CITY_NAME, aqi)

        # Create the image with OpenAI
        image_url = create_image_with_openai(OPEN_AI_TOKEN, prompt)

        # Download the generated image
        image = download_image(image_url)

        # Add text to the image
        image = add_text_to_image(image, CITY_NAME, aqi, CUSTOM_TEXT)

        # Save and copy the image to the user-provided path
        save_and_copy_image(image, CITY_NAME, aqi, user_path)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Run the script
if __name__ == "__main__":
    user_provided_path = input("Please enter the path to save the image: ")
    main(user_provided_path)


import logging
import shutil
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from collections import Counter
from openai import OpenAI
import requests

def generate_image_prompt(city_name, aqi):
    logging.info(f"Generating image prompt for city: {city_name}, with AQI: {aqi}")
    return (
        "Create a realistic landscape image of a famous landmark or popular destination from {}. "
        "The image should be altered to reflect an Air Quality Index based on AQI value: {}. "
        "The artistic style should be a hyper-realistic render, closely resembling a high-resolution photograph. "
        "The aspect ratio of the image should be 16:9 to provide a wide landscape view"
    ).format(city_name, aqi)

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

def download_image(image_url):
    logging.info(f"Downloading image from URL: {image_url}")
    response = requests.get(image_url)
    if response.status_code == 200:
        logging.info("Image downloaded successfully")
        return Image.open(BytesIO(response.content))
    else:
        logging.error(f"Failed to download image, status code: {response.status_code}")
        response.raise_for_status()

def add_text_to_image(image, city_name, aqi, font_path, font_size, custom_text=None):
    logging.info("Adding text overlay to image")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    text = custom_text if custom_text else f"{city_name} // {aqi}"
    text_size = draw.textlength(text, font=font)
    position = (image.width - text_size - 50, 50)
    most_common_color = Counter(image.getdata()).most_common(1)[0][0]
    draw.text(position, text, font=font, fill=most_common_color)
    logging.info("Text overlay added successfully")
    return image

def save_and_copy_image(image, city_name, aqi, user_path):
    logging.info("Saving and copying image to the specified path")
    temp_path = f"/tmp/{city_name}_{aqi}.png"
    image.save(temp_path)
    logging.info(f"Image saved to temporary path: {temp_path}")
    shutil.copy(temp_path, user_path)
    logging.info(f"Image copied to user-specified path: {user_path}")

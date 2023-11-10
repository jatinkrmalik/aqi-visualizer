import logging
import os
from aqi_api import get_aqi_data
from image_generator import (
    generate_image_prompt,
    create_image_with_openai,
    download_image,
    add_text_to_image,
    save_and_copy_image
)
from cli import parse_arguments
from utils import setup_logging

def main():
    setup_logging()
    args = parse_arguments()

    OPEN_AI_TOKEN = os.getenv('OPEN_AI_TOKEN')
    AQICN_TOKEN = os.getenv('AQICN_TOKEN')
    FONT_PATH = '/System/Library/Fonts/Avenir Next.ttc'
    FONT_SIZE = 50

    city_name = args.city
    custom_text = args.text
    output_path = args.output or os.getcwd()

    try:
        aqi = get_aqi_data(city_name, AQICN_TOKEN)
        prompt = generate_image_prompt(city_name, aqi)
        image_url = create_image_with_openai(OPEN_AI_TOKEN, prompt)
        image = download_image(image_url)
        image = add_text_to_image(image, city_name, aqi, FONT_PATH, FONT_SIZE, custom_text)
        output_file_path = os.path.join(output_path, f"{city_name}_{aqi}.png")
        save_and_copy_image(image, city_name, aqi, output_file_path)
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

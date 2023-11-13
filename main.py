import logging
import os
from aqi_api import get_aqi_data
from image_generator import (
    generate_image_prompt,
    create_image_with_openai,
    download_image,
    add_text_to_image,
    save_and_copy_image,
)
from cli import parse_arguments
from utils import setup_logging


def main():
    setup_logging()
    args = parse_arguments()

    OPEN_AI_TOKEN = os.getenv("OPEN_AI_TOKEN")
    AQICN_TOKEN = os.getenv("AQICN_TOKEN")

    city_name = args.city
    custom_text = args.text
    font_face = args.font_face
    font_size = args.font_size

    output_path = args.output or os.getcwd()

    try:
        # Fetch AQI data if the --aqi flag is True
        city_aqi = None
        if args.aqi:
            city_name, city_aqi = get_aqi_data(city_name, AQICN_TOKEN)
            logging.info(f"Retrieved AQI data: {city_aqi}")

        # Generate image prompt with or without AQI
        prompt = generate_image_prompt(city_name, city_aqi)

        image_url = create_image_with_openai(OPEN_AI_TOKEN, prompt)
        image = download_image(image_url)

        # If the --aqi flag is True, add the AQI overlay to the image
        if args.aqi:
            image = add_text_to_image(
                image, city_name, city_aqi, font_face, font_size, custom_text
            )
        output_file_path = os.path.join(output_path, f"{city_name}_{city_aqi}.png")
        save_and_copy_image(image, city_name, city_aqi, output_file_path)
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

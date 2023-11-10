import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate an image with AQI data overlay.')
    parser.add_argument('--city', type=str, default='here', help='City name to fetch the AQI data and generate image.')
    parser.add_argument('--text', type=str, help='Custom text to overlay on the image.')
    parser.add_argument('--output', type=str, help='Output file path to save the generated image. (Default: current working directory)')
    return parser.parse_args()

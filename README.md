# AQIVisualizer

AQIVisualizer is a command-line Python application that fetches the Air Quality Index (AQI) data for a specified city and generates a landscape image that artistically represents the current air quality conditions. The tool uses environmental data APIs and OpenAI's image generation capabilities to overlay the AQI value on the image in a hyper-realistic style.

For example: 

![image](https://github.com/jatinkrmalik/aqi-visualizer/assets/7387945/44331e70-0d0e-4ca3-a320-0e3f3c98a76a)

![image](https://github.com/jatinkrmalik/aqi-visualizer/assets/7387945/5a0db253-bbed-4185-b472-2a7f4a894101)


## Features

- Fetch real-time AQI data for any specified city.
- Generate a hyper-realistic image of the city's landmark with an AQI representation.
- Customize the text overlay on the generated image.
- Command-line arguments for easy customization.
- Save the final image to a specified path.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your machine.
- An active internet connection to fetch data from APIs and generate images.
- API keys for OpenAI and AQICN services.

## Project Structure

The project is organized into the following modules:

- `aqi_api.py`: Handles the fetching of AQI data from the environmental data API.
- `image_generator.py`: Manages the generation of images and the addition of text overlays.
- `cli.py`: Contains the command-line interface logic for accepting user inputs.
- `utils.py`: Provides utility functions such as logging setup.
- `main.py`: Serves as the entry point to the application, orchestrating the flow between modules

## Installation

To install AQIVisualizer, follow these steps:

1. Clone the repository or download the source code to your local machine.
2. Navigate to the project directory.
3. Install the required Python dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up your API keys as environment variables:
   ```sh
   export OPEN_AI_TOKEN=your_openai_token
   export AQICN_TOKEN=your_aqicn_token
   ```
   Replace `your_openai_token` and `your_aqicn_token` with your actual OpenAI and AQICN API keys, respectively.

## Usage

To use AQIVisualizer, you can run the script with optional command-line arguments. Here's how you can execute the script:

```sh
python main.py --city "City Name" --text "Custom Text Overlay" --output "path/to/save/image"
```

### Command-line Arguments

- `--city`: Specify the city name for which you want to fetch the AQI data and generate the image. If not provided, "here" will be used as the default value.
- `--text`: Custom text to overlay on the image. If not provided, the default text will be in the format "City Name // AQI".
- `--output`: Specify the path where you want to save the generated image. If not provided, the image will be saved in the current directory.
- `--help`: Display help information and exit.


## Contributing

If you would like to contribute to the development of AQIVisualizer, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature_branch`).
3. Make changes and add them (`git add .`).
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature_branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

If you have any questions or feedback, please contact the project maintainer.

Happy visualizing!


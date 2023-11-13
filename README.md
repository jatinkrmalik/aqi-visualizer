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
   export OPEN_AI_TOKEN=<your_openai_token>
   export AQICN_TOKEN=<your_aqicn_token>
   ```
   Replace `<your_openai_token>` and `<your_aqicn_token>` with your actual OpenAI and AQICN API keys, respectively.

   > Get your AQI Token from [here](https://aqicn.org/api).

## Usage

To use AQIVisualizer, you can run the script with optional command-line arguments. Here's how you can execute the script:

```sh
python main.py --city "City Name" --text "Custom Text Overlay" --output "path/to/save/image"
```

Example: 

```shell
$ python main.py --output="/Users/jmalik/Downloads" --text="konnichiwa" --city=Tokyo --font-size=100

2023-11-13 23:33:29,641 - INFO - Fetching AQI data for Tokyo
2023-11-13 23:33:34,916 - INFO - Successfully retrieved AQI data: 21 for city: Meguro (目黒)
2023-11-13 23:33:34,919 - INFO - Retrieved AQI data: 21
2023-11-13 23:33:34,919 - INFO - Generating image prompt for city: Tokyo, with AQI: 21
2023-11-13 23:33:34,919 - INFO - Requesting image generation with prompt: Create a realistic landscape image of a famous landmark or popular destination from Tokyo. The artistic style should be a hyper-realistic render, closely resembling a high-resolution photograph. The image should be altered to reflect an Air Quality based on AQI value: 21. 
2023-11-13 23:33:50,641 - INFO - HTTP Request: POST https://api.openai.com/v1/images/generations "HTTP/1.1 200 OK"
2023-11-13 23:33:50,645 - INFO - Image generated successfully
2023-11-13 23:33:50,645 - INFO - Downloading image from OpenAI
2023-11-13 23:33:57,201 - INFO - Image downloaded successfully
2023-11-13 23:33:57,216 - INFO - Adding text overlay to image
2023-11-13 23:33:57,511 - INFO - Text overlay added successfully
2023-11-13 23:33:57,511 - INFO - Saving and copying image to the specified path
2023-11-13 23:33:58,017 - INFO - Image saved to temporary path: /tmp/Tokyo_21.png
2023-11-13 23:33:58,020 - INFO - Image copied to user-specified path: /Users/jmalik/Downloads/Tokyo_21.png
```

![image](https://github.com/jatinkrmalik/aqi-visualizer/assets/7387945/dd9e4cca-be5e-4816-94ff-5e3486344404)


### Command-line Arguments

- `--city`: Specify the city name for which you want to fetch the AQI data and generate the image. If not provided, "here" will be used as the default value.
- `--aqi`: Whether to generate and overlay AQI. Use --aqi=false to disable. (Default: true)
- `--text`: Custom text to overlay on the image. If not provided, the default text will be in the format "City Name // AQI". (Note: --aqi must NOT be false for this to work.)
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


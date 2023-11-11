import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate a hyper-realistic image of a city with an optional Air Quality Index (AQI) overlay."
    )

    # Optional arguments
    optional_args = parser.add_argument_group('optional arguments')
    optional_args.add_argument(
        "--city",
        type=str,
        default="here",
        help="City name to fetch the AQI data and generate the image. Defaults to 'here', which autodetects based on IP.",
    )

    optional_args.add_argument(
        "--aqi",
        type=lambda x: (str(x).lower() in ['true', 'yes', '1']),
        nargs='?',
        const=True,
        default=True,
        help="Overlay the AQI on the image (default: true). Set to 'false' to disable.",
    )
    optional_args.add_argument(
        "--text",
        type=str,
        help="Custom text to overlay on the image. If not provided, defaults to the city name and AQI."
    )
    optional_args.add_argument(
        "--output",
        type=str,
        default=".",
        help="Output file path to save the generated image. Defaults to the current working directory."
    )

    args = parser.parse_args()

    # Post-processing for boolean flags
    if isinstance(args.aqi, str):
        args.aqi = args.aqi.lower() == 'true'

    return args

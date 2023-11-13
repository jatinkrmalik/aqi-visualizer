import logging
import re


# Setup logging
def setup_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

# Filter out non-English characters and strip whitespace from text ends
def filter_english_characters(text):
    # This regex pattern matches any character that is not a basic English letter (both cases), digit, common punctuation, or space
    pattern = re.compile("[^a-zA-Z0-9,._\- ]+")
    filtered_text = re.sub(pattern, "", text)
    return filtered_text.strip()

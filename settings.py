import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_CONFIG = {
    'api_key': os.getenv('OPENAI_API_KEY')
}

INPUT_CONFIG = {
    'title_words': (10, 50),
    'body_words': (500, 1000),
    'conclusion_words': (100, 300),
}

CRAZYNESS_LEVEL = 0
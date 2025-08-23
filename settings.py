import os
from dotenv import load_dotenv

if os.getenv("GITHUB_ACTIONS") != "true":
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

CONTENT_DIR_PATH = 'content'
WRITEN_TOPICS_FILE_PATH = 'writen_topics.csv'
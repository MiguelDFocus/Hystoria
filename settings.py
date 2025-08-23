import os

CRAZYNESS_LEVEL = 0

CONTENT_DIR_PATH = 'content'
WRITEN_TOPICS_FILE_PATH = 'writen_topics.csv'

if os.environ.get("GITHUB_ACTIONS"):
    WORKDIR = '/home/runner/work/AIHistorianBlogger/AIHistorianBlogger'
    CONTENT_DIR_PATH = f'{WORKDIR}/content'
    WRITEN_TOPICS_FILE_PATH = f'{WORKDIR}/writen_topics.csv'
else:
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
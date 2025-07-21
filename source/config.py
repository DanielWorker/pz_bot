import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')

SERVER_NAME = os.getenv('SERVER_NAME')
SCREEN_NAME = os.getenv('SCREEN_NAME')
LOG_PATH = os.getenv('LOG_PATH')

ALLOWED_USERS = {
    1170767517,
    788441330,
    365500138
}

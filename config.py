import os

import dotenv

dotenv.load_dotenv()

HEADERS = None

BOT_TOKEN = os.getenv('BOT_TOKEN')

TEST_URL = os.getenv('TEST_URL')
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
RANGE_NAME = os.getenv('RANGE_NAME')

from dotenv import load_dotenv
import os

load_dotenv(".env",override=True)

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
FROM_SEASON = os.environ.get('FROM_SEASON')
THRU_SEASON = os.environ.get('THRU_SEASON')
YEAR = os.environ.get('YEAR')
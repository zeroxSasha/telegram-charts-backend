from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")
X_USER_DATA = os.getenv("X_USER_DATA")
TELEGRAM_BOT = os.getenv("TELEGRAM_BOT")
TELEGRAM_SESSION = os.getenv("TELEGRAM_SESSION")
PALACENFT_BASE_URL = os.getenv("PALACENFT_BASE_URL")
TIMEOUT = int(os.getenv("TIMEOUT"))
TELEGRAM_SESSION_LOGIN_TIMEOUT = int(os.getenv("TELEGRAM_SESSION_LOGIN_TIMEOUT"))
SLEEP_BETWEEN_REQUESTS = float(os.getenv("SLEEP_BETWEEN_REQUESTS"))
UPDATE_INTERVAL = int(os.getenv("UPDATE_INTERVAL"))
DATABASE_URL = os.getenv("DATABASE_URL")

import time
import asyncio
import logging

from services import fetch_floor_prices
from core import UPDATE_INTERVAL
from core import TelegramWebViewError, PalaceAuthError, PalaceClientError


logger = logging.getLogger(__name__)

collections = None
last_updated = 0
supply = {}

async def updater():
    global collections, last_updated, supply
    while True:
        try:
            collections = await fetch_floor_prices()
            last_updated = time.time()
            logger.info("Collections successfully updated.")
        except TelegramWebViewError as e:
            logger.warning("Telegram WebView error: %s", e)
        except PalaceAuthError as e:
            logger.warning("Palace auth URL cannot be parsed: %s", e)
        except PalaceClientError as e:
            logger.warning("Palace client error: %s", e)
        except Exception as e:
            logger.exception("Unexpected error during updater loop")

        await asyncio.sleep(UPDATE_INTERVAL)

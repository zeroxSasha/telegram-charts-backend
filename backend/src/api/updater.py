import time
import asyncio
import logging

from services import fetch_floor_prices, fetch_supply
from core import UPDATE_INTERVAL
from core import TelegramWebViewError, PalaceAuthError, PalaceClientError, DatabaseError

logger = logging.getLogger(__name__)

collections = None
last_updated = 0
supplies = None

async def updater():
    global collections, last_updated, supplies
    while True:
        try:
            collections, supplies = await asyncio.gather(
                fetch_floor_prices(),
                fetch_supply()
            )

            last_updated = time.time()
            logger.info("Data successfully updated.")
        except TelegramWebViewError as e:
            logger.warning("Telegram WebView error: %s", e)
        except PalaceAuthError as e:
            logger.warning("Palace auth URL cannot be parsed: %s", e)
        except PalaceClientError as e:
            logger.warning("Palace client error: %s", e)
        except DatabaseError as e:
            logger.warning("Database error: %s", e)
        except Exception as e:
            logger.exception("Unexpected error during updater loop")

        await asyncio.sleep(UPDATE_INTERVAL)

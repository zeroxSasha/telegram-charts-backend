import asyncio
from clients import PalaceNFTClient
from clients import request_webview_url
from core import PALACENFT_BASE_URL, X_USER_DATA, TELEGRAM_SESSION, API_ID, API_HASH, TELEGRAM_BOT, TIMEOUT, TELEGRAM_SESSION_LOGIN_TIMEOUT, SLEEP_BETWEEN_REQUESTS
from utils import extract_auth_params, generate_x_user_data
from core import TelegramWebViewError, PalaceAuthError, PalaceClientError

async def fetch_floor_prices():
    palace_url = await get_palace_url(TELEGRAM_SESSION, API_ID, API_HASH, TELEGRAM_BOT)

    x_user_data = get_x_user_data_from_url(palace_url)

    collections = await get_collections(x_user_data)

    return await enrich_collections(collections, x_user_data)


async def get_palace_url(telegram_session, api_id, api_hash, telegram_bot):
    try:
        return await asyncio.wait_for(
            request_webview_url(telegram_session, api_id, api_hash, telegram_bot),
            timeout=TELEGRAM_SESSION_LOGIN_TIMEOUT
        )
    except asyncio.TimeoutError:
        raise TelegramWebViewError("Timeout while requesting WebView URL")
    except Exception as e:
        raise TelegramWebViewError(f"Unexpected error while requesting WebView: {e}")

def get_x_user_data_from_url(url):
    try:
        auth_date, signature, hash_value = extract_auth_params(url)
        return generate_x_user_data(X_USER_DATA, auth_date, signature, hash_value)
    except Exception as e:
        raise PalaceAuthError(f"Error while parsing palaceNFT url: {e}")

async def get_collections(x_user_data):
    try:
        async with PalaceNFTClient(PALACENFT_BASE_URL, x_user_data) as client:
            return await asyncio.wait_for(
                client.collections_on_sale(),
                timeout=TIMEOUT
            )
    except asyncio.TimeoutError:
        raise PalaceClientError("Timeout while fetching collections")
    except Exception as e:
        raise PalaceClientError(f"Unexpected error while fetching collections: {e}")

async def enrich_collections(collections, x_user_data):
    updated = {}
    async with PalaceNFTClient(PALACENFT_BASE_URL, x_user_data) as client:
        for col in collections:
            try:
                pack = await asyncio.wait_for(
                    client.offers_by_id(col["id"]),
                    timeout=TIMEOUT
                )
                updated[col["name"]] = {
                    "floor_price": pack["offers"][0]["price"],
                    "logo": col["logo"]
                }
                await asyncio.sleep(SLEEP_BETWEEN_REQUESTS)
            except asyncio.TimeoutError:
                raise PalaceClientError("Timeout while fetching offers")
            except Exception as e:
                raise PalaceClientError(f"Unexpected error while fetching offers: {e}")
    return updated

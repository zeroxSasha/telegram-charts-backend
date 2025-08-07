import asyncio
from database import fetch_supply as raw_fetch_supply
from core import DatabaseError, TIMEOUT

async def fetch_supply():
    try:
        return await asyncio.wait_for(
            raw_fetch_supply(),
            timeout=TIMEOUT
        )
    except asyncio.TimeoutError:
        raise DatabaseError("Timeout while fetching data")
    except Exception as e:
        raise DatabaseError(f"Unexpected error while fetching data: {e}")

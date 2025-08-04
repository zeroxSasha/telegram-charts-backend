import asyncio
from database import init_models as raw_init_models
from core import DatabaseError, TIMEOUT

async def init_models():
    try:
        return await asyncio.wait_for(
            raw_init_models(),
            timeout=TIMEOUT
        )
    except asyncio.TimeoutError:
        raise DatabaseError("Error occured while initializing models")
    except Exception as e:
        raise DatabaseError(f"Unexpected error while initializing models: {e}")

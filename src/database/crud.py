from .db import AsyncSessionLocal, engine
from .models import Base, Pack
from sqlalchemy import select

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def fetch_supply():
    async with AsyncSessionLocal() as session:
        result = await session.execute(
            select(Pack.collection_id, Pack.name, Pack.supply)
        )

        return result.fetchall()

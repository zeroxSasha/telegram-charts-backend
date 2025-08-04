import asyncio
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from api.updater import updater
from api.routes.app_router import router
from services import init_models
from core import DatabaseError

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app):
    try:
        await init_models()
    except DatabaseError as e:
        logger.critical("Database error: %s", e)

    task = asyncio.create_task(updater())
    try:
        yield
    finally:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            logger.info("Updater task was cancelled during shutdown.")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500",
    ],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)

app.include_router(router=router)



from fastapi import APIRouter
from .supplies import router as supplies_router
from .collections import router as collections_router

router = APIRouter()
router.include_router(supplies_router)
router.include_router(collections_router)

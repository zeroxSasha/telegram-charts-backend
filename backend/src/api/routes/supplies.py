from api import updater
from fastapi import APIRouter

router = APIRouter()

@router.get("/supplies")
async def supplies():
    if updater.supplies is None:
        return { "status": "updating" }
    else:
        result = [
            {
                "collection_id": collection_id,
                "name": name,
                "supply": supply
            }
            for collection_id, name, supply in updater.supplies
        ]
        return { "supplies": result }

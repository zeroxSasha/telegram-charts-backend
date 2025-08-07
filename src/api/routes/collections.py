import datetime
from api import updater
from fastapi import APIRouter

router = APIRouter()

@router.get("/collections")
async def collections():
    if updater.collections is None:
        return { "status": "updating" }
    else:
        value = datetime.datetime.fromtimestamp(updater.last_updated)
        
        result = []
        for name, data in updater.collections.items():
            result.append({
                "name": name,
                "floor_price": data["floor_price"],
                "logo": data["logo"]
            })

        return {
            "last_updated": value.strftime('%Y-%m-%d %H:%M:%S'),
            "collections": result,
        }

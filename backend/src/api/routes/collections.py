import datetime
from fastapi import APIRouter
from api import updater

router = APIRouter()

@router.get("/collections")
async def hello():
    if updater.collections is None:
        return {"status": "updating please wait"}
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

import aiohttp

class PalaceNFTClient:
    def __init__(self, base_url, x_user_data):
        self.__base_url = base_url
        self.__session = None
        self.__x_user_data = x_user_data

    async def __aenter__(self):
        self.__session = aiohttp.ClientSession(headers={
            "x-user-data": self.__x_user_data,
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0"
        })
        return self
    
    async def __aexit__(self, *args):
        try:
            await self.__session.close()
        except ConnectionError:
            pass

    async def collections_on_sale(self):
        url = f"{self.__base_url}/markets/collections?onSale=true"
        async with self.__session.get(url) as response:
            response.raise_for_status()
            return await response.json()

    async def offers_by_id(self, id):
        url = f"{self.__base_url}/markets/offers?collection_id={id}&limit=40&offset=0&sort=price_asc"
        async with self.__session.get(url) as response:
            response.raise_for_status()
            return await response.json()

from async_requests import Requests


class SerpAPI(Requests):

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://serpapi.com/search"

    async def search(self, data: list) -> dict:
        for params in data:
            params["api_key"] = self.api_key
        urls = [f"{self.base_url}?{Requests.build_query(params)}" for params in data]
        return await Requests.get(urls)

    async def organic_results(self, data: list) -> list:
        results = await self.search(data)
        return [result["organic_results"] for result in results]

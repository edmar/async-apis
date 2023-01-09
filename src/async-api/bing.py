from async_requests import Requests


class Bing:

    def __init__(self, subscription_key: str = None):
        self.subscription_key = subscription_key
        self.base_url = "https://api.bing.microsoft.com/v7.0/search"
        self.headers = {"Ocp-Apim-Subscription-Key": self.subscription_key}

    async def search(self, queries: list):
        urls = [f"{self.base_url}?setLang=en-US&q={query}" for query in queries]
        headers = [self.headers for _ in range(len(queries))]
        return await Requests.get(urls, headers)

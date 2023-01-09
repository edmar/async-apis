import aiohttp
import asyncio


class Requests:

    @staticmethod
    async def get_url(session, url, headers, data, res_type="json"):
        async with session.get(url, headers=headers) as resp:
            if res_type == "json":
                response = await resp.json()
            else:
                response = await resp.text()
            return response

    @staticmethod
    async def post_url(session, url, headers, data, res_type="json"):
        async with session.post(url, headers=headers, json=data) as resp:
            response = await resp.json()
            return response

    @staticmethod
    async def async_requests(method, urls: list, headers: dict = None, data=None, res_type="json"):
        if headers is None:
            headers = [None for _ in range(len(urls))]
        if data is None:
            data = [None for _ in range(len(urls))]
        async with aiohttp.ClientSession(trust_env=True) as session:
            tasks = [asyncio.ensure_future(method(session, url, header, data, res_type)) for url, header, data in zip(urls, headers, data)]
            results = await asyncio.gather(*tasks)
            return results

    @staticmethod
    def get(urls: list = [], headers: dict = None, data: dict = None, res_type="json"):
        return Requests.async_requests(method=Requests.get_url, urls=urls, headers=headers, data=data, res_type=res_type)

    @staticmethod
    def post(urls: list = [], headers: dict = None, data: dict = None):
        return Requests.async_requests(method=Requests.post_url, urls=urls, headers=headers, data=data)

    @staticmethod
    def build_query(params: dict) -> str:
        return "&".join([f"{key}={value}" for key, value in params.items()])

import pytest
import time

from async_requests import Requests


@pytest.fixture()
def get_urls():
    return [f'https://pokeapi.co/api/v2/pokemon/{number}' for number in range(1, 151)]


@pytest.fixture()
def post_urls():
    return ['https://api.openai.com/v1/completions' for _ in range(10)]


@pytest.fixture()
def headers():
    api_key = "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"
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    return [header for _ in range(10)]


@pytest.fixture()
def data():
    data = {"model": "text-davinci-002", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 60}
    return [data for _ in range(10)]


@pytest.mark.asyncio
async def test_get(get_urls):
    start = time.time()
    pokemon_names = await Requests.get(get_urls)
    end = time.time()
    print(f"Time taken: {end - start}")
    assert len(pokemon_names) == 150


@pytest.mark.asyncio
async def test_post(post_urls, headers, data):
    start = time.time()
    results = await Requests.post(post_urls, headers, data)
    end = time.time()
    print(f"Time taken: {end - start}")
    assert len(results) == 10

import pytest
from serpapi import SerpAPI


@pytest.fixture(scope="module")
def serpapi():
    serpapi = SerpAPI(api_key="30b1bef87aa82708a85e7dda0c0491bace6c2bdeb7025e991fdbc76acce4aa83")
    return serpapi


@pytest.fixture(scope="module")
def data():
    data = [
        {
            "device": "desktop",
            "engine": "google",
            "q": "Coffee",
            "location": "Austin, Texas, United States",
            "google_domain": "google.com",
            "gl": "us",
            "hl": "en"
        },
        {
            "device": "desktop",
            "engine": "google",
            "q": "books that won the hugo award for best novel",
            "location": "Austin, Texas, United States",
            "google_domain": "google.com",
            "gl": "us",
            "hl": "en"
        },
    ]
    return data


@pytest.mark.asyncio
async def test_search(serpapi, data):
    results = await serpapi.search(data)
    assert results is not None


@pytest.mark.asyncio
async def test_organic_results(serpapi, data):
    organic_results = await serpapi.organic_results(data)
    assert len(organic_results) == 2
    assert len(organic_results[0]) == 10

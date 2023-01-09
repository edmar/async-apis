import pytest
from wikipedia import Wikipedia


@pytest.fixture()
def queries():
    return ["books", "hugo award", "neuromancer"]


@pytest.fixture()
def page_titles():
    return ["Python", "Java", "C++"]


@pytest.mark.asyncio
async def test_search(queries):
    results = await Wikipedia().search(queries)
    assert len(results) == 3


@pytest.mark.asyncio
async def test_get_pages(page_titles):
    pages = await Wikipedia().get_pages(page_titles)
    assert len(pages) == 3

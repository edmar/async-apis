import os
import pytest
from bing import Bing


@pytest.fixture
def bing():
    subscription_key = os.environ.get('BING_KEY')
    return Bing(subscription_key=subscription_key)


@pytest.fixture
def queries():
    return ['python', 'asyncio']


@pytest.mark.asyncio
async def test_search(bing, queries):
    results = await bing.search(queries)
    assert len(results) == 2
    assert results[0]["queryContext"]["originalQuery"] == "python"
    assert results[1]["queryContext"]["originalQuery"] == "asyncio"

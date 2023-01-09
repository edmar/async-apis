import pytest
from gpt3 import GPT3
import os


@pytest.fixture()
def data():
    data = {"model": "text-davinci-002", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 60}
    return [data for _ in range(10)]


@pytest.fixture
def prompt_data():
    prompt = """Query: ${{a main query}}
Search: ${{keywords to search}}
Questions:
${{sub-questions of the query}}

Query: USA presidents born in New York
Search: USA presidents born in New York
Questions:
Is X a USA president?
Was X born in New York?

Query: horror movies that won the Oscars
Search: horror movies, won the Oscars
Questions:
Is X a horror movie?
Did X win the oscar?

Query:{}
Search:"""
    query = "USA presidents born in New York"
    data = {"model": "text-davinci-003", "prompt": prompt.format(query), "temperature": 0, "max_tokens": 600}
    return [data]


@pytest.fixture()
def gpt3():
    api_key = os.environ.get('OPENAI_KEY')
    return GPT3(api_key=api_key)


@pytest.mark.asyncio
async def test_completion(gpt3, data):
    results = await gpt3.completion(data)
    assert len(results) == 10


@pytest.mark.asyncio
async def test_completion_prompt(gpt3, prompt_data):
    results = await gpt3.completion(prompt_data)
    assert len(results) == 1

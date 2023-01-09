from async_requests import Requests


data = {"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 60}


class GPT3:

    def __init__(self, api_key: str = None, base_url: str = "https://api.openai.com/v1/") -> None:
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }
        self.base_url = base_url

    def completion(self, data: list):
        headers = [self.headers for _ in range(len(data))]
        urls = [f"{self.base_url}completions" for _ in range(len(data))]
        return Requests.post(urls, headers, data)

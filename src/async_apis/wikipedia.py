from async_requests import Requests
import re


class Wikipedia():

    def __init__(self, base_url: str = "https://en.wikipedia.org/w/api.php"):
        self.base_url = base_url

    def search(self, queries: list):
        urls = [f"{self.base_url}?action=query&list=search&srsearch=\"{query}\"&format=json&srlimit=500" for query in queries]
        return Requests.get(urls)

    async def get_pages(self, page_titles: list):
        urls = [f"{self.base_url}?action=query&prop=extracts&exlimit=1&explaintext=1&formatversion=2&titles={page_title}&format=json" for page_title in page_titles]
        results = await Requests.get(urls)
        # create a list of pages
        pages = []
        for page in results:
            page = page["query"]["pages"][0]
            pages.append(WikiPage(title=page["title"], text=page["extract"]))
        return pages

    async def get_pages_html(self, page_titles: list):
        urls = [f"{self.base_url}?action=parse&page={page_title}&format=json" for page_title in page_titles]
        results = await Requests.get(urls)
        # create a list of pages
        pages = []
        for page in results:
            page = page["parse"]
            html = page["text"]["*"]
            # remove all the html tags
            text = re.sub(r"<.*?>", "", html)
            pages.append(WikiPage(title=page["title"], text=text))
        return pages


class WikiPage:

    def __init__(self, title: str, text: str, questions: list = []) -> None:
        self.title = title
        self.text = text

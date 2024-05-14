from bs4 import BeautifulSoup
import mechanicalsoup

class BaseScraper:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.browser = mechanicalsoup.Browser()
        self.page = self.browser.get(self.base_url)
        self.soup: BeautifulSoup = self.page.soup

    def get_matches(self): ...

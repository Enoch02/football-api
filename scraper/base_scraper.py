"""
The base scraper module
"""

from bs4 import BeautifulSoup
import mechanicalsoup
from requests import Response


class BaseScraper:
    """
    Represents the root object that specific scrapers will inherit
    """

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.browser = mechanicalsoup.Browser()
        self.page: Response = None
        self.soup: BeautifulSoup = None

    def get_matches(self, path: str):
        """Get the list of available matches"""
        self.page = self.browser.get(path)
        self.soup = self.page.soup

    def get_match_stream_link(self, path: str):
        """Get the stream url for a specific match"""
        self.page = self.browser.get(path)
        self.soup = self.page.soup

    def get_highlights(self, path: str):
        """Get highlights from sites that contain them"""
        self.page = self.browser.get(path)
        self.soup = self.page.soup

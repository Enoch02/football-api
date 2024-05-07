from base_scraper import BaseScraper


class Ns247Scraper(BaseScraper):
    def __init__(self, base_url: str) -> None:
        super().__init__(base_url)

    def get_matches(self):
        return super().get_matches()

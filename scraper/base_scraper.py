class BaseScraper:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_matches(self): ...

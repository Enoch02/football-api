"""
Scrapes a certain football website
"""

from typing import List

from bs4 import ResultSet

from .base_scraper import BaseScraper
from .model.live_matches import NS247LiveMatches
from .model.match import NS247Match


class Ns247Scraper(BaseScraper):
    """Scraper for ns247 website"""

    def __init__(self, base_url: str = "https://naijasport247.com/") -> None:
        super().__init__(base_url)

    def get_matches(self, path: str = "live/") -> NS247LiveMatches:
        """
        Gets the available matches from the object

        :return: a LiveMatches object
        """
        super().get_matches(f"{self.base_url}{path}")
        try:
            tags: List[ResultSet] = self.soup.find_all("tr")
            matches: list[NS247Match] = []

            for match_tag in tags:
                try:
                    sub_tags = match_tag.find_all("td")

                    # rows like the date tag only have one `td`
                    if (len(sub_tags)) > 1:
                        try:
                            home_team = sub_tags[0]
                            away_team = sub_tags[2]
                            onclick_value = sub_tags[1].find("input")["onclick"]
                            start_index = onclick_value.find("'") + 1
                            end_index = onclick_value.find("'", start_index)
                            match_page_url = onclick_value[start_index:end_index]

                            match = NS247Match(
                                home_team=home_team.find("p").text,
                                home_team_logo_url=home_team.find("img").get("src"),
                                match_page_url=match_page_url,
                                channel=match_page_url.split("/")[3],
                                away_team=away_team.find("p").text,
                                away_team_logo_url=away_team.find("img").get("src"),
                            )

                            matches.append(match)
                        except (AttributeError, KeyError, IndexError, ValueError) as e:
                            print(f"Error processing match tag: {e}")

                    live_matches = NS247LiveMatches(
                        date=tags[0].find("td").text,
                        matches=matches,
                    )

                except (AttributeError, IndexError) as e:
                    print(e)
                    return None

            return live_matches
        except AttributeError as e:
            return None

    def get_match_stream_link(self, path: str = ""):
        super().get_match_stream_link(f"{self.base_url}/{path}/")

        try:
            iframe_tag = self.soup.find("iframe")

            if iframe_tag and 'src' in iframe_tag.attrs:
                video_url = iframe_tag['src']

                return video_url
            else:
                return None

        except AttributeError:
            return None

    def get_highlights(self, path: str = "highlights/"):
        super().get_highlights(path)

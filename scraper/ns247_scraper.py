from bs4 import ResultSet
from base_scraper import BaseScraper
from model.live_matches import LiveMatches
from model.match import Match
from typing import List


class Ns247Scraper(BaseScraper):
    def __init__(self, base_url: str = "https://naijasport247.com/live/") -> None:
        super().__init__(base_url)

    def get_matches(self) -> LiveMatches:
        tags: List[ResultSet] = self.soup.find_all("tr")
        live_matches: LiveMatches = None
        matches: list[Match] = []

        date = tags[0].find("td").text
        for match_tag in tags:
            try:
                sub_tags = match_tag.find_all("td")

                # rows like the date tag only have one `td`
                if (len(sub_tags)) > 1:
                    home_team = sub_tags[0]
                    match_url = sub_tags[1]
                    away_team = sub_tags[2]
                    match = Match(
                        home_team=home_team.find("p").text,
                        home_team_logo_url=home_team.find("img").get("src"),
                        match_url="",  # TODO: check when a match is going on to see if the value of `onClick` changes
                        away_team=away_team.find("p").text,
                        away_team_logo_url=away_team.find("img").get("src"),
                    )

                    matches.append(match)

                live_matches = LiveMatches(date=date, matches=matches)

            except Exception as e:
                print(e)
                pass

        return live_matches


if __name__ == "__main__":
    scraper = Ns247Scraper()
    live_matches = scraper.get_matches()

    for match in live_matches.matches:
        print(match)

from dataclasses import dataclass


@dataclass
class Match:
    home_team: str
    home_team_logo_url: str
    match_page_url: str
    away_team: str
    away_team_logo_url: str

    def to_dict(self) -> dict[str, any]:
        return {
            "home_team": self.home_team,
            "home_team_logo_url": self.home_team_logo_url,
            "match_page_url": self.match_page_url,
            "away_team": self.away_team,
            "away_team_logo_url": self.away_team_logo_url,
        }

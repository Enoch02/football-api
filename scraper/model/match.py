from dataclasses import dataclass


@dataclass
class Match:
    home_team: str
    home_team_logo_url: str
    match_url: str
    away_team: str
    away_team_logo_url: str

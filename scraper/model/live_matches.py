from dataclasses import dataclass
from . import match


@dataclass
class LiveMatches:
    date: str
    matches: list[match.Match]

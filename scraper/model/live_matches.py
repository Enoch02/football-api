from dataclasses import dataclass
from . import match


@dataclass
class LiveMatches:
    date: str
    matches: list[match.Match]

    def to_dict(self) -> dict[str, any]:
        return {"date": self.date.strip("\n"), "matches": self.matches}

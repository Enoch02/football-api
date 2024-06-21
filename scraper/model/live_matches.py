"""
Live matches model
"""

from dataclasses import dataclass

from . import match


@dataclass
class NS247LiveMatches:
    "Represents the live matches from NS247"
    date: str
    matches: list[match.NS247Match]

    def to_dict(self) -> dict[str, any]:
        """Get the dict representation of this object"""
        return {"date": self.date.strip("\n"), "matches": self.matches}

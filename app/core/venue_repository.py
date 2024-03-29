from typing import Dict

from app.core.venue import Venue


class VenueRepository:

    def __init__(self) -> None:
        self.registry: Dict[str, Venue] = {}

    def register(self, venue: Venue) -> Venue:
        self.registry[venue.venue_id] = venue
        return venue

    def get_venue_for(self, venue_id: str) -> Venue:
        return self.registry[venue_id]

    def is_registered(self, venue_id: str) -> bool:
        return venue_id in self.registry

import logging

from core.event_repository import EventRepository
from core.venue import Venue
from core.venue_processor import VenueProcessor
from core.venue_repository import VenueRepository
from venues.spot.spot_config import SpotConfig
from venues.spot.spot_fetcher import SpotFetcher
from venues.spot.spot_parser import SpotParser


class SpotProcessor(VenueProcessor):

    def __init__(self, event_repository: EventRepository):
        self.config = SpotConfig()
        self.event_repository = event_repository

    def create_venue(self) -> Venue:
        return Venue(venue_id=self.config.venue_id,
                     name='SPOT',
                     phone='+31 (0)50-3680111',
                     city='Groningen',
                     country='NL',
                     timezone='Europe/Amsterdam',
                     email='info@spotgroningen.nl',
                     url=self.config.base_url)

    def sync_stores(self) -> None:
        spot_fetcher = SpotFetcher()
        spot_parser = SpotParser(self.config)

        data = spot_fetcher.fetch()
        events = spot_parser.parse(data)
        logging.info(f'fetched a total of {len(events)} items')
        self.event_repository.upsert(events)

    def register_venue_at(self, venue_repository: VenueRepository):
        venue_repository.register(self.config.venue_id, self.create_venue(), self)
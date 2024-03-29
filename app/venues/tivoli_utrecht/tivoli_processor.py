from app.core.event_repository import EventRepository
from app.core.source import Source
from app.core.venue import Venue
from app.core.venue_processor import VenueProcessor
from app.core.venue_repository import VenueRepository
from app.venues.tivoli_utrecht.tivoli_source import TivoliSource


class TivoliProcessor(VenueProcessor):

    def __init__(self, event_repository: EventRepository, venue_repository: VenueRepository):
        self.venue = TivoliProcessor.create_venue()
        venue_repository.register(self.venue)
        super().__init__(event_repository, self.venue)

    def fetch_source(self) -> Source:
        return TivoliSource(self.venue)

    @staticmethod
    def create_venue() -> Venue:
        return Venue(venue_id='tivoli-utrecht',
                     name='Tivoli Vredenburg',
                     phone='030 - 2314544',
                     city='Utrecht',
                     country='NL',
                     timezone='Europe/Amsterdam',
                     timezone_short='+02:00',
                     email='info@tivolivredenburg.nl',
                     source_url='https://www.tivolivredenburg.nl/agenda/',
                     url='https://www.tivolivredenburg.nl')

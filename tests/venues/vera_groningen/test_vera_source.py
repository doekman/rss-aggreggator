import unittest

from hamcrest import equal_to, contains
from hamcrest.core import assert_that
from pytest import fail
from rx.operators import count, buffer_with_count, map

from app.venues.vera_groningen.vera_processor import VeraProcessor
from app.venues.vera_groningen.vera_source import VeraSource


class TestVeraGroningenSource(unittest.TestCase):

    def setUp(self) -> None:
        self.source = VeraSource(VeraProcessor.create_venue())

    def test_sample_file(self):
        self.source.observable().pipe(count()).subscribe(
            lambda aantal: assert_that(aantal, equal_to(34)),
            lambda e: fail(e))

    def test_buffering(self):
        self.source.observable().pipe(
            buffer_with_count(12),
            map(lambda items: len(items)),
            buffer_with_count(3),
        ).subscribe(
            lambda aantal: assert_that(aantal, contains(12, 12, 10)),
            lambda e: fail(e)
        )

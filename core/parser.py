from abc import ABC, abstractmethod
from typing import List

from core.event import Event
from core.parsing_context import ParsingContext


class Parser(ABC):

    @abstractmethod
    def parse(self, parsing_context: ParsingContext) -> List[Event]:
        pass

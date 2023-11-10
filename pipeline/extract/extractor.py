from typing import Protocol


class Extractor(Protocol):
    def __init__(self) -> None:
        pass

    def extract(self, data) -> None:
        pass # TODO: update io

class HTML_Extractor():
    def __init__(self) -> None:
        pass

    def extract(self, data) -> None: # ? Change to process?
        
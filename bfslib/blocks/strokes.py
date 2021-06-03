from ..abstract import AbstractBlock
from ..generators import sines


class ShortStroke(AbstractBlock):
    def __init__(self) -> None:
        super().__init__()
        self.x = sines.SimpleSine(500, 5000, (0, 100), 0, 0)
        self.y = sines.SimpleSine(500, 5000, (0, 100), 0, 0)
        self.z = sines.SimpleSine(500, 5000, (0, 100), 0, 0)

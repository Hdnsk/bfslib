import math
import numpy

from ..abstract import AbstractGenerator


class SimpleSine(AbstractGenerator):
    def __init__(self, period, duration, amplitude, x_start=0, y_start=0) -> None:
        super().__init__(period, duration, amplitude, x_start, y_start)
        self.gen_x()
        self.set_x_offset()
        self.gen_y()

    def expression(self, x) -> float:
        return self.sine_factor * math.sin((2 * math.pi) / self.period * (x + self.x_offset)) + self.y_offset

    def set_x_offset(self) -> None:
        self.x_offset = math.asin((self.y_start - self.y_offset)/self.sine_factor) * self.period / (2 * math.pi) - self.x_start

    def gen_x(self) -> None:
        self.x_list = numpy.arange(self.x_start, self.x_start + self.duration)

    def gen_y(self) -> None:
        self.y_list = numpy.empty(shape=self.x_list.size)
        for c in range(self.x_list.size):
            self.y_list[c] = self.expression(c)

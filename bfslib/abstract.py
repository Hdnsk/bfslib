from abc import ABC, abstractmethod
from scipy.signal import find_peaks
from numpy import array as nparr


class AbstractGenerator(ABC):
    def __init__(self, period, duration, amplitude, x_start, y_start) -> None:
        self.period = period
        self.duration = duration
        self.x_start = x_start

        if amplitude[0] > amplitude[1]:
            self.amplitude = (amplitude[1], amplitude[0])
        else:
            self.amplitude = amplitude

        if self.amplitude[0] <= y_start <= self.amplitude[1]:
            self.y_start = y_start
        else:
            self.y_start = amplitude[0]

        self.sine_factor = (self.amplitude[1] - self.amplitude[0])/2
        self.y_offset = self.sine_factor + self.amplitude[0]
        self.x_offset = 0

    @abstractmethod
    def expression(self, x) -> float:
        pass

    @abstractmethod
    def gen_x(self) -> None:
        pass

    @abstractmethod
    def gen_y(self) -> None:
        pass

    def set_x_offset(self) -> None:
        pass

    def get_peaks(self) -> list:
        peaks, _ = find_peaks(self.y_list)
        return peaks

    def get_valleys(self) -> list:
        inv_y = self.y_list*(-1)
        valleys, _ = find_peaks(inv_y)
        return valleys


class AbstractBlock(ABC):
    def __init__(self) -> None:
        super().__init__()

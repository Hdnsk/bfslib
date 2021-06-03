from abc import ABC, abstractmethod


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

    @abstractmethod
    def set_x_offset(self) -> None:
        pass

    def get_peaks(self) -> list:
        pass

    def get_valleys(self) -> list:
        pass


class AbstractBlock(ABC):
    def __init__(self) -> None:
        super().__init__()

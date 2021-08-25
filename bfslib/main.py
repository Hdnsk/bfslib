from .generators import sines
import matplotlib.pyplot as plt


def print_points(x, y, color):
    plt.plot(x, y, color)
    for i_x, i_y in zip(x, y):
        plt.text(i_x + 50, i_y, f"({i_x}, {i_y})")


def main():
    s = sines.SimpleSine(1500, 8000, (25, 75), 0, 0)
    plt.plot(s.x_list, s.y_list)
    plt.ylim(0, 100)
    peaks = s.get_peaks()
    valleys = s.get_valleys()
    print_points(peaks, s.y_list[peaks], "xr")
    print_points(valleys, s.y_list[valleys], "xg")

    # plt.plot(s.get_peaks(), s.y_list[s.get_peaks()], "xr")
    # for i_x, i_y in zip(s.get_peaks(), s.y_list[s.get_peaks()]):
    #     plt.text(i_x + 50, i_y, f"({i_x}, {i_y})")

    # plt.plot(s.get_valleys(), s.y_list[s.get_valleys()], "xg")
    # for i_x, i_y in zip(s.get_valleys(), s.y_list[s.get_valleys()]):
    #     plt.text(i_x + 50, i_y, f"({i_x}, {i_y})")
    plt.show()

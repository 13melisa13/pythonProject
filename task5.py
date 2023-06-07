# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


def f(y, z):
    sum = 0
    n = len(y)
    y = [0] + y
    z = [0] + z
    for i in range(1, n + 1):
        sum += 96 * (y[n + 1 - i] ** 3 - 18 * z[n + 1 - math.ceil(i/2)] - 71) ** 2
    print(86 * sum)
    return sum * 86


if __name__ == "__main__":
    f([-0.88, -0.54, 0.72, 0.47, -0.69, 0.62], [0.64, 0.57, 0.54, 0.22, 0.15, -0.42])
    f([-0.87, -0.47, 0.17, 0.99, 0.88, -0.96], [-0.22, -0.51, 0.1, -0.02, -0.95, 1.0])
    f([0.08, -0.83, 0.32, 0.3, -0.65, 0.67], [0.26, 0.75, 0.7, -0.08, -0.31, 0.63])


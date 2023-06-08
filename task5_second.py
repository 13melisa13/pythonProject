import math


def f(z, x):
    s = 0
    n = len(z)
    for i in range(1, n + 1):
        s += (44 * x[math.ceil(i / 3) - 1] ** 3 - 97 * (z[n + 1 - math.ceil(i / 3) - 1]) ** 2) ** 7
    return s


if __name__ == '__main__':
    print(f([-0.73, 0.16, 0.85, 0.36, -0.79, -0.67, 0.31], [0.72, 0.17, 0.13, -0.47, -0.82, 0.57, -0.08]))

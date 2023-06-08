def x0(x, f, s):
    if x[0] == 1988:
        return f
    else:
        return s


def x2(x, f, s):
    if x[2] == 'ABNF':
        return f
    else:
        return s


def x1(x, f, s, t):
    if x[1] == 'QML':
        return f
    else:
        if x[1] == 'CLIPS':
            return s
        else:
            return t


def main(x):
    if x[4] == 1987:
        if x[3] == 'LESS':
            return x2(x, 0, x1(x, 1, 2, 3))
        else:
            if x[3] == 'OX':
                return x0(x, 4, x1(x, 5, 6, 7))
            else:
                return x2(x, 8, x0(x, 9, 10))
    else:
        return 11


if __name__ == '__main__':
    print(main([1988, 'QML', 'QMAKE', 'ABAP', 1987]))

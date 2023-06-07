def x1(x, first, second, third):
    if x[1] == 'GRACE':
        return first
    else:
        if x[1] == 'LUA':
            return second
        else:
            return third


def x0(x, first, second):
    if x[0] == 'BRO':
        return first
    else:
        return second


def x4(x, first, second, third):
    if x[4] == 1978:
        return first
    else:
        if x[4] == 2006:
            return second
        else:
            return third


def main(x):
    if x[3] == 2015:
        if x[2] == 'BRO':
            return x4(x, x1(x, 7, 8, 9), 10, 11)
        else:
            return x1(x, x0(x, 0, 1), x4(x, 2, 3, 4), x0(x, 5, 6))

    else:
        if x[3] == 1983:
            return 12
        else:
            return 13


if __name__ == "__main__":
    print(
        main(['BRO', 'GRACE', 'UNO', 2015, 1978]),  # 0
        main(['J', 'GRACE', 'UNO', 2015, 1978]),  # 1

        main(['BRO', 'LUA', 'UNO', 2015, 1978]),  # 2
        main(['BRO', 'LUA', 'UNO', 2015, 2006]),  # 3
        main(['BRO', 'LUA', 'UNO', 2015, 1966]),  # 4

        main(['BRO', 'RDOC', 'UNO', 2015, 2006]),  # 5
        main(['J', 'RDOC', 'UNO', 2015, 2006]),  # 6

        main(['BRO', 'GRACE', 'BRO', 2015, 1978]),  # fail 7
        main(['BRO', 'LUA', 'BRO', 2015, 1978]),  # fail 8
        main(['BRO', 'RDOC', 'BRO', 2015, 1978]),  # fail 9

        main(['BRO', 'LUA', 'BRO', 2015, 2006]),  # fail 10
        main(['BRO', 'LUA', 'BRO', 2015, 1966]),  # fail 11

        main(['J', 'GRACE', 'UNO', 1983, 1978]),  # 12
        main(['J', 'LUA', 'UNO', 1975, 1978]),  # 13
    )

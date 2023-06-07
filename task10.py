class MealyError(Exception):
    pass


class Mealy:
    c = 'A'

    def spin(self):
        match self.c:
            case 'A':
                self.c = 'B'
                return 0
            case 'B':
                self.c = 'E'
                return 3
            case 'C':
                self.c = 'D'
                return 4
            case 'D':
                self.c = 'E'
                return 5
            case 'E':
                self.c = 'F'
                return 6
            case _:
                raise MealyError

    def punch(self):
        match self.c:
            case 'B':
                self.c = 'C'
                return 1
            case 'E':
                self.c = 'A'
                return 7
            case 'F':
                self.c = 'G'
                return 9
            case _:
                raise MealyError

    def stand(self):
        match self.c:
            case 'B':
                self.c = 'G'
                return 2
            case 'E':
                self.c = 'G'
                return 8
            case _:
                raise MealyError


def main():
    return Mealy()


def test():
    o = main()
    assert o.spin() == 0
    assert o.punch() == 1
    assert o.spin() == 4
    assert o.spin() == 5
    assert o.punch() == 7
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.spin() == 6
    assert o.punch() == 9
    o = main()
    assert o.spin() == 0
    assert o.stand() == 2
    o = main()
    assert o.spin() == 0
    assert o.spin() == 3
    assert o.stand() == 8
    try:
        o.spin()
    except Exception as e:
        assert type(e) == MealyError
    try:
        o.stand()
    except Exception as e:
        assert type(e) == MealyError
    try:
        o.punch()
    except Exception as e:
        assert type(e) == MealyError


if __name__ == '__main__':
    test()

def main(s):
    i = int(s)
    c1 = 0b1111111 & i
    c2 = 0b1111111111 & (i >> 7)
    c3 = 0b11 & (i >> 17)
    c5 = 0b111111111 & (i >> 27)
    return tuple(map(str, (c1, c2, c3, c5)))


if __name__ == '__main__':
    print(main('51593330143'),
          main('51755522310'),
          main('33813465578'),
          main('30103671231')
          )

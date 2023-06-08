def main(s):
    i = int(s[0], base=16) | (int(s[1], base=16) << 5) | \
        (int(s[2], base=16) << 11) | (int(s[3], base=16) << 12)
    i = hex(i)
    return i


if __name__ == '__main__':
    print(main(('0x1f', '0x1f', '0x1', '0x5')))

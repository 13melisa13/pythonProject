import re


def main(x):
    p = r"\[\[\s*variable\s*list\(\s*([^)]*)\)\s*=>\s*([^.]*)"
    ls1 = re.findall(p, x)
    final = []
    for one in ls1:
        set_of_one = re.split(r"\.", one[0])
        ls = []
        for one_set_of_one in set_of_one:
            ls.append(int(one_set_of_one))
        one_tuple = tuple([one[1], ls])
        final.append(one_tuple)
    return final


if __name__ == '__main__':
    print(main("\begin [[ variable list(-8983 . 6385 )=>aoren_461. ]], [[variable\n" +
               "list( -6192 . 4321 . -1780 . 955) =>riuser_156. ]],[[ variable\n" +
               "list(-9612 . -2556) =>eres.]], [[ variable list( -9853 . -4639 . -2997\n" +
               ") => zaisa_42. ]], \end"))

import re


def main(s):
    p = r"<section>\s*glob\s*\"([^\"]*)\"\s*([^<]*)"
    ls1 = re.findall(p, s)
    d = dict(ls1)
    for item in d:
        d[item] = int(d[item])
    return d


if __name__ == '__main__':
    print(main("[[ <section> glob \"rile_573\" -1669 </section>, <section>" +
               "glob\n\"orsoma\" -8239</section>, <section> glob \"enedbe_386\" 7778 </section>,\n" +
               "<section> glob \"quat_134\" 8510 </section>, ]]"))

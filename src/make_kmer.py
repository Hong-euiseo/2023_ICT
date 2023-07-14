import sys


def make_kmer(l1: list, l2: list, n: int):
    if n == 1:
        return l2

    l = list()
    for s1 in l1:
        for s2 in l2:
            l.append(s1 + s2)

    return make_kmer(l1, l, n - 1)


if __name__ == "__main__":
    n = int(sys.argv[1])
    l1 = ["A", "T", "G", "C"]
    l2 = ["A", "T", "G", "C"]

    res = make_kmer(l1, l2, n)
    print(res)

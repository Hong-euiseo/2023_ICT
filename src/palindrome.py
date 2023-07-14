import make_kmer


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


l1 = ["A", "T", "G", "C"]
l2 = ["A", "T", "G", "C"]
mer7 = make_kmer.make_kmer(l1, l2, 7)

cnt = 0
for mer in mer7:
    if is_palindrome(mer):
        cnt += 1

print(cnt)

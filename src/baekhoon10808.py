S = input()

import string

alpha = [i for i in string.ascii_lowercase]
data = {}
for i in alpha:
    if i not in data:
        data[i] = 0

for string in S:
    if string in data:
        data[string] += 1

for value in data:
    print(data[value], end=" ")

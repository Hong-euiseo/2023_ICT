S = input()
# S = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
data = {"A": 0, "C": 0, "G": 0, "T": 0}

for char in S:
    data[char] += 1

for value in data:
    print(data[value], end=" ")

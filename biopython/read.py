filepath = "NC_045512.2.fasta"

data = {}
with open(filepath) as handle:
    _ = handle.readline()
    for line in handle:
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1
print(data)

length = 0
for base, cnt in data.items():
    print(f"{base} : {cnt}")
    length += cnt
print(length)

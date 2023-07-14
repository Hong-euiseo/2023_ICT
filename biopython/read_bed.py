filepath = "test.bed"

chrom = ""
data = {}
with open(filepath, "rt") as handle:
    for line in handle:
        lines = line.strip().split("\t")
        chrom = lines[0]
        if chrom not in data:
            data[chrom] = 0
        data[chrom] += int(lines[2]) - int(lines[1])

for chrom, bp in data.items():
    print(f"{chrom}: {bp}")

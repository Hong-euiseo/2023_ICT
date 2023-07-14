filepath = "sample.vcf"

pass_cnt = 0
row_cnt = 0
data = {}
with open(filepath, "rt") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        if line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue

        row = line.strip().split("\t")
        if row[filter_idx] == "PASS":
            pass_cnt += 1

        row_cnt += 1

        gt = row[-1].split(":")[0]
        if gt not in data:
            data[gt] = 0
        data[gt] += 1

        if row[2] != ".":
            for alt in row[4].split(","):
                print(f"{row[0]}-{row[1]}-{row[3]}-{alt}-{row[2]}")

# print(f"PASS: {pass_cnt}/{row_cnt} ({round((pass_cnt/row_cnt)*100,2)}%)")

# for gt, val in data.items():
#     print(f"{gt}: {val}")

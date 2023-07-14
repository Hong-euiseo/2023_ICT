import gzip

filepath = "sample.fastq.gz"

cnt = 0
Q20 = 0
Q30 = 0
Q_total = 0
total_cnt = 0
with gzip.open(filepath, "rt") as handle:
    for line in handle:
        lines = line.strip()
        cnt += 1
        if cnt % 4 == 0:
            for qual in lines:
                total_cnt += 1
                Q_total += ord(qual) - 33
                if ord(qual) - 33 >= 30:
                    Q30 += 1
                if ord(qual) - 33 >= 20:
                    Q20 += 1

print(f"Quality Average : {round(Q_total/total_cnt, 2)}")
print(f"Q20(%) : {round((Q20 / total_cnt) * 100,2)}")
print(f"Q30(%) : {round((Q30 / total_cnt) * 100,2)}")

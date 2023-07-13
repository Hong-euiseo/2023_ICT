from Bio import SeqIO

filepath = "NC_045512.2.fasta"
record = SeqIO.read(filepath, "fasta")
# print(record)

data = dict()
for base in record.seq:
    if base not in data:
        data[base] = 0
    data[base] += 1
# print(data)
# print(len(record.seq))

import seaborn as sns
import matplotlib.pyplot as plt

df = {"BASE": [], "COUNT": []}
for base, cnt in data.items():
    df["BASE"].append(base)
    df["COUNT"].append(cnt)
# print(df)

sns.barplot(x="BASE", y="COUNT", data=df)
plt.title("Covid-19 base count", fontdict={"size": 16})
plt.xlabel("BASE")
plt.ylabel("COUNT")
plt.savefig("base_barplot.png")

import gzip

filepath = "NC_045512.2.fasta.gz"
with gzip.open(filepath, "rt") as handle:
    print(handle.readline())
    print(handle.readline())

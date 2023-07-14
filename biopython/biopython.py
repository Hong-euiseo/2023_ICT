from Bio.Seq import Seq

### type check
# seq = Seq("ATGTCATAG")
# print(seq)
# print(type(seq))

### commends
# print(seq.count("A"))
# print(seq.lower())

# print(seq.transcribe())
# print(seq.translate())

# print(seq.complement())
# print(seq.reverse_complement())

### check gc contents
# gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
# print(round(gc, 2))

### commends 2
# seq2 = Seq("tataaaggcAATATGCAGTAG")
# print(seq2.upper())
# print(seq2.lower())

# seq3 = Seq("AUGAACUAAGUUUAGAAU")
# print(seq3.translate())
# print(seq3.translate(to_stop=True))

### see codon
# res = seq3.translate()
# codon = res.split("*")
# for idx, value in enumerate(codon, start=1):
#     print(f"{idx}: {value}")

### melting temperature comparison
# from Bio.SeqUtils import MeltingTemp as mt

# seq1 = Seq("AGTCTGGGACGGCGCGGCAATCGCA")
# seq2 = Seq("TTCCTAAGACGAATCGGCTATACGC")
# tm1 = mt.Tm_Wallace(seq1)
# tm2 = mt.Tm_Wallace(seq2)

# if tm1 > tm2:
#     print(seq1, ">", seq2)
#     print(tm1, ">", tm2)
# else:
#     print(seq1, "<", seq2)
#     print(tm1, "<", tm2)

### sequence record
# from Bio.SeqRecord import SeqRecord

# seq = Seq("ACGT")
# seq_record = SeqRecord(
#     seq,
#     id="NC_1234",
#     name="test_name",
#     description="test_description",
#     features=["feature 1", "feature 2"],
# )

# seq_record.id = "NC_5678"
# seq_record.name = "test_name_2"
# seq_record.description = "test_description_2"
# seq_record.features.append("feature 3")

# print(seq_record)

### sequence from fasta
from Bio import SeqIO

# record = SeqIO.read("NC_045512.2.fasta", "fasta")
# print(record)

# records = SeqIO.parse("test.fasta", "fasta")
# for record in records:
#     print(record)
#     print("-----")

### sequence from fastq
# cnt = 0
# records = SeqIO.parse("sample.fastq", "fastq")
# for record in records:
#     cnt += 1
# print(cnt)

# import gzip

# cnt = 0
# handle = gzip.open("sample.fastq.gz", "rt")
# records = SeqIO.parse(handle, "fastq")
# for record in records:
#     cnt += 1
# print(cnt)

### sequence from genbank
# gbk = SeqIO.read("NC_045512.2.gb", "genbank")
# print(gbk.id)
# print(gbk.description)
# print(gbk.annotations["molecule_type"])
# print(gbk.annotations["organism"])

### sequence from Entrez
from Bio import Entrez


def entrez_runner(ncbi_id):
    Entrez.email = "your@email.com"
    handle = Entrez.efetch(db="nucleotide", rettype="gb", id=ncbi_id)

    write_filepath = f"{ncbi_id}.genbank"
    with open(write_filepath, "w") as fw:
        for line in handle:
            fw.write(line)

    print(f"#DONE :: {write_filepath}")


# entrez_runner("NC_045512.2")


def entrez_runner_fasta(ncbi_id):
    Entrez.email = "your@email.com"
    handle = Entrez.efetch(db="nucleotide", rettype="fasta", id=ncbi_id)

    write_filepath = f"{ncbi_id}.fasta"
    with open(write_filepath, "w") as fw:
        for line in handle:
            fw.write(line)

    print(f"#DONE :: {write_filepath}")

# read method 1
filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\read_sample.txt"
seq = ""
with open(filepath) as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        seq += line.strip()
print(seq)

# write method 1
filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\write_sample.txt"
contents = [">A_Strain", "ATGCGGAAG", "TCGGGATAG"]
with open(filepath, "w") as handle:
    handle.write("\n".join(contents))

# write with A, C, G, T counts
filepath2 = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\write_result.txt"
with open(filepath2, "w") as handle:
    handle.write(f"A : {seq.count('A')}\n")
    handle.write(f"C : {seq.count('C')}\n")
    handle.write(f"G : {seq.count('G')}\n")
    handle.write(f"T : {seq.count('T')}\n")

# write with A, C, G, T count faster
filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\write_sample.txt"
seq = ""
A, C, G, T = 0, 0, 0, 0
with open(filepath, "r") as handle:
    for line in handle:
        if line.startswith(">"):
            continue
        A += line.count("A")
        C += line.count("C")
        G += line.count("G")
        T += line.count("T")

filepath2 = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\write_result.txt"
with open(filepath2, "w") as handle:
    handle.write(f"A : {A}\n")
    handle.write(f"C : {C}\n")
    handle.write(f"G : {G}\n")
    handle.write(f"T : {T}\n")

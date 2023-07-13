# gene_expr = [3.14, 11.82, 7.44, 1.92]
# codon = ["ATG", "GGC", "TGA", "CCT"]

# new_list = gene_expr + codon
# print(new_list)

l = [3, 1, 1, 2, 0, 0, 2, 3, 3]
l_unique = set(l)
print(l_unique)
for elem in l_unique:
    print(elem)

# new_list = list()
# for elem in l:
#     if elem not in new_list:
#         new_list.append(elem)
# print(new_list)

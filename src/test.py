import json

# filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\test.csv"

# data = list()
# with open(filepath) as handle:
#     header = handle.readline().strip().split(",")
#     print(header)
#     for line in handle:
#         row = line.strip().split(",")
#         data.append(dict(zip(header, row)))

# print(json.dumps(data, indent=2))


# min_val = float(data[0]["VALUE"])
# min_gene = data[0]["GENE"]
# max_val = float(data[0]["VALUE"])
# max_gene = data[0]["GENE"]
# for elem in data:
#     if min_val > float(elem["VALUE"]):
#         min_val = float(elem["VALUE"])
#         min_gene = elem["GENE"]
#     if max_val < float(elem["VALUE"]):
#         max_val = float(elem["VALUE"])
#         max_gene = elem["GENE"]

# print(min_gene, min_val)
# print(max_gene, max_val)
filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\test.csv"
data = list()
with open(filepath) as handle:
    header = handle.readline().strip().split(",")
    for line in handle:
        row = line.strip().split(",")
        data.append(dict(zip(header, row)))
print(data)

filepath = "C:\\Users\\user\\Desktop\\2023_ICT교육\\2023_ICT\\test3.json"
with open(filepath, "w") as handle:
    json.dump(data, handle, indent=2)

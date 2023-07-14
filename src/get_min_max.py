l = [3, 1, 1, 2, 0, 0, 2, 3, 3]

min_val = l[0]
max_val = l[0]

for n in l:
    if n < min_val:
        min_val = n
    if n > max_val:
        max_val = n
print(min_val)
print(max_val)

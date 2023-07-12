string = input()
count = 0

while string != "#":
    for i in range(len(string)):
        if "a" in string[i]:
            count += 1
        elif "e" in string[i]:
            count += 1
        elif "i" in string[i]:
            count += 1
        elif "o" in string[i]:
            count += 1
        elif "u" in string[i]:
            count += 1
    print(count)

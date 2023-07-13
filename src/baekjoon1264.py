while True:
    string = input()
    if string == "#":
        break
    else:
        count = 0
        string = string.lower()
        for i in range(len(string)):
            if string[i] == "a":
                count += 1
            elif string[i] == "e":
                count += 1
            elif string[i] == "i":
                count += 1
            elif string[i] == "o":
                count += 1
            elif string[i] == "u":
                count += 1
        print(count)

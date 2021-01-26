def cyclisch(char, num):
    bin = "".join(format(ord(item), "b") for item in char)
    new_bin = ""
    if num > 0:
        new_bin = bin[num:]
        for int_char in range(0, num):
            new_bin += bin[int_char]
    else:
        for int_char in range(len(bin) - 1, abs(num), -1):
            new_bin += bin[int_char]
        new_bin += bin[:num]
    return print(new_bin)

cyclisch("x", 3)
cyclisch("x", -3)
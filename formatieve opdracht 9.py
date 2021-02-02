
def cyclisch(char, num):
    # Verandert de string in binary
    bin_code = "".join(format(ord(item), "b") for item in char)
    # Return bin_code van af num tot einde plus bin_code van het begin tot num
    return chr(int((bin_code[num:] + bin_code[:num]), 2))

print(cyclisch("x", 3))
print(cyclisch("x", -3))


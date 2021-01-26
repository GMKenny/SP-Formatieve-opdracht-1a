def ceasercijfers():
    input_string = str(input("Geef een tekst:"))
    input_num = int(input("Geef een rotatie:"))
    alfabeth = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    new_string = ""
    for item in input_string:
        for index, alfabeth_item in enumerate(alfabeth):
            if item == alfabeth_item:
                new_num = index + input_num
                while new_num > 26:
                    new_num -= 26
                new_string += alfabeth[new_num-1]
                break
    return new_string
print(ceasercijfers())
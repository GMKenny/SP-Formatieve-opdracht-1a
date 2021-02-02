def ceasercijfers():
    input_string = str(input("Geef een tekst:"))
    input_num = int(input("Geef een rotatie:"))
    alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    new_string = ""
    # Voor elke item in input_string
    for item in input_string:
        # Voor elke item in alfabet, pak item en nummer op
        for index, alfabet_item in enumerate(alfabet):
            # Als item gelijk is aan het alfabeth_item
            if item == alfabet_item:
                # New_num is het nieuwe index nummer
                new_num = index + input_num
                # Zolang het index nummer boven de 26 is. Lenght van het alfabet
                while new_num > 26:
                    new_num -= 26
                new_string += alfabet[new_num]
                # Stop voor loop als het gevonden is
                break
    return new_string

print(ceasercijfers())
import random

def random_int():
    # ?
    answer = random.randint(0, 10)
    print("Gok een getal tussen 0 en 10")
    input_int = int(input("Voer de keuze in:"))
    while answer != input_int:
        input_int = int(input("Voer de keuze in:"))
    print(input_int, "is goed gegokt")

random_int()
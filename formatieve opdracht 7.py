import random

def random_int():
    # Maak een random getal van 0 tot 10
    answer = str(random.randint(0, 10))
    print("Gok een getal tussen 0 en 10")
    input_int = ""
    # Zolang het antwoord niet gelijk is aan de input
    while answer != input_int:
        input_int = input("Voer de keuze in:")
    print(input_int, "is goed gegokt")

random_int()
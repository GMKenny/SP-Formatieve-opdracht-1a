num = int(input("Hoe groot moet de piramide?"))

# Opdracht 1
def print_pyramid(index):
    # Voor elk nummer in de range van 1 tot index
    for num in range(1, index):
        # Print "*" keer het huidige nummer
        print("*" * num)
    # Voor elk nummer vanaf index tot 0
    for num in range(index, 0, -1):
        # Print "*" keer het huidige nummer
        print("*" * num)


def print_pyramid_while(index):
    counter = 0
    # Zolang counter niet gelijk is aan de gegeven index
    while counter != index:
        # Counter is counter plus 1
        counter += 1
        # Print "*" keer de counter
        print("*" * counter)
    counter = index - 1
    # Zolang counter niet gelijk is aan 0
    while counter != 0:
        # Print "*" keer de counter
        print("*" * counter)
        counter -= 1


print_pyramid(num)
print_pyramid_while(num)

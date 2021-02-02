def fizzbuzz():
    # Voor elke nummer in range van 1 tot 100
    for index in range(1, 101):
        # Als het nummer modulo drie null is en nummer modulo Vijf null is
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
            # Ga verder met de loop
            continue
        # Als het nummer modulo vijf null is
        elif index % 5 == 0:
            print("buzz")
            continue
        # Als het nummer modulo drie null is
        elif index % 3 == 0:
            print("fizz")
            continue
        print(index)


def fizzbuzz_two():
    # Voor elke nummer in range van 1 tot 100
    for index in range(1, 101):
        string = ""
        # Als het nummer modulo drie null is
        if index % 3 == 0:
            string += "fizz"
        # Als het nummer modulo vijf null is
        elif index % 5 == 0:
            string += "buzz"
        else:
            print(index)
            continue
        print(string)


fizzbuzz()
fizzbuzz_two()
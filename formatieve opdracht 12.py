
def fizzbuzz():
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print("fizzbuzz")
            continue
        elif index % 5 == 0:
            print("buzz")
            continue
        elif index % 3 == 0:
            print("fizz")
            continue
        print(index)


def fizzbuzz2():
    for index in range(1, 101):
        string = ""
        if index % 3 == 0:
            string += "fizz"
        elif index % 5 == 0:
            string += "buzz"
        else:
            print(index)
            continue
        print(string)


fizzbuzz()
fizzbuzz2()

string_one = input("Voer een palindroom in of niet:")

def palindroom_one(string):
    # Is string gelijk aan string omgekeerd.
    return string == string[::-1]


def palindroom_two(string):
    # Als de lengte van de string kleiner is dan 1
    if len(string) < 1:
        return True
    # Als het eerst karakter en laatse karakter gelijk zijn aan elkaar
    if string[0] == string[-1]:
        # Herhaal functie min het eerste index en de laatse index
        return palindroom_two(string[1:-1])
    return False


print(palindroom_one(string_one))
print(palindroom_two(string_one))

test_lijst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]

def count(lst, target):
    # Als de lengte van de lijst gelijk is aan 0
    if len(lst) == 0:
        return 0
    # Als item op de eerste plek gelijk is aan het target
    if lst[0] == target:
        # return 1 plus functie count min het eerste getal
        return 1 + count(lst[1:], target)
    # return functie count min het eerste getal
    return count(lst[1:], target)

def count2(lst, target):
    # Variable count == 0
    count = 0
    # Voor elke element in lst
    for item in lst:
        # Als item gelijk is aan target
        if item == target:
            # Count plus 1
            count += 1
    return count


def diff(list):
    # Variable diff is 0
    diff = 0
    # Voor element van 0 tot lengte van de lijst min 1
    for index in range(0, (len(list) - 1)):
        # eerste item min het volgende item
        # abs keert een negatief naar een positief
        check = abs(list[index] - list[index + 1])
        # Als check groter is dan het grooste verschil
        if check > diff:
            diff = check
    return print("Het grooste verschil is:", diff)


def zero_one_list_check(lst):
    ones = count(lst, 1)
    zeros = count2(lst, 0)
    if ones > zeros and zeros < 12:
        return print("De lijst voldoet aan de eisen")
    return print("De lijst voldoet niet aan de eisen")


diff(test_lijst)
zero_one_list_check(test_lijst)
test_lijst = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8]

def count(lst, target):
    if len(lst) == 0:
        return 0
    if lst[0] == target:
        return 1 + count(lst[1:], target)
    else:
        return count(lst[1:], target)

def count2(lst, target):
    count = 0
    for item in lst:
        if item == target:
            count += 1
    return count


def diff(list):
    diff = 0
    for index in range(0, (len(list) - 1)):
        check = list[index] - list[index + 1]
        if abs(check) > diff:
            diff = abs(check)
    return print("Het grooste verschil is:", diff)


def diff2(list):
    if len(list) < 1:
        return 0
    if len(list) == 1:
        return list[0]
    next_list = abs(diff2(list[2:]))
    if abs(list[0] - list[1]) < next_list:
        return abs(next_list)
    else:
        return abs(list[0] - list[1])


def zero_one_list_check(lst):
    ones = count(lst, 1)
    zeros = count2(lst, 0)
    if ones > zeros:
        if zeros < 12:
            return print("De lijst voldoet aan de eisen")
    return print("De lijst voldoet niet aan de eisen")

print(diff2(test_lijst))
diff(test_lijst)
zero_one_list_check(test_lijst)
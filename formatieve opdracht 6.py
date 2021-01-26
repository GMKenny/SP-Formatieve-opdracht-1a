test_list_tree = [5, 5, 4, 6]


def gemiddelde(list):
    if len(list) == 0:
        return 0
    lenght = len(list)
    return (list[0] + (lenght - 1) * gemiddelde(list[1:])) // lenght


def gemiddelde2(list):
    # Kan ook met een For loop
    gem = sum(list) // len(list)
    return gem

print(gemiddelde(test_list_tree))
print(gemiddelde2(test_list_tree))
test_list_tree = [5, 5, 4, 6]


def gemiddelde(list):
    # Als de lengte van de lijst 0 is
    if len(list) == 0:
        return 0
    lenght = len(list)
    # Het element op index 0 + het gemiddelde van af index 1
    # De lengte van de lijs wordt * de uitkomt van functie gedaan anders word bij iedere loop het gedeelt.
    return (list[0] + ((lenght - 1) * gemiddelde(list[1:]))) // lenght


def gemiddelde2(list):
    # Totaal van de lijst min de lengte van de lijst
    gem = sum(list) // len(list)
    return gem

print(gemiddelde(test_list_tree))
print(gemiddelde2(test_list_tree))
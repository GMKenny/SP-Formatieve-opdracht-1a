input_string = str(input("Geef een string:"))
input_string_two = str(input("Geef tweede string:"))


def similar(string, string_two):
    # Pak de kleinste lengte van de 2 strings
    range_list = min(len(string), len(string_two))
    # Geef index nummer 0 tot met de lengte van de kleinste string
    for index in range(0, range_list):
        # Als karakter van string niet gelijk is aan de karakter van string_two
        if string[index] != string_two[index]:
            # return index
            return print("Het verschil zit op index", index)
    # Als de lengte van string niet gelijk is aan de lengte van string_two
    if len(string) != len(string_two):
        # return lengte van de kleinste lijst, zonder min 1.
        return print("Het verschil zit op index:", range_list)
    # return er is geen verschil
    return print("Er is geen verschil")


similar(input_string, input_string_two)

input_string = str(input("Geef een string:"))
input_string_two = str(input("Geef tweede string:"))


def similar(string, string_two):
    range_list = min(len(string), len(string_two))
    for index in range(0, range_list):
        if string[index] != string_two[index]:
            return print("Het Verschil zit op  index", index)
    if len(string) != len(string_two):
        return print("Het verschil zit op index:", range_list)
    else:
        return print("Er is geen verschil")


similar(input_string, input_string_two)

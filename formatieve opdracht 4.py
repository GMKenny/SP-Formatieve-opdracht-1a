
string_one = input("Voer een pandindroom in of niet:")

def palindroom_one(string):
    reverse_string = "".join(reversed(string))
    if reverse_string == string:
        return print(string, "Is een palindroom.")
    return print(reverse_string, "Is geen palindroom")


def palindroom_two(string, original):
    if len(string) <= 1:
        return print(original, "Is een palindroom.")
    if string[0] == string[-1]:
        return palindroom_two(string[1:-1], original)
    return print(original, "Is geen palindroom")


palindroom_one(string_one)
palindroom_two(string_one, string_one)

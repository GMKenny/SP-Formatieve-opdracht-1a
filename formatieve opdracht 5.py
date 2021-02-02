list_sort_one = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list_sort_two = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def sort_list(list):
    # Omgekeerd.
    copy_list = list.copy()
    # Voor index van af de lengthe van de lijst tot aan he begin van de lijst
    for index in range(len(copy_list) - 2, -1, -1):
        # kopie van het element op het huidige index
        copy_index = copy_list[index]
        index_grens = index
        # Zolang index_grens kleiner is of gelijk aan de lenghte van de lijst en
        # Het element op de indexgrens groter is als het element op index grens plus 1
        while index_grens <= len(copy_list) - 2 and copy_list[index_grens] > copy_list[index_grens + 1]:
            # Element index grens wordt het volgende element
            copy_list[index_grens] = copy_list[index_grens + 1]
            # Het volgende nummer word het huidige element
            copy_list[index_grens + 1] = copy_index
            index_grens += 1
    return copy_list


print(sort_list(list_sort_one))
print(sort_list(list_sort_two))
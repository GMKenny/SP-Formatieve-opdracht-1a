list_sort_one = [9, 8, 7, 6, 5, 4, 3, 2, 1]
list_sort_two = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

def sort_list(list):
    # Omgekeerd
    copy_list = list.copy()
    for index in range(len(copy_list) - 2, -1, -1):
        copy_index = copy_list[index]
        index_grens = index
        while index_grens <= len(copy_list) - 2 and copy_list[index_grens] > copy_list[index_grens + 1]:
            copy_list[index_grens] = copy_list[index_grens + 1]
            copy_list[index_grens + 1] = copy_index
            index_grens += 1
    return copy_list


print(sort_list(list_sort_one))
print(sort_list(list_sort_two))
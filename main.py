def testing(list):
    expected_list = [2, 3, 5, 6, 7, 8]
    if (list == expected_list):
        return True
    else:
        return False


def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(len(list) - 1):
            if (list[j] > list[j + 1]):
                list[j] = list[j + 1]
                list[j + 1] = list[j]
    return list


def main():
    list = [5, 3, 8, 6, 7, 2]
    sorted_list = bubble_sort(list)
    print("The sorted list is: ", sorted_list)
    print("Does it work?", testing(sorted_list))


main()

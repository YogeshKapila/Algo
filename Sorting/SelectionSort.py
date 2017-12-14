"""
Sort an Array.
Algorithm: Selection Sort.
"""


def selection_sort(input_list):
    """
    Selection Sort Implementation
    :param input_list:
    :return: Sorted Input List
    """
    length = len(input_list)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if input_list[j] < input_list[min_index]:
                min_index = j
        if min_index != i:
            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

    return input_list


if __name__ == "__main__":
    print(selection_sort([2, 3, 1, 1, 2, 2, 4, 0, -1.5, 3.5, -1, -112, 10000]))

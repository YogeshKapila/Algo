"""
Sort an Array.
Algorithm: Insertion Sort.
"""


def insertion_sort(input_list):
    """
    Insertion Sort Implementation
    :param input_list:
    :return: Sorted Input List
    """
    length = len(input_list)
    for i in range(1, length):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1

        input_list[j + 1] = key

    return input_list


if __name__ == "__main__":
    print(insertion_sort([2, 3, 1, 1, 2, 2, 4, 0, -1.5, 3.5, -1, -112, 10000, 2]))

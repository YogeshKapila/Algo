"""
Sort an Array.
Algorithm: Bubble Sort.
"""


def bubble_sort(input_list):
    """
    Bubble Sort Implementation
    :param input_list: Input List
    :return: Sorted Input List
    """
    length = len(input_list)

    for i in range(length):
        swapped = False
        for j in range(length - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if not swapped:
            break

    return input_list


if __name__ == "__main__":
    print(bubble_sort([2, 3, 1, 1, 2, 2, 4, 0, -1.5, 3.5, -1, -112, 10000]))

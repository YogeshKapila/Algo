"""
Given a sorted array of n elements, write a function to search a given element x in it.
Algorithm: Binary Search
"""


def binary_search(input_list, rightmost_index, leftmost_index, to_find):
    """
    Binary Search implementation.
    :param input_list: Input List
    :param rightmost_index: Rightmost index of the list
    :param leftmost_index: Leftmost index of the list
    :param to_find: Element to be searched for
    :return: Index of the element Or -1 if not found
    """

    if rightmost_index >= leftmost_index:
        middle_index = int((rightmost_index + leftmost_index) / 2)

        if to_find == input_list[middle_index]:
            print("{} found at position {}".format(to_find, middle_index))
            return middle_index

        elif to_find > input_list[middle_index]:
            return binary_search(input_list, rightmost_index, middle_index + 1, to_find)

        else:
            return binary_search(input_list, middle_index - 1, leftmost_index, to_find)

    print("{} was not found in the given list".format(to_find))
    return -1


if __name__ == "__main__":
    help(binary_search)
    test_list = range(10, 10000, 10)
    print(len(test_list))
    print("Returned Index: ", binary_search(test_list, len(test_list) - 1, 0, 400))
    print("Returned Index: ", binary_search(test_list, len(test_list) - 1, 0, 121))

"""
Given a sorted array of n elements, write a function to search a given element x in it.
Algorithm: Exponential Search
"""


# Helper Function
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

    print("{} is not present in the given list.".format(to_find))
    return -1


def exponential_search(input_list, to_find):
    """
    Exponential Search Implementation
    :param input_list: Input List
    :param to_find: Element to be searched for
    :return: Index of the element Or -1 if not found
    """
    length = len(input_list)
    interval_indices = [2**i - 1 for i in range(length) if 2**i <= length]
    interval_indices.append(length - 1)

    for index in interval_indices:
        if to_find == input_list[index]:
            print("{} found at position {}".format(to_find, index))
            return index

        elif to_find > input_list[index]:
            continue

        elif to_find < input_list[index]:
            stop_index = index
            start_index = interval_indices[interval_indices.index(index) - 1]
            return binary_search(input_list, stop_index, start_index, to_find)

    print("{} is not present in the given list.".format(to_find))
    return -1


if __name__ == "__main__":
    help(exponential_search)
    test_list = range(10, 1000, 10)
    print(len(test_list))
    print("Returned Index: ", exponential_search(test_list, 90))
    print("Returned Index: ", exponential_search(test_list, 951))
"""
Given an array of n elements, write a function to search a given element x.
Algorithm: Linear Search
"""


def linear_search(input_list, to_find):
    """
    Linear Search Implementation.
    :param input_list: Input List
    :param to_find: Element to be searched for
    :return: Index of the element Or -1 if not found
    """
    for elem in input_list:
        if elem == to_find:
            index = input_list.index(to_find)
            print("{} found at position {}".format(to_find, index))
            return index

    print("{} is not present in the given list.".format(to_find))
    return -1


if __name__ == "__main__":
    help(linear_search)
    test_list = [1, 9, 4, 3, 7, 8, 5]
    print("Returned Index: ", linear_search(test_list, 4))
    print("Returned Index: ", linear_search(test_list, 20))


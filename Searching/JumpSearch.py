"""
Given a sorted array of n elements, write a function to search a given element x in it.
Algorithm: Jump Search
"""
import math


def jump_search(input_list, to_find):
    """
    Jump Search Implementation.
    :param input_list: Input List
    :param to_find: Element to be searched for
    :return: Index of the element Or -1 if not found
    """
    length = len(input_list)
    jump_size = int(math.sqrt(length))
    search_start_index = None
    search_end_index = None

    for i in range(0, length, jump_size):
        if to_find == input_list[i]:
            print("{} found at position {}".format(to_find, i))
            return i

        elif to_find > input_list[i]:
            if ((length - 1) - i) > jump_size:
                continue
            else:
                search_start_index = i
                search_end_index = length

        if not (search_start_index and search_end_index):
            search_start_index = i - jump_size
            search_end_index = i

        if search_start_index < 0:
            print("{} is not present in the given list.".format(to_find))
            return -1

        for j in range(search_start_index, search_end_index):
            if to_find == input_list[j]:
                print("{} found at position {}".format(to_find, j))
                return j

    print("{} is not present in the given list.".format(to_find))
    return -1


if __name__ == "__main__":
    help(jump_search)
    test_list = range(10000)
    print(len(test_list))
    print("Returned Index: ", jump_search(test_list, 563))
    print("Returned Index: ", jump_search(test_list, 10000))

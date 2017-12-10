"""
Given a sorted array of n elements, write a function to search a given element x in it.
Algorithm: Interpolation Search
"""


def interpolation_search(input_list, to_find):
    """
    Interpolation Search Implementation
    :param input_list: Input List
    :param to_find: Element to be searched for
    :return: Index of the element Or -1 if not found
    """
    length = len(input_list)
    low = 0
    high = length - 1

    while (input_list[low] <= to_find <= input_list[high]) and high >= low:
        probe_pos = int(low + (to_find - input_list[low]) * (high - low) / (input_list[high] - input_list[low]))
        if input_list[probe_pos] == to_find:
            print("{} found at position {}".format(to_find, probe_pos))
            return probe_pos

        elif input_list[probe_pos] > to_find:
            high = probe_pos - 1
            if high < 0:
                break
            continue

        else:
            low = probe_pos + 1
            if low >= length:
                break
            continue

    return -1


if __name__ == "__main__":
    help(interpolation_search)
    test_list = range(10, 10000, 10)
    print(len(test_list))
    print("Returned Index: ", interpolation_search(test_list, 290))
    print("Returned Index: ", interpolation_search(test_list, -5))
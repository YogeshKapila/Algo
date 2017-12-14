"""
Sort an Array.
Algorithm: Merge Sort.
"""


def merge(input_list, left, middle, right):
    # Temp Lists
    L = input_list[left:(middle + 1)]
    R = input_list[(middle + 1):(right + 1)]
    print(L, R)

    len_L = len(L)
    len_R = len(R)

    i, j = 0, 0
    k = left

    while i < len_L and j < len_R:
        if L[i] < R[j]:
            input_list[k] = L[i]
            i += 1

        else:
            input_list[k] = R[j]
            j += 1

        k += 1

    while i < len_L:
        input_list[k] = L[i]
        i += 1
        k += 1

    while j < len_R:
        input_list[k] = R[j]
        j += 1
        k += 1


def merge_sort_helper(input_list, left, right):
    if left < right:
        middle = int((left + right) / 2)

        merge_sort_helper(input_list, left, middle)
        merge_sort_helper(input_list, middle + 1, right)
        merge(input_list, left, middle, right)


def merge_sort(input_list):
    """
    Merge Sort Implementation
    :param input_list:
    :return: Sorted Input List
    """
    merge_sort_helper(input_list, 0, len(input_list) - 1)
    return input_list


if __name__ == "__main__":
    print(merge_sort([2, 3, 1, 4, 0, 6]))

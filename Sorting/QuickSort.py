"""
Sort an Array.
Algorithm: Quick Sort.
"""


def partition(input_list, low, high):
    pivot = high
    pivot_val = input_list[pivot]
    j = low - 1
    for i in range(low, high):
        if input_list[i] < pivot_val:
            j += 1
            input_list[j], input_list[i] = input_list[i], input_list[j]

    input_list[j + 1], input_list[pivot] = input_list[pivot], input_list[j + 1]
    pivot = j + 1
    return pivot


def quick_sort_helper(input_list, low, high):
    if low < high:
        pivot = partition(input_list, low, high)

        quick_sort_helper(input_list, low, pivot - 1)
        quick_sort_helper(input_list, pivot + 1, high)


def quick_sort(input_list):
    """
    Quick Sort Implementation.
    :param input_list: Input List
    :return: Sorted Input List
    """
    quick_sort_helper(input_list, low=0, high=len(input_list) - 1)
    return input_list


if __name__ == "__main__":
    print(quick_sort([2, 3, 1, 1, 2, 2, 4, 0, -1.5, 3.5, -1, -112, 10000]))

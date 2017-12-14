"""
Sort an Array.
Algorithm: Merge Sort.
"""


def heapify(input_list, max_length, pos):
    largest = pos
    left = 2*pos + 1
    right = 2*pos + 2

    print(input_list, pos)

    if left < max_length and input_list[largest] < input_list[left]:
        largest = left

    if right < max_length and input_list[largest] < input_list[right]:
        largest = right

    # Swap largest and root
    if largest != pos:
        input_list[largest], input_list[pos] = input_list[pos], input_list[largest]

        # Perform recursive heapify for sub tree
        heapify(input_list, max_length, largest)


def heap_sort(input_list):
    """
    Heap Sort Implementation.
    :param input_list:
    :return: Sorted Input List
    """

    length = len(input_list)

    # Build Heap
    for i in range(int(length/2), -1, -1):
        heapify(input_list, length, i)

    # Sort
    for j in range(length - 1, -1, -1):
        input_list[j], input_list[0] = input_list[0], input_list[j]
        heapify(input_list, j, 0)

    return input_list


if __name__ == "__main__":
    print(heap_sort([12, 11, 13, 5, 6, 7, -1, 0, -1]))

"""
Find the length of the longest sub sequence of a given sequence such that all elements of the
sub sequence are sorted in increasing order.
Paradigm: Dynamic Programming
"""


def lis_util(input_list, n, result):

    for i in range(1, n):
        for j in range(i):
            if input_list[i] > input_list[j] and result[i] < result[j] + 1:
                result[i] = result[j] + 1

    lis_len = max(result)
    return lis_len


def longest_increasing_subsequence(input_list):
    length = len(input_list)
    result = [1] * length
    return lis_util(input_list, length, result)


if __name__ == '__main__':
    test_input_list = [50, 3, 10, 7, 40, 80]
    print(longest_increasing_subsequence(test_input_list))

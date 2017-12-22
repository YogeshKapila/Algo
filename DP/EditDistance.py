"""
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of
edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace

All of the above operations are of equal cost.

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations.
Replace 'n' with 'r', insert t, insert a
"""


# def edit_distance(str_1, str_2, m, n):
#     """
#     Simple Recursive
#     """
#     if m == 0:
#         return n
#
#     if n == 0:
#         return m
#
#     if str_1[m - 1] == str_2[n-1]:
#         return edit_distance(str_1, str_2, m - 1, n - 1)
#
#     else:
#         # 1 + min(insert, remove, replace)
#         return 1 + min(edit_distance(str_1, str_2, m, n - 1),
#                        edit_distance(str_1, str_2, m - 1, n),
#                        edit_distance(str_1, str_2, m - 1, n - 1))


def edit_distance(str_1, str_2, m, n):
    """
    DP
    """
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str_1[i - 1] == str_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = 1 + min(dp[i][j - 1],
                                   dp[i - 1][j],
                                   dp[i - 1][j - 1])

    return dp[m][n]


if __name__ == '__main__':
    test_str_1 = "sunday"
    test_str_2 = "saturday"
    print(edit_distance(test_str_1, test_str_2, len(test_str_1), len(test_str_2)))

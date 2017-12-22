"""
Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm}
valued coins, how many ways can we make the change? The order of coins doesn’t matter.
"""


# def count(input_arr, m, n):
#     """
#     Recursive Solution
#     """
#     if n == 0:
#         return 1
#
#     if n < 0:
#         return 0
#
#     if m <= 0 and n >= 1:
#         return 0
#
#     return count(input_arr, m - 1, n) + count(input_arr, m, n - input_arr[m - 1])


def count(input_arr, m, n):
    """
    DP Solution
    """
    dp = [[0 for x in range(m + 1)] for x in range(n + 1)]

    for i in range(m + 1):
        dp[0][i] = 1

    for i in range(1, n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - input_arr[j - 1]][j]

    return dp[n][m]


if __name__ == '__main__':
    arr = [1,2,3]
    m = len(arr)
    n = 4
    x = count(arr, m, n)
    print(x)

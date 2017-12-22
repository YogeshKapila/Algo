"""
Given a sequence of matrices, find the most efficient way to multiply these matrices together.
The problem is not actually to perform the multiplications, but merely to decide in which order
to perform the multiplications.

Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i].
We need to write a function MatrixChainOrder() that should return the minimum number of multiplications needed to
multiply the chain.
"""

from sys import maxsize


# def matrix_chain_order(input_arr, i, j):
#     """
#     Recursive Solution
#     """
#     if i == j:
#         return 0
#
#     minimum = maxsize
#
#     for k in range(i, j):
#         count = input_arr[i - 1]*input_arr[k]*input_arr[j] +\
#                 matrix_chain_order(input_arr, i, k) + matrix_chain_order(input_arr, k + 1, j)
#
#         minimum = min(minimum, count)
#
#     return minimum


def matrix_chain_order(input_arr, n):
    """
    DP Solution
    """
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            j = i + L - 1
            for k in range(i, j):
                dp[i][j] = maxsize
                cost = input_arr[i - 1]*input_arr[k]*input_arr[j] +\
                    dp[i][k] + dp[k + 1][j]

                dp[i][j] = min(dp[i][j], cost)

    return dp[1][n - 1]


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    n = len(arr)
    x = matrix_chain_order(arr, n)
    print(x)

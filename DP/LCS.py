"""
Given two sequences, find the length of longest subsequence present in both of them. A subsequence is a sequence that
appears in the same relative order, but not necessarily contiguous.
"""


# def lcs_util(seq_1, seq_2, n, m):
#     """ Recursive """
#     if n == 0 or m == 0:
#         return 0
#
#     if seq_1[n-1] == seq_2[m-1]:
#         return 1 + lcs_util(seq_1, seq_2, n - 1, m - 1)
#
#     return max(lcs_util(seq_1, seq_2, n, m - 1), lcs_util(seq_1, seq_2, n - 1, m))
#


def lcs_util(seq_1, seq_2, n, m):
    """DP"""
    helper = [[None] * (m + 1)] * (n + 1)

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                helper[i][j] = 0

            elif seq_1[i - 1] == seq_2[j - 1]:
                helper[i][j] = 1 + helper[i - 1][j - 1]
            else:
                helper[i][j] = max(helper[i - 1][j], helper[i][j-1])

    return helper[n][m]


def lcs(seq_1, seq_2):
    n = len(seq_1)
    m = len(seq_2)

    return lcs_util(seq_1, seq_2, n, m)

if __name__ == '__main__':
    test_seq_1 = "ABCDGH"
    test_seq_2 = "AEDFHR"
    print(lcs(test_seq_1, test_seq_2))
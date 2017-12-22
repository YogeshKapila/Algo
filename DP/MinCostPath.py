"""
Given a cost matrix cost[][] and a position (m, n) in cost[][],
write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).
"""


# def min_cost_path(input_arr, dest_x, dest_y):
#     if dest_x < 0 or dest_y < 0:
#         return 1e10
#     if dest_x == 0 and dest_y == 0:
#         return input_arr[dest_x][dest_y]
#
#     return input_arr[dest_x][dest_y] + min(min_cost_path(input_arr, dest_x - 1, dest_y),
#                                            min_cost_path(input_arr, dest_x, dest_y - 1),
#                                            min_cost_path(input_arr, dest_x - 1, dest_y - 1))


def min_cost_path(input_arr, dest_x, dest_y):
    size_x = len(input_arr)
    size_y = len(input_arr[0])
    result = [[0 for x in range(size_y)] for x in range(size_x)]

    result[0][0] = input_arr[0][0]

    for i in range(1, dest_x + 1):
        result[i][0] = input_arr[i][0] + result[i - 1][0]

    for j in range(1, dest_y + 1):
        result[0][j] = input_arr[0][j] + result[0][j - 1]

    for i in range(1, dest_x + 1):
        for j in range(1, dest_y + 1):

            result[i][j] = input_arr[i][j] + min(result[i - 1][j],
                                                 result[i - 1][j - 1],
                                                 result[i][j - 1])

    return result[dest_x][dest_y]


if __name__ == '__main__':
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    print(min_cost_path(cost, 1, 1))

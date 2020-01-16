# state = [[False for i in range(10)] for j in range(5)]
# print(state)
#
#
# def knapsack(weight, n, w):
#     state[0][0] = True
#     state[0][weight[0]] = True
#
#     for i in range(1, n):
#         for j in range(w):
#             if state[i - 1][j] is True:
#                 state[i][j] = state[i - 1][j]
#         for j in range(w - weight[i]):
#             if state[i - 1][j] is True:
#                 state[i][j + weight[i]] = True
#
#     for i in reversed(range(w)):
#         if state[n - 1][i] is True:
#             print(i)
#
#
# if __name__ == '__main__':
#     knapsack([2, 2, 4, 6, 3], 5, 9)
from qa_list import current_path
print(current_path)

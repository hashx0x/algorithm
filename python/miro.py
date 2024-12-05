# start (1,1)
# escape (n,m)
# miro (n,m)
# monster 0, not monster 1

from collections import deque

# 행렬
graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

n = 5
m = 6
stack = []

# 0이면 break, 1이면 +
# 돌아다니면서 1, 0 인지 체크만하면됨

result = 0


def inspect(x, y):
    queue = deque()
    queue.append((x, y))


# def inspect(x, y):
#     result = 0
#     if x < 0 or y < 0 or x >= n or y >= m:
#         return False

#     if x == n-1 and y == m-1:
#         return result

#     if graph[x][y] == 1:

#         result += 1

#         # 상, 하, 좌, 우
#         inspect(x-1, y)

#         inspect(x+1, y)

#         inspect(x, y-1)

#         inspect(x, y+1)
#     return result


# def main():
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if inspect(i, j) == True:
#                 result += 1

#     print(result)


# inspect(0, 0)

# 연결 요소 찾기

# n, m = map(int, input().split())
# y행 x열
graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

n = 4
m = 5


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1

        # 좌
        dfs(x - 1, y)
        # 우
        dfs(x + 1, y)
        # 상
        dfs(x, y+1)
        # 하
        dfs(x, y-1)
        return True
    return False


result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)

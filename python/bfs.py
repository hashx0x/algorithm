# bfs
# 큐 이용
from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

hashmapGraph = {
    0: [],
    1: [2,3,8]
};

visited = [False] * 9


def bfs(graph, start, visited):

    # 1번노드 큐에 삽입
    queue = deque([start])
    # 1번 노드 true
    visited[start] = True

    # queue 가 있는한 계속 반복
    while queue:
        # 큐에서 꺼냄
        v = queue.popleft()

        # print
        print(v, end='')

        # 큐에서 꺼낸 노드으 인접 노드들 중
        for i in graph[v]:

            # 아직 방문하지 않았다면
            if not visited[i]:

                # 큐에 넣음
                queue.append(i)

                # 큐에 넣으면서 방문처리
                visited[i] = True


# *
# 1 삽입
# 1번 방문처리
# while
# 큐에서 꺼내서
# 인접 노드 확인 후 방문하지 않았다면 큐에 넣음
# 큐에 넣으면서 방문처리
#
#
# *#

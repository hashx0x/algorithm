from collections import deque

Graph = dict[int, list[int]]

graph: Graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6],
}


def bfs_queue(graph: Graph, start_node):
    queue = deque([start_node])
    visited = []

    while queue:
        cur_visited = queue.popleft()
        visited.append(cur_visited)
        adjacents = graph[cur_visited]
        for adj_node in adjacents:
            if adj_node not in visited:
                queue.append(adj_node)

    return visited


print(bfs_queue(graph, 1))
# 답 : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

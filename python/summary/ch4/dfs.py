Graph = dict[int, list[int]]
graph: Graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9],
}
visited = []  # 방문한 걸 저장하기 위한 배열


def dfs_recursion(graph: Graph, cur_node: int, visited: list[int]):
    visited.append(cur_node)

    adjacents = graph[cur_node]

    for adjacent_node in adjacents:
        if adjacent_node not in visited:
            dfs_recursion(graph=graph, cur_node=adjacent_node, visited=visited)


def dfs_stack(graph: Graph, start_node: int):
    stack = [start_node]
    visited = []

    while stack:
        visited_node = stack.pop()
        visited.append(visited_node)
        adjacents = graph[visited_node]
        print(adjacents)
        for adjacent_node in adjacents:
            if adjacent_node not in visited:
                stack.append(adjacent_node)

    return visited


# dfs_recursion(graph=graph, cur_node=1, visited=visited)
# print(f"visited : {visited}")


print(f"visited : {dfs_stack(graph=graph, start_node=1)}")

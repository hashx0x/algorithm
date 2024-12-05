def dfs(graph, v, visited):
    visited[v] = True
    print( v, end= ' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] *9

dfs(graph,1,visited)

#*
# visited[1] = True
# 1
# graph[1] = [2,3,8]
# i = 2,3,8 => 2부터 시작
# if not visited[2]
#  => dfs(graph,2,visited)
# visited[2] = True [False, True, True, False, ...]
# print(2)
# for i in graph[2] = [1,7]
# i = 1,7   1부터시작
# if not visited[1](True이므로 if절 안탐)
# if not visited[7](False이므로 if절 탐)
# dfs()
# 
#
# *#
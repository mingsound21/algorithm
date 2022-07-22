import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]

for i in range(int(input())):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS ver
visited_bfs = [False for _ in range(n+1)]
def bfs(graph, start, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True
    
    while(queue):
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited_bfs[i]:
                visited_bfs[i] = True
                queue.append(i)
                
bfs(graph, 1, visited_bfs)
print(visited_bfs.count(True)-1) # print(sum(visited_bfs)-1)

# DFS ver
visited_dfs = [False for _ in range(n+1)]
def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

dfs(graph, 1, visited_dfs)
print(sum(visited_dfs)-1)


# 단순히 정점 방문이 중요 -> DFS, BFS 상관 없음
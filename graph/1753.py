import sys
input = sys.stdin.readline
from collections import deque

INF = sys.maxsize

V, E = map(int, input().split())
s = int(input())

weight = [[INF for j in range(V+1)] for i in range(V+1)]
graph = [[] for i in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    weight[u][v] = w
    graph[u].append(v)

visited = [0 for i in range(V+1)]

def bfs(s):
    queue = deque(graph[s])
    
    visited[s] = True
    
    while queue:
        v = queue.popleft()
        print(queue)
        
        for i in graph[v]:
            if not visited[i]:
                if weight[s][i] > weight[s][v] + weight[v][i]:
                    weight[s][i] = weight[s][v] + weight[v][i]
                queue.append(i)
                visited[i] = True    
            

bfs(s)
for i in range(1, V+1):
    if s == i:
        print(0)
    elif weight[s][i] == 9223372036854775807:
        print('INF')
    else:
        print(weight[s][i])
# 방향 그래프

# 메모리초과 나옴
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs():
    queue = deque([])
    visited = [0] * (n+1)
    visited[1] = 1

    # 친구들 queue에 담기
    for v in graph[1]:
        queue.append(v)
        visited[v] = 1
    cnt = len(queue)    
    
    while queue:
        v = queue.popleft()
        
        for u in graph[v]:
            if not visited[u]:
                visited[u] = 1
                cnt += 1
    
    return cnt

print(bfs())

                
            
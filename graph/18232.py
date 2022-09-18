import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
s, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dx = [-1, 1]
def bfs():
    queue = deque([])
    
    for i in range(2):
        nx = s + dx[i]
            
        if 0 < nx <= n:
            visited[nx] = 1
            queue.append((nx, 1))
            
    for v in graph[s]:
        queue.append((v, 1))
        visited[v] = 1
    
    while queue:
        x, cnt = queue.popleft()
        if x == e:
            return cnt
        
        for i in range(2):
            nx = x + dx[i]
            
            if 0 < nx <= n and not visited[nx]:
                visited[nx] = 1
                queue.append((nx, cnt+1))
        
        for v in graph[x]:
            nx = v
            if not visited[nx]:
                visited[nx] = 1
                queue.append((nx, cnt+1))
print(bfs())


# 1부터 N까지 하나의 텔레포트 정거장, 텔레포트 통하여 다른 텔레포트 정거장으로 이동 가능
# 이동 방법 : x-1, x+1, x와 연결된 텔레포트 정거장 -> 각 이동시간 1초
# 점 S에서, E까지 가는 최소시간
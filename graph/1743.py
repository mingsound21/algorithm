import sys
input = sys.stdin.readline
from collections import deque

n, m, k = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(m)] for _ in range(n)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return cnt

_max = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            _max = max(_max, bfs(i, j))
    
print(_max)

# 가장 큰 음식물의 크기 출력
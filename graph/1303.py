import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, team):
    queue = deque([(x, y)])
    visited[x][y] = 1
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        cnt += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == team:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                
    return cnt**2

visited = [[0]*m for _ in range(n)]
a = 0
b = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if graph[i][j] == 'W':
                a += bfs(i, j, 'W')
            else:
                b += bfs(i, j, 'B')

print(a, b)

# 아군 병사(W)의 위력의 합과 적국 병사(B)의 위력의 합을 출력
# n명이 뭉쳐있을때(상하좌우로 붙어있으면) n^2의 위력을 낼 수 있음
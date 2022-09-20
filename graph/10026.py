import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, color):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] in color:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                

GB = 0 # 적록 색약
NGB = 0 # 적록 색약 X

visited = [[0]* n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            if graph[i][j] in ['G', 'R']:
                bfs(i, j, ['G', 'R'])
            else:
                bfs(i, j, ['B'])
            GB += 1
            
visited = [[0]* n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, [graph[i][j]])
            NGB += 1

print(NGB, GB)
            

# R, G, B 중 하나가 색칠 되어있음
# 상하좌우로 인접한 경우 같은 구역
# 적록 색약인 사람은 R == G로 판단
# 적록 색약인 사람이 봤을때와 아닌 사람이 봤을 때의 구역의 수를 출력
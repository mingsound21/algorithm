import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

start = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            start.append((i, j))
            
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]            

visited = [[0] * m for _ in range(n)]
def bfs():
    queue = deque(start)
    for x, y in start:
        visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if graph[x][y] >= 3:
            return visited[x][y] - 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    return -1

    
answer = bfs()
if answer == -1:
    print('NIE')
else:
    print('TAK')
    print(answer)

# 빈 복도 0, 장애물 1, 딱다구리 2, 청국장 3, 스시 4, 맥앤치즈 5
# 1시간 마다 상하좌우 1만 지나갈 수 없음.

# 음식 먹었다면 TAK과 현위치에서 가장 빨리 도착할 수 있는 음식까지 최단 거리 출력
# 음식 못먹었다면 NIE
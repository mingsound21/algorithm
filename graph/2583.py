import sys
input = sys.stdin.readline
from collections import deque

m, n, k = map(int, input().split())
graph = [[0 for j in range(n)] for i in range(m)]
for i  in range(k):
    ay, ax, by, bx = map(int, input().split())
    for a in range(m-bx, m-ax):
        for b in range(ay, by):
            graph[a][b] = 1
        
    
def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    area_size = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= m or ny < 0 or ny >= n :
                continue
            
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                area_size += 1
                
    return area_size

area_size = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            area_size.append(bfs(i, j))

print(len(area_size))
for v in sorted(area_size):
    print(v, end = " ")
    
# bfs
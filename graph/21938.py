import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
t = int(input())

graph = [[] for _ in range(n)]
for i in range(n):
    avg = 0
    for j in range(m*3):
        avg += data[i][j]
        
        if j % 3 == 2:
            avg = avg // 3
            if avg >= t :
                graph[i].append(255)
            else:
                graph[i].append(0)
            avg = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 255:
                queue.append((nx,ny))
                visited[nx][ny] = 1
                

visited = [[0]*m for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 255 and not visited[i][j]:
            bfs(i, j)
            answer += 1
            
print(answer)

# r, g, b 3개의 평균 >= t이면 255
# 그런뒤에 물체(연결요소) 개수 출력
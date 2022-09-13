import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if data[i][j] == 2: # 목표점 위치 얻기
            x = i
            y = j
            

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(m)] for _ in range(n)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0 
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # nx, ny가 범위안에 있고, 아직 방문하지 않았으며, 갈 수 있는 위치라면
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and data[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                

bfs(x, y)
for i in range(n):
    for j in range(m):
        # 갈 수 있는 곳이지만, 도달하지 못하는 경우 -1
        if data[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
    print(*visited[i])
    


# 2 : 목표점, 1 : 갈 수 있는 땅, 0 : 갈 수 없는 땅
# 도달할 수 없는 위치는 -1
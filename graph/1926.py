import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    space = 0
    
    while queue:
        x, y = queue.popleft()
        space += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))

    return space

_max = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            _max = max(_max, bfs(i, j))
            cnt += 1
            

print(cnt)
print(_max)
        

# 그림의 개수와 가장 넓은 그림의 넓이를 출력
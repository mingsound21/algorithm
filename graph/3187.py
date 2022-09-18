import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0 for _ in range(c)] for _ in range(r)]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    sheep = 0
    wolf = 0
    
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 'v':
            wolf += 1
        elif graph[x][y] == 'k':
            sheep += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and graph[nx][ny] != '#':
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf
    
total_sheep = 0
total_wolf = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != '#':
            sheep, wolf = bfs(i, j)
            total_sheep += sheep
            total_wolf += wolf

print(total_sheep, total_wolf)

# 같은 울타리 영역안에서 양 수 > 늑대 수 이면 늑대 전부 잡아먹힘 (반대는 반대)
# 울타리 #, 늑대 v, 양 k
# 몇마리 양 늑대 살아남을지
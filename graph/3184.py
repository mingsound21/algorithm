from collections import deque
import sys
input = sys.stdin.readline

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
        elif graph[x][y] == 'o':
            sheep += 1
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    if sheep > wolf :
        wolf = 0
    else:
        sheep = 0
    return sheep, wolf

res_sheep = 0
res_wolf = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and graph[i][j] != '#':
            sheep, wolf = bfs(i, j)
            res_sheep += sheep
            res_wolf += wolf

print(res_sheep, res_wolf)

        
# . 빈 필드, # 울타리, o 양, v 늑대
# 우리 안에 들어있는 양은 싸움을 걸 수 있고, 
# 영역 안에 양의 수 > 늑대수 이면 이기고, 늑대를 우리에서 쫓아냄, 아니라면 지역안의 모든 양을 먹음

# 아침이 되었을때 살아남은 양과 늑대 수 출력

# 쫓아낸다 = 아예 늑대 없앰
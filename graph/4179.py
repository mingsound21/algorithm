import sys
input = sys.stdin.readline
from collections import deque


r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, fire):
    queue = deque([(x, y)])
    fire_queue = fire
    visited = [[0 for _ in range(c)] for _ in range(r)]
    fire_visit = [[0 for _ in range(c)] for _ in range(r)]
    visited[x][y] = 1
    
    while queue:
        # 불먼저
        temp_fire = []
        for fire in fire_queue:
            x, y = fire
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and fire_visit[nx][ny] == 0 and graph[nx][ny] != '#':
                    fire_visit[nx][ny] = 1
                    temp_fire.append((nx,ny))
                    graph[nx][ny] = 'F'
                    
        fire_queue = temp_fire
        
        
        for _ in range(len(queue)): # for문 꼭 돌려줘야함 - 그래야 한번 사람 이동, 한번 불 이동이 가능
            x, y = queue.popleft()
            if x == 0 or x == r-1 or y == 0 or y == c-1:
                
                return visited[x][y]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0 and graph[nx][ny] != 'F' and graph[nx][ny] != '#':
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
        
    return 0

fire = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'F':
            fire.append((i, j))
        if graph[i][j] == 'J':
            x = i
            y = j
day = bfs(x, y, fire)



if day == 0:
    print("IMPOSSIBLE")
else:
    print(day)
            
# 불과 지훈이는 매분 마다 상하좌우로 이동
# 미로의 가장자리로 탈출 가능
# 지훈, 불은 벽이 있는 공간은 통과 못함
# 가장 빠른 탈출 시간
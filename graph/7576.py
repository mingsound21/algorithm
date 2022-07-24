import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = []
tomato = []
empty = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i, j))
        if graph[i][j] == 0:
            empty += 1

def bfs(graph, initialList):
    queue = deque(initialList)
    day = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                if day < graph[nx][ny]:
                    day = graph[nx][ny]
    return day -1

if empty == 0:
    print(0)
else:
    day = bfs(graph, tomato) 

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                day = -1
                break

    print(day)
    

# 저장될 때 부터 모든 토마토가 익어있는 상태이면 0 출력

# 입력 받으면서 1위치를 담은뒤
# bfs 1회 실행 후
# 2중 loop 돌아서 0이 하나라도 있으면 -1

# 해설 +
# 문제에서 "최소일수", "주변의 토마토 익힘" => bfs
# >> 깊이 들어갈 일이 없어서

# exit(0)하면 거기서 코드 종료
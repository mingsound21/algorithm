import sys
input = sys.stdin.readline
from collections import deque
import copy
INF = sys.maxsize

graph = []
n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

wall = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            wall.append((i, j))


def bfs(a, b, tmp_graph):
    queue = deque([(0, 0)])
    tmp_graph[0][0] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = tmp_graph[x][y] + 1
                queue.append((nx, ny))
            
                if nx == a and ny == b:
                    return tmp_graph[nx][ny]
    return INF # n, m위치에 도달 못하는 경우

day = []
tmp_graph = copy.deepcopy(graph)
day.append(bfs(n-1, m-1, tmp_graph)) # 벽하나도 안지웠을 때

for i, j in wall:
    tmp_graph = copy.deepcopy(graph)
    tmp_graph[i][j] = 0
    day.append(bfs(n-1, m-1, tmp_graph))

day = min(day)
if day == INF:
    print(-1)
else:
    print(day)
    
# 1 있는 곳 모두 한번씩 지워가면서 bfs 돌리기
# 시간 초과
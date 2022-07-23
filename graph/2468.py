import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph, x, y, h, visited):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n :
                if visited[nx][ny] == 0 and graph[nx][ny] >= h:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
            

max_h = max(map(max, graph)) # 최고 높이
hArr = []

for h in range(1, max_h+1):
    cnt = 0
    visited = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if graph[i][j] >= h and visited[i][j] == 0:
                bfs(graph, i, j, h, visited)
                cnt += 1
    hArr.append(cnt)

print(max(hArr))

# 이전 내 풀이에서 보완한 것 >> 근데 시간은 늘어났다고 나옴...
# 최고 높이까지 비가 오면 모두 잠기니까 최고 높이 -1 까지만 계산
# graph_copy 대신 0으로 채워진 visited를 넘겨서 visit하면 1로 이동 경로 체크

# 38번째 줄에서 graph[i][j] > h로 작성할 경우 h 범위가 range(max_h)
# >> range에서 0이 포함되어야하는 이유 : 비가 전혀 오지 않는 경우도 고려
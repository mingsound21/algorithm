import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

def bfs(graph, x, y, h):
    
    queue = deque([(x, y)])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        # print(queue)
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if graph[nx][ny] >= h:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                
max_h = max(map(max, graph))
hArr = []
for h in range(1, max_h+1):
    # print(h)
    cnt = 0
    graph_copy = [item[:] for item in graph]
    for i in range(n):
        for j in range(n):
            if graph_copy[i][j] >= h :
                bfs(graph_copy, i, j, h)
                cnt += 1
    hArr.append(cnt)
    
print(max(hArr))
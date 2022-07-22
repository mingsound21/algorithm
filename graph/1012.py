import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10 ** 7)

def bfs(graph, x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while(queue):
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if graph[nx][ny]:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    
def dfs(graph, x, y):
    
    graph[x][y] = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
    
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        if graph[nx][ny]:
            dfs(graph, nx, ny)

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0 for b in range(m)] for a in range(n)]
    for i in range(k):
        y, x  = map(int, input().split())
        graph[x][y] = 1
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j) # 여기만 dfs, bfs 변경하면 됨
                cnt += 1
            
    print(cnt)
    
# 상하좌우 - 인접
# 배추들이 모여있는 덩어리 개수 = 필요한 지렁이 수

# 정점 방문이 중요한 문제 - DFS, BFS 모두 가능
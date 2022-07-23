import sys
input = sys.stdin.readline
from collections import deque


    
def bfs(x, y, visited):
    queue = deque([(x, y)])
    
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    while queue:
        x, y  = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if(nx < 0 or nx >= n or ny < 0 or ny >= n):
                continue
            
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                
                if bx == nx and by == ny:
                    return visited[nx][ny]
                
                
for _ in range(int(input())):
    n = int(input())
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    
    if ax == bx and ay == by:
        print(0)
        continue
    
    visited = [[0 for j in range(n)] for i in range(n)]
    print(bfs(ax, ay, visited))
    
# BFS
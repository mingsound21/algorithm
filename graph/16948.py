import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
visited = [[0]*n for _ in range(n)]
r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

def bfs():
    q = deque([(r1, c1)])
    visited[r1][c1] = 1 # 0으로 시작하면 (r1, c1) 방문 안했다고 판단하기때문에, 시작을 횟수 1로 하고 return 할때 횟수 - 1을 해줌
    
    while q:
        x, y = q.popleft()
        if x == r2 and y == c2:
            return visited[x][y] - 1
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
    return -1

print(bfs())

# (r1, c1)에서 (r2, c2)로 이동하는 최소 이동 횟수
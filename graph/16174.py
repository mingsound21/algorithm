import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

visited = [[0]* n for _ in range(n)]
def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x== n-1 and y==n-1:
            return True
        
        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return False

answer = bfs()
if answer:
    print("HaruHaru")
else:
    print("Hing")
# 정사각형 구역안에서만 움직일 수 있음
# 맨 왼쪽 위에서 출발
# 오른쪽과 아래로만 이동 가능
# 가장 오른쪽 아래 칸에 도달하면 쩰리 승
# 한번에 이동할 수 있는 칸의 수는 현재 밟고 있는 칸에 쓰인 수

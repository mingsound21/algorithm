import sys
input = sys.stdin.readline
from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

n, m = map(int, input().split())
x, y = map(int, input().split())
graph = [[0] * n for _ in range(n)] # 1 : 상대말
other = []

for i in range(m):
    a, b = map(int, input().split())
    other.append((a, b))
    graph[a-1][b-1] = 1

total_cnt = len(other)
visited = [[-1] * n for _ in range(n)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        if graph[x][y] == 1:
            cnt += 1
            
        if cnt == total_cnt:
            break
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

bfs(x-1, y-1)
    
for a, b in other:
    print(visited[a-1][b-1], end = ' ')

# 상대편 말을 잡기 위한 나이트의 최소 이동수 출력

# 문제마다 좌표가 0부터 시작인지 1부터 시작인지 잘 확인!
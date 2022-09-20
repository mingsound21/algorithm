import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

visited = [[0] * m for _ in range(n)]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                

answer = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == 1:
            bfs(i, j)
            answer += 1
            
print(answer)

# 현수막에 글자가 몇개인지 출력
# 글자인 부분 1, 아닌 부분 0
# 상하좌우 + "대각선"으로 1이 연결되어있을때 1개의 글자
# >> 1 연결 요소 개수 출력

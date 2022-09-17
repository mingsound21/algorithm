import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(initial):
    answer = 'NO'
    queue = deque(initial)
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in queue:
        visited[x][y] = 1
        
    while queue:
        x, y = queue.popleft()
        if x == n-1:
            answer = 'YES'
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return answer

initial = []
for i in range(m):
    if graph[0][i] == 0:
        initial.append((0, i))

print(bfs(initial))


# 검은색(1) - 전류 차단, 흰색(0) - 전류 통함
# 가장 위쪽에 전류를 흘렸을때 가장 아래쪽까지 전류가 전달되는지
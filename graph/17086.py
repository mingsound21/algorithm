import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(shark):
    queue = deque(shark)
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


shark = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            shark.append((i, j))
            visited[i][j] = 0
            
bfs(shark)

answer = 0
for v in visited:
    answer = max(answer, max(v))

print(answer)

# 안전거리 : 그 칸과 가장 가까운 아기 상어와의 거리
# 두 칸의 거리 : 그 사이 빈 칸 개수
# 이동 : 대각선 포람 인접 8방향
# 안전거리의 최댓값 출력

# 문제를 제대로 읽자,,,
# "각 칸에서" 가장 가까운 상어와의 거리 중 최댓값을 출력하는 문제
# >> "상어와 상어 사이 거리" 중에서 최댓값을 출력하는 문제로 착각,,,

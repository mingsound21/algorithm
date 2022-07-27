import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = []

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] # n x m x 2
visited = [0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))
    
    while queue:
        a, b, c = queue.popleft()
        # 최종 장소에 도달하면 이동 횟수 반환
        if a == n-1 and b == m-1:
            return visited[a][b][c]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽파괴 기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx, ny, 1))
                
            # 다음 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 경우
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx, ny, c))
    return -1

print(bfs(0, 0, 0))

# 벽 부순 여부를 3차원 행렬로 나타내기
# visited[x][y][0] : 안부순 경로
# visited[x][y][1] : 부순 경로

# 어렵다,, 풀이 이해도 어려워,,
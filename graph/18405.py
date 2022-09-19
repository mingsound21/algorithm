import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
s, a, b = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(initial):
    q = deque(initial)
    
    while q:
        x, y = q.popleft()
        
        if visited[x][y] == s: # s초뒤 방문을 이미 했다면, 이제 시간 끝
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                graph[nx][ny] = graph[x][y]
                q.append((nx, ny))
    
    return graph[a-1][b-1]
    
    

initial = []
visited = [[-1] * n for _ in range(n)] # -1이면 방문 안했음. 방문했을 경우에는 몇초뒤에 방문한 것인지 표현
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            visited[i][j] = 0 # 시작은 0초
            initial.append((i, j)) # x, y, 바이러스 종류

initial.sort(key = lambda x : graph[x[0]][x[1]]) # 바이러스 종류 오름차순으로 정렬
print(bfs(initial))

# 바이러스 종류 : 1 - k 
# 매 초마다 낮은 종류 바이러스부터 먼저 증식
# 이미 바이러스 있는 칸에는 바이러스 덮어쓰기 X
# s초 뒤에 (x, y)에 존재하는 바이러스의 종류를 출력, 없다면 0 출력

# 처음에 바이러스 담긴 좌표를 바이러스 종류를 기준으로 오름차순 정렬한뒤, 그 배열을 가지고 bfs를 적용하면,
# 바이러스 종류가 낮은 것이 우선적으로 처리됨
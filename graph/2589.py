import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 'L' and not visited:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                queue.append((nx, ny))
    return cnt -1 

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
        

# 육지 L, 바다 W
# 상하좌우 이웃한 육지로만 이동 가능, 한칸 이동시 한시간 걸림
# 보물은 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있음
# 보물이 묻혀있는 두 곳 간의 최단거리로 이동하는 시간 구하기
# 육지 연결 요소중에서 가장 최단거리 이동시간이 먼 2곳의 위치를 구하기

# 어려운데...?
# 일단 다른 문제들과 다르게 시작점이 너무 무작위....

# 방법 1)
# 일단 아무 한 곳 x에서 부터 각 위치의 최단 거리를 구함. 근데 상하좌우 arr에 따로 (x, y, 최단거리) 를 저장
# 상하좌우에서 각각 최단 거리 max를 뽑아내고, 뽑힌 4개 중에서 max 2개를 뽑기. 뽑힌 2개의 max를 더한뒤 + 1하면 답
# 연결요소가 여러개 일 수 있으니까, 연결요소마다 max비교
#>> 틀림... 안됨.. 복잡함...

# 다른 사람 정답 풀이
# >> 생각보다 간단했음
# 그냥 모든 L인곳에서 bfs돌려서 가장 긴 최단거리를 구해서 비교
# 가로, 세로 길이가 길지 않아서(50) 250 * 250 = 62500이라서 가능한듯!
from copy import deepcopy
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

n, m = map(int, input().split()) # n <= 50, m <= 10
graph = [list(map(int, input().split())) for _ in range(n)]

# 바이러스 놓을 칸 찾기
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(virus):
    queue = deque(virus)
    for x, y in virus:
        visited[x][y] = 1
        copy_graph[x][y] = 3
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and copy_graph[nx][ny] in [0, 2]: # 주의! in[0, 2]
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
def findMaxTime():
    # 최소 시간 찾기
    _max = 0
    check_all = 0
    for i in range(n):
        for j in range(n):
            _max = max(_max, visited[i][j])
            if copy_graph[i][j] in [0, 2] and not visited[i][j]: # 주의! in[0, 2]
                check_all = 1

    if check_all: # 모든 빈칸에 바이러스 퍼뜨릴수 없는 경우
        return -1
    
    return _max

answer = 10**5
for v in list(combinations(virus, m)):
    copy_graph = deepcopy(graph)
    visited = [[0]* n for _ in range(n)]
        
    bfs(v) # 바이러스 퍼뜨리고
    
    # print('-'*12)
    # for g in copy_graph:
    #     print(*g)
    
    result = findMaxTime()
    if result != -1:
        answer = min(answer, result)

if answer == 10**5:
    print(-1)
else:
    print(answer-1)


# 특정위치에 바이러스 M개 놓음
# 빈칸, 벽으로 이루어져있음
# 바이러스 : 상하좌우로 인접한 모든 빈칸으로 동시에 복제되며, 1초걸림
# 빈칸 0, 벽 1, 바이러스 2
# 모든 빈칸에 바이러스를 퍼뜨리는 최소시간 구하기
#>> combination
# 모든 빈칸에 바이러스 퍼뜨릴수 없는 경우 -1 출력
# >> 바이러스를 놓을 수 있는 칸이 10개 이하로 정해져있구나

# 다른 연구소 문제랑 조금 달랐던 게 아마... 2로 표시된 칸들 중에서 m개의 칸에만 바이러스를 놓고 다른 2로 표시된 칸들은 0과 같이 생각해야한다는 점
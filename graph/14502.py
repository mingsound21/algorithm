import sys
input = sys.stdin.readline
from collections import deque
import copy

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    
    # 감염
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            if tmp_graph[nx][ny] == 0:
                tmp_graph[nx][ny] = 2
                queue.append((nx, ny))

    # 안전 지역 개수 구하기           
    global answer
    cnt = 0
    
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    
    answer = max(answer, cnt)

# 오 이렇게 재귀를 사용해서 모든 경우의 수를 만들 수 있구나,,
def makeWall(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt + 1)
                graph[i][j] = 0
                
n, m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))
    
answer = 0
makeWall(0)
print(answer)

# 문제
# > 바이러스 상하좌우 인접한 빈칸으로 퍼짐
# > 새로 세울 수 있는 벽 개수 : 3

# >> 안전 영역 크기의 최댓값

# 상하좌우 퍼짐 -> bfs

# 풀이
# 2인 칸을 모두 큐에 넣고
# bfs에서 하나씩 꺼내 확장

# 벽을 어디에 세워야 최댓값이 나올지 알 수 없어서 벽을 세울 수 있는 모든 경우의 수에 대해 수행
# 벽 세우고, bfs 수행, 벽 다시 지우기
# 백 트래킹 방식을 사용해 3개의 벽을 모든 칸에 세워본다.


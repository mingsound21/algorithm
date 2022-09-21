import sys
input = sys.stdin.readline
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [-1] * (F+1) # -1 : 아직 방문 안함. 그외 숫자는 방문한 시각
dx = [U, -D]
def bfs():
    queue = deque([S])
    visited[S] = 0
    
    while queue:
        x = queue.popleft()
        
        if x == G:
            return visited[x]
        
        for i in range(2):
            nx = x + dx[i]
            
            if nx < 1 or nx > F or visited[nx] != -1:
                continue
            
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
    return "use the stairs"

print(bfs())


# 총 F층, S층에서 G층으로 가려함
# 엘베 버튼은 [+U, -D] 버튼 뿌
# 범위를 벗어난 곳에 도착하게되는 경우에는 >> use the stairs 출력
# S층에서 G층으로 가기 위해서 눌러야하는 버튼 수의 최솟값 출력
# >> 일종의 최단 경로 >> bfs사용 (최단경로는 dfs를 사용하면 맨 먼저 도착해도 그 값이 최단 경로임을 보장하지 못함)
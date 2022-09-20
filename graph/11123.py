import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] == '#':
                queue.append((nx, ny))
                visited[nx][ny] = 1
                
    

for _ in range(int(input())):
    h, w = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    
    answer = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == '#':
                bfs(i, j)
                answer += 1
    
    print(answer)


# 양 #, 풀 .

# 몇 개의 양 무리가 있는지 출력
# >> 연결 요소 개수 출력
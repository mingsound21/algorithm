import sys
input = sys.stdin.readline
from collections import deque

n, m, t = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 1
    get_gram = 100000
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y] + 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif data[nx][ny] == 2:
                    data[nx][ny] = data[x][y] + 1
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    get_gram = data[nx][ny] + (n-1-nx) + (m-1-ny)
    
    if data[n-1][m-1] == 0: # 이 경우를 생각해주지 못함
        return get_gram
    return min(get_gram, data[n-1][m-1])

answer = bfs(0, 0)

if answer == 0 or answer > t:
    print('Fail')
else:
    print(answer)
    
# 그람 - 여러개의 벽 부수기 가능
# 딱 t시간에 도착해도 구출 가능
# 0 : 빈공간, 1 : 벽, 2 : 그람(좋은 칼)

# 그람 도착시에는 최단거리는 이미 정해져 있지 않나?
# >> 그람을 얻어서 벽을 깨부수고 가는 길보다 그냥 그람 안얻고 가는 길이 빠를 수도 있을듯
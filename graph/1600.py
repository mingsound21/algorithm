import sys
input = sys.stdin.readline
from collections import deque

k = int(input())
w, h = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(h)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
d1 = [-2, -1, 1, 2, -2, -1, 1, 2]
d2 = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs():
    q = deque()
    q.append((0, 0, k))
    visited = [[[0 for _ in range(31)] for i in range(w)] for i in range(h)]
    
    while q:
        x, y, z = q.popleft()
        
        if x == h-1 and y == w-1: # 도착지점에 도착했다면
            return visited[x][y][z]
        
        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]
            # nx, ny가 범위안에 있고, 가려는곳이 장애물이 있지 않고, 아직 방문을 하지 않았다면
            if 0 <= nx < h and 0 <= ny < w and data[nx][ny] != 1 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append((nx, ny, z))
            
        if z > 0: # 아직 대각선으로 이동할 수 있는 기회가 남아있다면
            for i in range(8):
                nx = x + d1[i]
                ny = y + d2[i]
                if 0 <= nx < h and 0 <= ny < w and data[nx][ny] != 1 and visited[nx][ny][z-1] == 0:
                    visited[nx][ny][z-1] = visited[x][y][z] + 1
                    q.append((nx, ny, z-1))
    return -1

print(bfs())

# 0 평지, 1 장애물

# 원숭이는 K 번만 나이트처럼 이동 가능, 그외에는 인접한 칸으로만 움직일 수 있음
# 원숭이가 왼쪽 위에서 오른쪽 아래로 이동할 수 있는 최소한의 동작 수 (불가능한 경우 -1 출력)


# 벽 부수기 문제와 유사
# >> 전체 맵으로 보면 같은 위치지만, 상태변화에 따라 해당 정점이 다른 의미를 지니기에 상태의 정보를 담을 공간을 추가적으로 만들어줘야함

# point visited를 3차원으로 z는 대각선이동할 수 있는 남은 기회 수
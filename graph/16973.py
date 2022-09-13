from collections import deque
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
h, w, x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; x2 -=1 ; y1 -=1 ; y2 -= 1
visited = [[0 for _ in range(m)] for i in range(n)]

def bfs():
    queue = deque([(x1, y1)])
    
    visited[x1][y1] = 1
    
    while queue:
        # print(queue)
        x, y = queue.popleft()
        
        #좌
        check = 0
        ny = y - 1
        if 0 <= ny < m and visited[x][y-1] == 0:
            for i in range(h):
                nx = x + i
                if data[nx][ny] == 0:
                    continue
                check += 1
            if check == 0:
                queue.append((x, y-1))
                visited[x][y-1] = visited[x][y] + 1
            
        #우
        check = 0
        ny = y + w
        if 0 <= ny < m and visited[x][y+1] == 0:
            for i in range(h):
                nx = x + i
                if data[nx][ny] == 0:
                    continue
                check += 1
            if check == 0:
                queue.append((x, y+1))
                visited[x][y+1] = visited[x][y] + 1
            
        #위
        check = 0
        nx = x - 1
        if 0 <= nx < n and visited[x-1][y] == 0:
            for i in range(w):
                ny = y + i
                if data[nx][ny] == 0:
                    continue
                check += 1
            if check == 0:
                queue.append((x-1, y))
                visited[x-1][y] = visited[x][y] + 1
            
        #아래
        check = 0
        nx = x + h
        if 0 <= nx < n and visited[x+1][y] == 0:
            for i in range(w):
                ny = y + i
                if data[nx][ny] == 0:
                    continue
                check += 1
            if check == 0:
                queue.append((x+1, y))
                visited[x+1][y] = visited[x][y] + 1
        
        # for v in visited:
        #     print(*v)
        # print('-' * 15)

if x1 == x2 and y1 == y2:
    print(0)
    exit(0)

bfs()

    
if visited[x2][y2] == 0:
    print(-1)
else:
    print(visited[x2][y2]-1)
    
# 격자판의 각 칸에는 빈칸(0) or 벽(1)
# 최소 이동 횟수, 이동불가인경우 -1 출력


# 다른 사람 풀이

def move(x, y):
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = True
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == Fr-1 and y == Fc-1: # 원하는 위치에 도착했다면 cnt return
            return cnt 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 사각형의 처음과 끝의 위치가 범위안에 있고
            # 방문을 하지 않았고
            # 벽에 부딪치지 않으면 if 문 실행
            if 0 <= nx and nx + h - 1 < n and 0 <= ny and ny + w - 1 < m and not visited[nx][ny] and check(nx, ny):
                q.append([nx, ny, cnt+1])
    return -1


# 벽에 부딪치는지 체크하는 함수
def check(x, y):
    visited[x][y] = True
    for i, j in walls:
        if x <= i < x + h and y <= j < y + w:
            return False
    return True

n, m = map(int, input().split())
data = []
walls = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            walls.append((i, j))
    data.append(row)
h, w, Sr, Sc, Fr, Fc = map(int, input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(move(Sr-1, Sc-1))
import sys
input = sys.stdin.readline
from collections import deque

# 틀린 내 풀이 - 메모리 초과

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
sr, sc, sdir = map(int, input().split())
fr, fc, fdir = map(int, input().split())

# 동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
dir_2 = set([(0, 1), (1, 0), (2, 3), (3, 2)])

def bfs():
    visited = [[-1] * m for _ in range(n)] # -1은 방문하지 않았음, 0이상의 수는 최소의 명령으로 올 수 있었는지 나타냄
    queue = deque([(sr-1, sc-1, sdir-1)]) # 나는 동서남북 0123으로 설정
    visited[sr-1][sc-1] = 0
    arr = []
    
    while queue:
        x, y, dir = queue.popleft()
        
        if x == fr-1 and y == fc-1:
            if (dir, fdir-1) in dir_2:
                diff = 2
            elif dir == fdir-1:
                diff = 0
            else:
                diff = 1
            arr.append(visited[x][y] + diff)
        
        for i in range(4):
            ndir = (4 + dir - i) % 4
            # diff = abs(ndir - dir) # 이런식으로 계산하면 안됨
            if (dir, ndir) in dir_2:
                diff = 2
            elif dir == ndir:
                diff = 0
            else:
                diff = 1
                
            # print(dir, ndir, diff)
            
            for j in range(1, 4):
                nx = x + j * dx[ndir]
                ny = y + j * dy[ndir]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 안이 아니면 continue
                    continue
                
                if graph[nx][ny] == 1: # 1칸 이동했는데 갈 수 없는 곳이면 2칸, 3칸이동은 아예 불가능
                    break
                
                
                # 항상 먼저 도착했다고 해서 가장 적은 수의 명령으로 도착했다는 보장이 없는 것 같아서
                # 명령수가 같은데 같은 장소에 도착했다면 queue에 추가 >> 마지막에 turn수에 따라서 최소 명령 횟수가 될 가능성이 있어서 
                if visited[nx][ny] == visited[x][y] + diff + 1 or visited[nx][ny] == -1: 
                    visited[nx][ny] = visited[x][y] + diff + 1
                    queue.append((nx, ny, ndir))
    
    # for v in visited:
    #     print(*v)
        
    print(min(arr))
    return

bfs()

# 0은 로봇이 갈 수 있고, 1은 로봇이 갈 수 없음
# 로봇의 현재 위치와 바라보는 방향이 주어졌을때 로봇을 원하는 위치로 이동, 원하는 방향을 바라보도록하는데 필요한 최소 명령 수
# 명령 1 . Go k (1<= k <=3) 현재 바라보고 있는 방향으로 k만큼
# 명령 2 . Turn left(or right) : 왼, 오로 90도 turn

# 방향은 동 1, 서 2, 남 3, 북 4


# 다른 사람 풀이 - https://pacific-ocean.tistory.com/399
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(n)]
startX, startY, startD = map(int, input().split())
endX, endY, endD = map(int, input().split())

def bfs():
    q = deque()
    q.append([startX-1, startY-1, startD, 0])
    visit = [[[0 for _ in range(5)]for _ in range(m)] for _ in range(n)]
    visit[startX-1][startY-1][startD] = 1
    
    while q:
        x, y, d, cnt = q.popleft()
        if x == endX-1 and y == endY-1 and d == endD : return cnt
        
        nx, ny = x, y 
        for i in range(3):
            nx += dx[d]
            ny += dy[d]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny][d] == 1: continue
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
                visit[nx][ny][d] = 1
                q.append((nx, ny, d, cnt + 1))
            else: break
        
        for i in range(1, 5):
            if d != i and visit[x][y][i] == 0:
                visit[x][y][i] = 1
                if (d == 1 and i == 2) or (d == 2 and i == 1) or (d == 3 and i == 4) or (d == 4 and i == 3):
                    q.appen((x, y, i, cnt + 2))
                else:
                    q.append((x, y, i, cnt + 1))

print(bfs())

# visit 배열을 3차원으로 설정 >> x, y, direction
# https://www.acmicpc.net/board/view/53257  >> visit 배열을 그렇게 설정하는 이유
# visit 배열을 좌표의 개념을 넘어 특정 "상태"를 저장한다고 생각


# 어렵다...!
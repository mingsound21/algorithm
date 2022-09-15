import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
ice = []
for i in range(n):
    for j in range(m):
        if data[i][j] != 0:
            ice.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def check_split(x, y):
    q = deque([(x, y)])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and data[nx][ny] > 0:
                q.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    
    return cnt
        

def bfs():
    q = deque(ice)
    year = 0
    while q:
        arr = []
        for _ in range(len(q)):
            
            x, y = q.popleft()
            
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
                    cnt += 1
                
            arr.append((x, y, cnt))

        # 녹이기
        for x, y, cnt in arr:
            data[x][y] -= cnt
            if data[x][y] < 0:
                data[x][y] = 0
            if data[x][y] > 0:
                q.append((x, y))
        
        if len(q) == 0: # 인덱스 에러 수정 코드
            return 0
                
        # 2개 이상으로 분리되었는지 확인
        if check_split(q[0][0], q[0][1]) != len(q):
            return year + 1
        
        year += 1
    return 0
print(bfs())

# 빙산의 각 칸은 동서남북에 있는 0의 개수만큼 줄어든다.
# 빙산이 두덩어리 이상으로 분리되는 시간을 구하시오
# 전부 녹을 때 까지 두덩어리로 쪼개지지 않으면 0을 출력


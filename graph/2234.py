import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result1, result2, result3 = 0, 0, 0 # 방의 개수, 최대 방 넓이, 하나의 벽 제거 후 얻을 수 있는 최대 방 넓이

# 서 북 동 남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1
    cnt = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 이 부분이 핵심!!!
            # 2진수 연산 >> & | ~ ^
            # 1, 2, 4, 8이 2진수로 변환했을때 각자리 빼고는 모두 0
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: # 범위 안에 있고, 방문하지 않았고
                if i == 0: # 서 
                    if 1 & graph[x][y]: continue # & 결과 1이 나온다면 서쪽에 벽 있음
                elif i == 1: # 북 
                    if 2 & graph[x][y] : continue # & 결과 2가 나온다면 북쪽에 벽 있음
                elif i == 2: # 동
                    if 4 & graph[x][y] : continue
                else: # 남
                    if 8 & graph[x][y] : continue
                
                # 가려는 곳에 벽이 세워져있지않다면 
                # 방문처리 & 큐에 삽입
                visited[nx][ny] = 1
                q.append((nx, ny))
                cnt += 1 # 방 넓이 1 추가
    return cnt # 방 넓이
                
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0: # 아직 방문하지 않았다면
            result1 += 1 # 방 개수 하나 추가 >> bfs하면 같은 방 공간들은 모두 visited = 1처리됨
            result2 = max(result2, bfs(i, j)) # bfs의 return값 = 방 넓이, 최대 방 넓이 구하기


# 벽 하나 제거시 최대 방 넓이
for i in range(n):
    for j in range(m):
        num = 1
        while num < 9: # num *=2 >> num 1, 2, 4, 8
            if num & graph[i][j]: # 해당 num 방향에 벽이 있다면
                visited = [[0] * m for _ in range(n)] # visited 배열초기화
                graph[i][j] -= num # 해당 num 방향 벽 제거
                result3 = max(result3, bfs(i, j)) 
                graph[i][j] += num # 다시 벽 원위치
            num *= 2 # 벽 방향 변경
            
print(result1)
print(result2)
print(result3)

# 성에 있는 방의 개수, 가장 넓은 방 넓이, 하나의 벽을 제거해 얻을 수 있는 가장 넓은 방 크기
# 벽에 대한 정보 : 2진수로 생각했을때 "남동북서" (작은값)

# 2진수 계산을 저렇게 하는거구나

# 어려움.... 손도 못댐..... 근데 또 생각해보면 그냥 bfs 계산이긴해
# 벽 하나 제거했을때 최대 방 넓이 구하는거
    # 벽 하나 제거 - bfs 수행 - max(현재 max값, 새로운 방 넓이) - 제거했던 벽 원위치, visited 다시 생성

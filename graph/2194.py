import sys
input = sys.stdin.readline
from collections import deque

n, m, a, b, k = map(int, input().split())
obstacle = set()
for i in range(k):
    x, y = map(int, input().split())
    obstacle.add((x-1, y-1))
sc, sr = map(int, input().split())
fc, fr = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*m for _ in range(n)]
def bfs():
    queue = deque([(sc-1, sr-1)])
    visited[sc-1][sr-1] = 1
    
    while queue:
        x, y = queue.popleft()
        
        if x == fc-1 and y == fr-1:
            return visited[x][y] - 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]: # 범위안에 없거나, 이미 방문했다면
                continue
            
            check = False # 장애물때문에 못가는지 체크(False면 queue에 담을 수 있음)
            
            # 범위 설정이 어려웠음....
            if i == 0: # 위
                for j in range(b):
                    if (nx, ny + j) in obstacle or ny + j >= m:
                        check = True
                        break
                        
            elif i == 1: # 아래
                for j in range(b):
                    if (nx+a-1, ny + j) in obstacle or ny + j >= m:
                        check = True
                        break
                    
            elif i == 2: # 좌
                for j in range(a):
                    if (nx+j, ny) in obstacle or nx+j >= n:
                        check = True
                        break
                    
            else : # 우
                for j in range(a):
                    if (nx+j, ny+b-1) in obstacle or nx+j >= n:
                        check = True
                        break
            
            if not check:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1 # 시간 체크 필요
    return 0

answer = bfs()
if answer:
    print(answer)
else:
    print(-1)
# 유닛을 목적지까지 움직이기 위해서 필요한 최소이동 횟수
# 기본적 문제와의 차이점 : 유닛이 크기를 가짐
# 시작점 위치와 도착점 위치는 제일 왼쪽 위 한점만 주어짐
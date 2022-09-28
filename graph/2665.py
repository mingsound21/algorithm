import sys
input = sys.stdin.readline
from collections import deque

# 98% valueError 코드
n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

visited = [[[0] * n for _ in range(n)] for _ in range(100)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1
    arr = []
    
    while q:
        x, y, cnt = q.popleft()
        
        if x == n-1 and y == n-1:
            arr.append(cnt)
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and cnt < n*2-3:
                if graph[nx][ny] == 0 and not visited[cnt+1][nx][ny]: # 검은 방
                    visited[cnt+1][nx][ny] = 1
                    q.append((nx, ny, cnt+1))
                    
                elif graph[nx][ny] == 1 and not visited[cnt][nx][ny]: #흰방
                    visited[cnt][nx][ny] = 1
                    q.append((nx, ny, cnt))

    return min(arr)

print(bfs())

# 검은방 = 통과 못함
# 검은방에서 흰방으로 바꾸어야 할 최소의 수를 출력
# 왼쪽 맨 위에서 오른쪽 맨 아래로 이동

# 다른 사람 풀이
# 1261 문제하고 매우 유사

import heapq

n = int(input())
room = []
for _ in range(n):
    room.append(list(map(int, input().rstrip())))
    
visit = [[0]*n for _ in range(n)]

def dijkstra():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    
    while heap:
        a, x, y = heapq.heappop(heap) # 가장 검은방을 최소로 삭제한 것이 먼저 pop
        if x == n-1 and y == n-1:
            print(a)
            return 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                visit[nx][ny] = 1
                if room[nx][ny] == 0: # 검은 방
                    heapq.heappush(heap, [a+1, nx, ny])
                else:
                    heapq.heappush(heap, [a, nx, ny])

dijkstra()
# 힙 - 최솟값, 최댓값을 계속해서 호출해야하는 상황인 경우 힙을 사용해서 구현하면 좋다
# 힙은 첫번째 요소를 기준으로 정렬함

# 또 다른 사람 풀이
n = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(map(int, input().rstrip())) for _ in range(n)]

def bfs():
    q = deque([(0, 0)])
    visited = [[-1]*n for _ in range(n)]
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        if x == n-1 and y == n-1:
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] == 1: # 흰 방
                    q.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else: # 검은 방
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

print(bfs())
# 흰 방을 appendleft했기 때문에 먼저 탐색 >> 처음 도착장소에 도착했을 때 visited에 저장된 값이 최소로 검은 방 지운 개수

# 어려움...
# 핵심은 queue에서 검은방 최소로 삭제한 루트를 먼저 가도록 유도해서 처음으로 도착 장소에 도착했을 때 삭제한 검은 방의 개수를 출력
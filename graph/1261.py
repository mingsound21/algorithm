import sys
input = sys.stdin.readline
from collections import deque
import heapq

m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0, 0)])
    visited[0][0] = 1
    
    while queue:
        x, y, cnt = queue.popleft()
        
        if x == n-1 and y == m-1:
            print(cnt)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 1: # 벽
                    queue.append((nx, ny, cnt + 1))
                else:
                    queue.appendleft((nx, ny, cnt))

bfs()

def use_heap():
    heap = []
    visited = [[0] * m for _ in range(n)]
    heapq.heappush(heap,(0, 0, 0))
    visited[0][0] = 1
    

    while heap:
        cnt, x, y = heapq.heappop(heap) # heap은 첫번째 원소 기준으로 정렬됨
        
        if x == n-1 and y == m-1:
            print(cnt)
            return
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if graph[nx][ny] == 1: # 벽
                    heapq.heappush(heap, (cnt + 1, nx, ny))
                else: # 빈 방
                    heapq.heappush(heap, (cnt, nx, ny))

# use_heap()
# 빈 방 0, 벽 1
# (1, 1)에서 (n, m)으로 이동할때 벽을 최소 몇개 

# 2665문제 풀이 블로그에서 비슷하다고해서 풀어봤는데 거의 같은 문제네...
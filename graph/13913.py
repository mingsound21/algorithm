import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

dx = [-1, 1]
visited = [-1] * 100001

def bfs():
    queue = deque([(n, 0)])
    visited[n] = 1
    
    while queue:
        x, cnt = queue.popleft()

        if x == k:
            return cnt
        
        for i in range(3):
            if i == 2:
                nx = x * 2
            
            else:
                nx = x + dx[i]
        
            if 0 <= nx <= 100000 and visited[nx] == -1:
                visited[nx] = x # 나중에 k부터 시작해서 역으로 루트 가져오기
                queue.append((nx, cnt + 1))

time = bfs()
print(time)

route = [k]
while k != n:
    route.append(visited[k])
    k = visited[k]
print(*route[::-1])


# x-1, x+1, 2*x 위치로 이동
# 수빈이 동생 찾을 수 있는 가장 빠른 시간
# 다른 문제랑 차이점 : 어떻게 이동해야하는지까지 출력
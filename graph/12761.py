import sys
input = sys.stdin.readline
from collections import deque

a, b, n, m = map(int, input().split())
visited = [0] * 100001

dx = [-1, +1, +a, -a, +b, -b]
dx2 = [a, b]
def bfs():
    queue = deque([])
    for i in range(6):
        nx = n + dx[i]
            
        if nx < 0 or nx > 100000:
            continue
            
        queue.append((nx, 1))
        visited[nx] = 1

    for i in range(2):
        nx = n * dx2[i]
            
        if nx < 0 or nx > 100000:
            continue
            
        queue.append((nx, 1))
        visited[nx] = 1

    while queue:
        
        x, cnt = queue.popleft()
        
        if x == m:
            return cnt
        
        for i in range(6):
            nx = x + dx[i]
            
            if nx < 0 or nx > 100000 or visited[nx]:
                continue
            
            queue.append((nx, cnt+1))
            visited[nx] = 1

        for i in range(2):
            nx = x * dx2[i]
            
            if nx < 0 or nx > 100000 or visited[nx]:
                continue
            
            queue.append((nx, cnt+1))
            visited[nx] = 1
        
print(bfs())
            
# +1, -1
# A, B만큼 좌우로 점프
# A배, B배 위치로 이동가능


# 다른 사람 풀이
def bfs2():
    while q:
        x = q.popleft()
        for i in range(8):
            if i < 6:
                nx = x + dx[i]
            else:
                nx = x * dx[i]
            
            if 0 <= nx <= 100000 and visited[nx] == 0:
                q.append(nx)
                visited[nx] = 1
                cnt[nx] = cnt[x] + 1

a, b, n, m = map(int, input().split())
cnt = [0 for _ in range(100001)]
visited = [0 for _ in range(100001)]
visited[n] = 1
dx = [1, -1, a, -a, b, -b, a, b]
q = deque()
q.append(n)
bfs2()
print(cnt[m])
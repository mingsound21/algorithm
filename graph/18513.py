import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
water = list(map(int, input().split()))
visited = set() # idea! [배열길이 긴 경우 >> visited를 배열 말고 set으로 처리]
# >> 보통 0으로 채워진 배열을 visited로 사용한 경우가 많았는데, 배열 길이가 긴 경우에는 set으로 visited 처리!

dq = deque()
for i in water:
    dq.append((i, 1)) # 위치, 불행도
    visited.add(i)
    
result = 0 # 불행도 합 최솟값
now_build = 0 # 현재까지 지어진 집 수 

while dq:
    now, b = dq.popleft()
    
    for d in [-1, 1]:
        nx = now + d
        if nx in visited:
            continue
        
        visited.add(nx)
        result += b
        now_build += 1
        dq.append((nx, b + 1))
        
        if now_build == k:
            dq = list()

print(result)

# 불행도 : 집에서 가장 가까운 샘터까지 거리
# 불행도의 합이 최소가 되도록

# 샘터를 기준으로 -1, +1 방향으로 bfs진행
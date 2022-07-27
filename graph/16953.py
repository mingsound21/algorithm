import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())

def bfs():
    queue = deque([(a, 1)])
    
    while queue:
        v, cnt = queue.popleft()
        
        if v == b:
            print(cnt)
            exit(0)
        if v*2 <= b:
            queue.append((v*2, cnt + 1))
        if int(str(v) + '1') <= b:
            queue.append((int(str(v) + '1'), cnt+1))
    print(-1)
    exit(0)

bfs()
# BFS

# 메모리 초과 -> 16 ~ 19줄로 고침
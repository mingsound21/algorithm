from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 10 ** 5
dist = [0] * (MAX + 1)

def bfs():
    queue = deque([n])
    
    while queue:
        x = queue.popleft()
        
        if x == k :
            return dist[x]
        
        for nx in (x-1, x+1, 2*x): 
            if 0 <= nx <= MAX  and not dist[nx]: # not dist[nx] 체크 안하면 메모리 초과
                dist[nx] = dist[x] + 1
                queue.append(nx)
                    
print(bfs())

# 좌표의 상한을 정해 놓지 않으면 최악의 경우 큐에 엄청나게 많은 원소가 들어감
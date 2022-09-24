import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

queue = deque([n])
visited = [0] * 100001
visited[n] = 0

ans_count = 0
ans_way = 0
while queue:
    x = queue.popleft()
    count = visited[x]
    
    if x == k:
        ans_count = count
        ans_way += 1
        continue
    
    for nx in [x-1, x+1, 2*x]: # dx 대신 이렇게할 수도 있구나
        if 0 <= nx < 100001:
            # 일단, x까진 최단거리에 도착했음이 확실
            if visited[nx] == 0 or visited[nx] == visited[x] + 1: # 방문을 하지 않았거나, 이미 nx를 방문한 상태더라도 가장 빨리 nx를 방문했을때와 같은 시간에 nx에 도착한 경우
                queue.append(nx)
                visited[nx] = count + 1
                
print(ans_count)
print(ans_way)

# 1초뒤 x-1, x+1, 2*x위치로 이동
# n에서 k로 이동할 수 있는 가장 빠른 시간과, 가장 빠른 시간으로 찾는 방법 수를 출력
# 방법의 수,,, 다른 bfs 루트로 nx에 도착했더라도, nx에 최단시간에 도착한 시각과 같은 시각에 도착했다면, queue에 넣는 것으로....
import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
queue = deque()
queue.append(n)
visited = [-1 for _ in range(100001)]
visited[n] = 0

while queue:
    s = queue.popleft()
    
    if s == k:
        print(visited[s])
        break
    
    if 0 <= s-1 < 100001 and visited[s-1] == -1:
        visited[s-1] = visited[s] + 1
        queue.append(s-1)
    
    if 0 <= 2*s < 100001 and visited[s*2] == -1:
        visited[s*2] = visited[s]
        queue.appendleft(s*2) # 2*s가 다른 연산보다 더 높은 우선순위를 가지기 위함 
#        >> 1697 숨바꼭질에서는 모든게 다 1초걸렸으나, 이번 문제에서는 2*s는 0초 걸려서
    if 0 <= s+1 < 100001 and visited[s+1] == -1:
        visited[s+1] = visited[s] + 1
        queue.append(s+1)

# 목적지까지의 최단거리를 구하는 문제라서 BFS

# 걷는다면 1초뒤 x-1, x+1
# 순간이동 0초뒤 2*x

# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간
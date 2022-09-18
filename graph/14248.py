import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
data = list(map(int, input().split()))
s = int(input())
visited = [0] * n

def bfs():
    queue = deque([s-1])
    visited[s-1] = 1
    cnt = 0
    while queue:
        x = queue.popleft()
        cnt += 1
        for v in [x+data[x], x-data[x]]:
            if 0 <= v < n and not visited[v]:
                visited[v] = 1
                queue.append(v)
    
    return cnt

print(bfs())
# 돌다리에 적혀있는 숫자만큼 왼쪽 or 오른쪽으로 점프 가능
# 돌다리 밖으로 나갈 수는 없음
# 자기가 방문 가능한 돌 개수


# 다른 사람 풀이
n = int(input())
graph = list(map(int, input().split()))
s = int(input())
visited = [False] * n

def dfs(start):
    visited[start] = True
    for i in range(2):
        left = start - graph[start]
        right = start + graph[start]
        
        if not left < 0:
            dfs(left)
        if not right >= n:
            dfs(right)

dfs(s-1)

print(visited.count(True))
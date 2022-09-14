import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v, depth):
    if depth == 4:
        print(1)
        exit(0)
        
    for u in graph[v]:
        if not visited[u]:
            visited[u] = True
            dfs(u, depth + 1)
            visited[u] = False # 다시 해제를 해줘야 depth 계산을 제대로 할 수 있음

for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False # 다시 해제를 해줘야 depth 계산을 제대로 할 수 있음
    
print(0)

# 조건에 맞는 친구관계 존재하면 1, 없으면 0

# 문제 이해가 어려웠음
# 문제 보고 방향 그래프인지 무방향 그래프인지 구분이 필요할 듯

# 풀이 idea
# 해당 그래프의 깊이가 5임을 증명
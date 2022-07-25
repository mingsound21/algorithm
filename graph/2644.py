import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph =[[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# DFS
visited_dfs = [False for _ in range(n+1)]
dist_dfs = [0 for _ in range(n+1)]
def dfs(v):
    visited_dfs[v] = True
    
    for i in graph[v]:
        if not visited_dfs[i]:
            dist_dfs[i] = dist_dfs[v] + 1
            dfs(i)

# BFS
dist_bfs = [0 for _ in range(n+1)]
def bfs(s):
    visited_bfs = [False for _ in range(n+1)]
    
    
    queue = deque([s])
    visited_bfs[s] = True
    
    while queue:
        v = queue.popleft()
        
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True
                dist_bfs[i] = dist_bfs[v] + 1

bfs(p1)

if(dist_bfs[p2] != 0):
    print(dist_bfs[p2])
else:
    print(-1)
    


# 풀이 +
# 나는 트리 구조를 생각해서 푼 것 같음
# 근데 dfs, bfs를 사용해서 한 정점에서 다른 정점까지 이동한 거리 출력 문제
# 트리구조로 생각했을 때 풀기 어려우면 그래프 구조도 생각
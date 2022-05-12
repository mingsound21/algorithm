from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v, visited = [],):
    visited.append(v)
    check[v] = True
    
    for u in sorted(graph[v]):
        if not check[u]:
            dfs(u, visited)
    return visited

def bfs(v):
    visited = [v]
    check[v] = True
    queue = deque([v])
    
    while queue:
        v = queue.popleft()
        for u in sorted(graph[v]):
            if not check[u]:
                visited.append(u)
                queue.append(u)
                check[u] = True
    return visited

check = [False for _ in range(n+1)]
print(' '.join(map(str, dfs(v))))
check = [False for _ in range(n+1)]
print(' '.join(map(str,bfs(v))))




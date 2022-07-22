from collections import deque



n, m, start_node = map(int, input().split())

graph = [[] for _ in range(n+2)]

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited_dfs = [False for _ in range(n+2)]
visited_bfs = [False for _ in range(n+2)]

def dfs(graph, v, visited_dfs):
    visited_dfs[v] = True
    print(v, end = " ")
    
    for i in sorted(graph[v]):
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

def bfs(graph, start, visited_bfs):
    queue = deque([start])
    
    visited_bfs[start] = True
    
    
    while queue:
        v = queue.popleft()
        print(v, end = " ")
        
        for i in sorted(graph[v]):
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(graph, start_node, visited_dfs)
print()
bfs(graph, start_node, visited_bfs)
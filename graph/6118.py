import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**7)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
def bfs():
    q = deque([1])
    visited[1] = 1
    
    while q:
        x = q.popleft()

        for v in graph[x]:
            if not visited[v]:
                visited[v] = visited[x] + 1
                q.append(v)

    
bfs()

_max = max(visited)
answer = []
for i in range(1, n+1):
    if visited[i] == _max:
        answer.append(i)
        
print(answer[0], visited[answer[0]] -1, len(answer))

# 1번노드에서 가장 거리가 멀리 떨어져 있는 헛간을 찾아라
# 헛간 번호(여러개면 가장 작은 것), 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간의 개수


# dfs도 가능할 것 같았는데 복잡해짐... bfs로 푸는게 맞는듯
# 이렇게 짜면 문제 예시 상황에서 1-2가 더 짧은 거리임에도 불구하고 1-3-2를 통한 길을 먼저 방문해서 이미 방문처리가 되어버림
# def dfs(v, cnt):
#     visited[v] = cnt + 1
    
#     for u in graph[v]:
#         if not visited[u]:
#             dfs(u, cnt + 1)
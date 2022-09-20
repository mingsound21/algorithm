import sys
input = sys.stdin.readline
from collections import deque

a, b = map(int, input().split())
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v  =map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)


visited = [-1] * (n+1)
def bfs():
    queue = deque([a])
    visited[a] = 0
    
    while queue:
        x = queue.popleft()
        
        for v in graph[x]:
            if visited[v] == -1:
                visited[v] = visited[x] + 1
                queue.append(v) # 큐에 넣는 걸 자꾸 까먹어...

bfs()
print(visited[b])
# -----------------------------------------------
# 틀린 풀이 - dfs 사용
# def dfs(x):
#     for v in graph[x]:
#         if visited[v] == -1:
#             visited[v] = visited[x] + 1
#             dfs(v) # 이것도 자꾸 까먹음...


# visited[a] = 0
# dfs(a)
# -----------------------------------------------

# a를 b로 바꾸려면 : 연결된 노드를 거쳐서
# a에서 b까지 가기 위해 거쳐야하는 최소 간선 수
# 치환 불가능하면 -1 출력

# dfs, bfs 상관 없을듯?
# >> 아니었다...! 최단거리를 구하는 문제여서 dfs를 사용하면 처음발견한 해답이 최단거리가 아닐 수 있음(이 문제의 예시2를 넣어보면 알 수 있음)

# -----------------------------------------------
# <언제 dfs, bfs를 사용해야하나...!?>
# 1. 그래프의 모든 정점 방문 : DFS, BFS

# 2. 경로의 특징을 저장하는 문제 : DFS
# 예) 각 정점에 숫자가 있고, a부터 b까지의 경로를 구하는데 같은 숫자가 있으면 안된다는 문제
# 각각의 경로 마다 그 특징을 저장해두어야하는 문제는 경로를 쭈루룩 따라가는 DFS 사용

# 3. 최단거리 구하기 : BFS
# DFS로 경로를 탐색하면 처음 발견하는 해답이 최단거리가 아닐수 있지만, BFS는 현재 노드에서 가까운 곳 부터 찾기 때문에 경로를 탐색할 때 먼저 찾아지는 해답이 곧 최단거리임

# 4. 검색 대상 그래프가 많이 클 때 : DFS

# 5. 검색 대상 그래프가 많이 크지 않고, 검색 시작 지점으로부터 우너하는 대상이 별로 멀지 않으면 : BFS

# 참고 : https://duckracoon.tistory.com/entry/DFS%EC%99%80-BFS-%EA%B0%81%EA%B0%81-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import deque

# 메모리 초과,,, 틀린 풀이

INF = 300001
n, m, K, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


dist = [INF for _ in range(n+1)]
def dfs(v, cnt):
    for e in graph[v]:
        if dist[e] == 0:
            dist[e] = cnt
        else:
            dist[e] = min(dist[e], cnt)
        dfs(e, cnt +1)

dfs(x, 1)

check = 0

for i in range(1, n+1):
    if dist[i] == K:
        check = 1
        print(i)

if check == 0:
    print(-1)
    
# 최단거리

# 다른 사람 맞은 풀이
# 1. bfs 사용
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == k:
                    answer.append(i)
    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(x)

# 2. 다익스트라 사용
import heapq
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # (노드, 가중치)
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) # 방문하지 않은 노드 중에서 비용가장 작은 것 선택
        if distance[now] < dist: # 다른 경로로 더 빠른 경로가 존재한다는 의미이므로 패스
            continue
        for j in graph[now]: # 해당 노드와 인접한 노드들 간의 거리 계산
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(x)
answer = []
for i in range(1, n+1):
    if distance[i] == k:
        answer.append(i)
    
if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)

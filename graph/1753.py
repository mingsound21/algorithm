import sys
input = sys.stdin.readline
import heapq

INF = sys.maxsize

n, m = map(int, input().split())
start = int(input())

graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    
distance = [INF for i in range(n+1)]

def dijkstra(start):
    # 시작 정점 관련 처리
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (distance[start], start))
    
    while queue:
        dist, node = heapq.heappop(queue)
        
        if distance[node] < dist:
            continue
    
        for v, w in graph[node]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))

dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])

# 방향 그래프

# 다익스트라 : 하나의 정점에서 나머지 모든 정점까지의 최단 거리를 찾는 알고리즘
# > 단, 음의 간선을 포함할 수 없음
# > 하나의 최단거리를 구할때 그 이전까지 구했던 최단거리 정보를 그대로 사용

# 작동과정
# 1. 출발 노드 설정
# 2. 출발 노드 기준으로 각 노드의 최소 비용 저장
# 3. 방문하지 않은 노드 중에서 가장 비용이 적은 노드를 선택
# 4. 해당 노드를 거쳐서 특정한 노드로 가는 경우를 고려해 최소비용 갱신
# 5. 3~4과정을 반복

# cf. 플로이드-워셜 : 모든 정점의 최단거리 구하기
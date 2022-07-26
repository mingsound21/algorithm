# 하나의 시작 정점으로부터 모든 다른 정점까지의 최단 경로찾는 알고리즘

# 음의 간선이 존재하지 않을때 정상 작동

# 1. 출발 노드 설정
# 2. 최단 거리 테이블 초기화
# 3. 인접노드이면서, 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 해당 노드의 인접 노드로 가는 간선 비용을 계산해 최단 거리 테이블 업데이트
# 5. 3~4과정 반복

# 필요한 것 : 최단거리 기록 리스트, 방문노드 기록 리스트

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 방법 1) 순차 탐색
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split()) # n : 정점 수, m : 간선 수
start = int(input())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

# 방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_value = INF
    index = 0
    # 모든 정점 순차 탐색
    for i in range(1, n+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index

# 다익스트라
def dijkstra(start):
    # 시작노드 거리 0으로 초기화, 방문처리
    distance[start] = 0
    visited[start] = True
    
    # 시작 노드의 인접 노드들 거리 테이블 update
    for v, w in graph[start]:
        distance[v] = w
    
    
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        
        # 해당 노드와 인접한 노드들 간의 거리 계산
        for nextv, nextw in graph[now]:
            cost = distance[now] + nextw
            if cost < distance[nextv]:
                distance[nextv] = cost

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('도달 할 수 없음')
    else:
        print(distance[i])

# 시간 복잡도 : O(v^2)
# >> v : 노드의 개수
# >> 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택하기 위해서 
# 매 단계마다 거리 테이블길이(= 노드 개수)만큼 순차 탐색

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# 방법 2) 최소 힙 사용
import heapq

n, m = map(int, input().split())
start = int(input())

distance = [INF] * (n+1)

graph = [[] for i in range(n+1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append(b, w)

def dijkstra_heap(start):
    queue = []
    
    heapq.heappush(queue, (0, start)) # (거리, 노드번호), heapq는 첫번째 원소를 우선순위로 힙 구성
    distance[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue) # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        
        # visited 리스트를 사용하지 않고 아래의 if문을 사용
        # heapq에 (거리, 노드)순으로 넣다보니, 동일한 노드라도 큐에 저장이 됨
        # 예) queue[(7, 'B'), (10, 'B')]
        if distance[now] < dist:
            continue
        
        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(queue, (cost, v))

# 실행
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('도달 할 수 없음')
    else:
        print(distance[i])
                
    
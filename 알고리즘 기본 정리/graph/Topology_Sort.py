# 위상 정렬 : 방향 그래프의 모든 노드를 "방향성에 거스르지 않도록 순서대로 나열하는 것"
# 진입차수 : 특정한 노드로 들어오는 간선의 개수

# 위상 정렬 알고리즘
# 시간 복잡도 : O(V + E)

# 1. 진입차수가 0인 노드를 큐에 넣는다
# 2. 큐가 빌때까지 다음의 과정 반복
# 2-1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
# 2-2) 새롭게 진입차수가 0이된 노드를 큐에 넣음

#----------------------------------------------------------------------------------------
from collections import deque

v, e = map(int, input().split())
# 모든 노드에 대한 진입차수 0으로 초기화
indegree = [0] * (v + 1)
graph = [[] for i in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    
    # 처음 시작할때, 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)
    
    # 큐가 빌때까지
    while q:
        now = q.popleft()
        result.append(now)
        
        # 해당 원소와 연결된 노드들의 진입차수 1빼기
        for i in graph[now]:
            indegree[i] -= 1
            
            # 새롭게 진입차수가 0이되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end = " ")

    
topology_sort()

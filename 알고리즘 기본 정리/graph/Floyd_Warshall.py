# 모든 정점 사이 최단 경로 찾는 탐색 알고리즘 : O(N^3)
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 개수, 간선 개수 입력 받기

# 2차원 리스트를 만들고, 모든 값으로 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)] 

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # k를 거쳐서 가는 경로가 더 짧으면 갱신됨

# 결과 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('INFINITY', end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()
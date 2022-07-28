import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c
    
    
for k in range(n+1):
    for i in range(n+1):
        if i == k:
            continue
        
        for j in range(n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

for i in range(1, n+1):
    graph[i][i] = 0
    
for i in range(1, n+1):
    for j in range(1, n+1):
        if(graph[i][j] == INF):
            print(0, end = " ")
        else:
            print(graph[i][j], end = " ")
    print()


# floyd_warshall
# 모든 정점사이 최단 경로 찾기

# cf) 다익스트라
# 하나의 시작 정점으로부터 모든 다른 정점까지의 최단 경로찾는 알고리즘
# 음의 간선이 존재하지 않을때 정상 작동
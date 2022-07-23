# 모든 정점 사이 최단 경로 찾는 탐색 알고리즘
import sys

INF = sys.maxsize

def Floyd_Warshall():
    dist = [[INF] * n for i in range(n)] # 최단 경로를 담는 배열
    
    # 최단 경로를 담는 배열 초기화
    for i in range(n):
        for j in range(n):
            dist[i][j] = a[i][j]
            
    for k in range(n): # 경유점
        for i in range(n): # 시작점
            for j in range(n): # 끝점
                # k를 거쳤을때 경로가 더 짧아지면
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    return dist
    

n = 4 # 정점 수
a = [[0, 2, INF, 4], [2, 0, INF, 5], [3, INF, 0, INF], [INF, 2, 1, 0]]

dist = Floyd_Warshall()

for i in range(n):
    for j in range(n):
        print(dist[i][j], end = " ")
    print()
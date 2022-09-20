import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]

# 트리 구현
for i in range(n):
    a, b, w = map(int, input().split()) # 부모 노드, 자식 노드, 가중치
    graph[a].append((b, w))
    graph[b].append((a, w))
    

def dfs(x, wei):
    for a, b in graph[x]:
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)

distance = [-1] * (n+1)
distance[1] = 0 # 처음에 아무노드(= 루트)에서 가장 거리가 먼 노드을 찾음 (= start)
dfs(1, 0)

start = distance.index(max(distance)) # 1번에서 가장 먼 거리를 가진 노드를 찾음
distance = [-1] * (n+1)
distance[start] = 0 # start에서 가장 거리가 먼 것 까지의 거리가 트리의 지름
dfs(start, 0)

print(max(distance))

# 트리 : 사이크 없는 무방향 그래프 
# >> 트리에선 어떤 두 노드를 선택해도 둘 사이 경로가 항상 1개만 존재
# 입력 : 루트가 있는 트리를 "가중치가 있는" 간선들로 줄때 트리의 지름을 출력하는 프로그램

# 다른 사람 맞는 풀이)
# >> bfs 2번해서 O(n)의 시간 복잡도로 구현 가능

# 1. 트리에서 아무 노드를 잡고, 그 노드에 대한 가장 먼 노드를 구하고 그 노드를 n1이라고 함
# 2. n1에 대한 가장 먼 노드를 한번더 구함, 그 노드를 n2라고함
# 3. n1과 n2의 거리 = 트리의 지름

# 참고 : https://koosaga.com/14
# 참고 : https://kyun2da.github.io/2021/05/04/tree's_diameter/



# 어려움....
# 하도 문제들을 bfs로만 풀어서 dfs가 익숙치 않음...
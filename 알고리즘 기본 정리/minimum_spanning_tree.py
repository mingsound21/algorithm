# 신장 트리 : 하나의 그래프에서 모든 노드를 포함하면서, 사이클이 존재하지 않는 부분 그래프

# 최소 신장 트리 (minimum spanning tree)
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 가중치의 합이 최소인 트리

# 1) Kruskal
# 방법)
'''
    1. 간선 정렬(오름차순)
    2. 간선이 잇는 두 정점의 root를 찾음
    3. 다르다면 하나의 root를 바꾸어 연결
    >> 2, 3 과정을 통해서 현재 간선이 노드들 간의 사이클을 발생시키는 지 확인해,
        발생시키지 않는 경우, 최소신장트리에 포함
'''
# 2) Prim
'''
    1. 임의의 정점 선택
    2. 해당 정점에서 갈 수 있는 간선을 minheap에 넣음
    3. 최소값을 뽑아 해당 정점을 방문 안했다면 선택
'''

# kruskal은 간선 정렬이 필요
# >> 간선 적은 경우 kruskal, 많은 경우 prim을 사용
# >> kruskal은 간선 기준, prim은 정점 기준
# >> 두 알고리즘 모두 음의 간선이 포함되어도 됨.

# cf. 다익스트라
# 다익스트라는 전체 요소를 "연결"하는 것이 아닌, 한 정점에서 다른 정점으로 가는 가장 짧은 방법을 구할 때 사용

# ==============================================================================================================

# kruskal
# 1. root를 저장하는 Vroot 배열 생성
# 2. 간선들(Elist)를 가중치 기준으로 정렬
# 3. 간선들이 이은이 두 정점을 find함수를 통해 root(sRoot, eRoot)를 찾음
# 4. 두 root가 다르다면 큰 root 값을 작은 root 값으로 만들어 연결되게 함
# 5. 가중치를 더함
import heapq
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)] # root를 저장하는 배열, (root는 연결 요소중 가장 작은 값, 처음에는 자기자신을 저장)
Elist = [] # 간선들
for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key = lambda x : x[2]) # 간선 가중치 기준으로 정렬

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0

for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot: # 같다면 두 정점은 이미 이어졌음
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w

print(answer)

# ==============================================================================================================
# prim

import heapq

V, E = map(int, input().split())
visited = [False] * (V+1) # 방문 여부
Elist = [[] for _ in range(V+1)] # 간선 저장
heap = [[0, 1]] # 1번 정점 부터 시작

for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])
    
answer = 0
cnt = 0
while heap:
    if cnt == V: # 모든 정점을 방문했다는 의미
        break
    
    w, s = heapq.heappop(heap) # 현재 그래프에서 가장 weight가 작은 간선을 골라
    if not visited[s]: # 방문하지 않은 간선일 경우 
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]: # 해당 정점에서 갈 수 있는 간선 모두 heap에 추가
            heapq.heappush(heap, i)
            
print(answer)
import sys
input = sys.stdin.readline

# n = int(input())
# graph = [0]
# for i in range(n):
#     a = int(input())
#     graph.append(a)

# def dfs_check_cycle(start, v):
#     visited.add(v)
    
#     if graph[v] not in visited:
#         return dfs_check_cycle(start, graph[v])
#     elif graph[v] in visited and start == graph[v]:
#         return True
    
#     return False # graph[v] in visited and start != graph[v]

# answer = []
# for i in range(1, n+1):
#     visited = set()
#     if dfs_check_cycle(i, i):
#         answer.append(i)

# print(len(answer))
# for v in sorted(answer):
#     print(v)
        
# 첫째줄과 둘째줄에서 뽑은 정수들이 이루는 집합이 일치하는 것중 개수 최대
# >> 사이클이 있는 것들


# 다른 사람 풀이
# 둘째 줄의 노드가 윗 줄의 노드를 가리키고 있는 한방향 그래프로 바꾸어 생각
# 사이클을 찾아내, 사이클을 구성하는 노드를 모두 찾아내면 됨
# >> 나는 첫줄 노드가 둘째줄 노드를 가리키도록 문제 품 - graph를 2차원으로 만들 필요가 없음(각 첫줄 노드가 가리키는 것은 단 하나)

# 사이클 : 인접한 노드 확인시, 이미 방문한 노드 또 등장한다면 사이클 존재

def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    
    for v in graph[u]:
        if v not in visited:
            dfs(v, visited.copy()) # 복사본 만드는 이유 : 서로 다른 갈래로 dfs
        else:
            result.extend(list(visited))
            return

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    v = int(input())
    graph[v].append(i)
    
checked = [0 for _ in range(n+1)] # checked 사용해서 한번의 dfs로 해당 사이클에 포함된 모든 노드 가져옴
result = []
for i in range(1, n+1):
    if not checked[i]:
        dfs(i, set([]))

print(len(result))
for v in sorted(result):
    print(v)

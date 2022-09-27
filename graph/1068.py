import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
data = list(map(int, input().split()))
delete_node = int(input())

graph = [[] for _ in range(n)]

for i in range(len(data)):
    if data[i] == -1:
        root = i
        continue
    
    graph[data[i]].append(i)


graph[delete_node] = [] # delete_node의 자식 지우기, n번 노드가 하나의 부모와 연결되니까 이렇게 지워도 되는듯
if delete_node == root:# root == 삭제할 노드이면 그래프가 아예 없음
    print(0)
    exit()
    
graph[data[delete_node]].remove(delete_node) # delete_node의 부모에서 delete노드 삭제

# BFS 버전
def bfs(root):
    visited = [0] * n
    queue = deque([root])
    visited[root] = 1
    cnt = 0
    
    while queue:
        x = queue.popleft()
        
        if len(graph[x]) == 0:
            cnt += 1
            continue
        
        for v in graph[x]:
            if not visited[v]:
                visited[v] = 1
                queue.append(v)
    
    return cnt
# print(bfs(root))

#---------------------------------------
# DFS 버전
visited_dfs = [0] * n
def dfs(v):
    visited_dfs[v] = 1
    
    if len(graph[v]) == 0:
        return 1
    
    dfs_cnt = 0
    for u in graph[v]:
        if not visited_dfs[u]:
            dfs_cnt += dfs(u)
    
    return dfs_cnt

print(dfs(root))

# 트리가 주어졌을때 노드 하나 지움
# 남은 트리에서 리프 노드의 개수를 구하기
# 노드와 노드의 자손 모두 제거됨

# del : index로 삭제
# del arr[3]
# del arr[3:]

# remove : 값으로 삭제
# arr.remove(3) # 3이라는 숫자가 삭제
# >> 단, 3이 여러개 있어도 맨 처음 1개만 삭제됨


# 다른 사람 코드

def dfs2(num, arr):
    arr[num] = -2 
    
    for i in range(len(arr)): # 모든 정점 한번씩 돌면서
        if num == arr[i]: # 만약 i번째의 부모 == num이라면
            dfs(i, arr)

n = int(input())
arr = list(map(int, input().split()))
k = int(input())


dfs(k, arr) # 지울 노드에 대해서 dfs를 수행해서 방문한것은 -2로 표시
count = 0
for i in range(len(arr)): # 모든 정점을 돌면서
    if arr[i] != -2 and not in arr: # 방문하지 않았고, 부모가 아니라면(arr배열에는 부모가 저장되어있음)
        count += 1 # leaf 노드
print(count)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
par = [-1] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(n):
    for i in tree[n]:
        if par[i] == -1: # 부모노드 아직 없으면
            par[i] = n # 1부터 차례로 leaf node로 내려가니까
            dfs(i)
            

def bfs(s):
    queue = deque([s])
    
    while queue:
        v = queue.popleft()
        
        for i in tree[v]:
            if par[i] == -1:
                par[i] = v
                queue.append(i)
                
dfs(1)
# bfs(1)

for i in range(2, n+1):
    print(par[i])
    
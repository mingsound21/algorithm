import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
com = [[] for _ in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())
    com[b].append(a)



def bfs(start):
    visited = [False] * (n+1)
    visited[start] = True
    queue = deque([start])
    
    while queue:
        v = queue.popleft()
        for i in com[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return sum(visited)

_max = 0
result = [0]
for i in range(1, n+1):
    bfs_result = bfs(i)
    _max = max(_max, bfs_result)
    result.append(bfs_result)

# print('result', result)
for i in range(1, n+1):
    if result[i] == _max:
        print(i, end = ' ')

# A가 B를 신뢰하면, B를 해킹하면 A도 해킹
# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호 오름차순으로 출력
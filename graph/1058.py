import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
s = []
visited = [[0] * n for _ in range(n)]

def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                if s[i][j] == 'Y' or (s[i][k] == 'Y' and s[k][j] == 'Y'): # i - j가 친구이거나 k가 i, j와 동시에 친구라면
                    visited[i][j] = 1 # i - j는 친구
                    
for i in range(n):
    s.append(list(input().strip()))
    
floyd()
result = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if visited[i][j] == 1:
            cnt += 1
            
    result = max(result, cnt)
    
print(result)

# C가 B와 친구이고, A와 친구이면 A와 B는 친구가된다.

# 처음엔 dfs로 풀면 되겠다고 생각했음...
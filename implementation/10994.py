import sys
input = sys.stdin.readline

n = int(input())

N = 1 + 4 * (n-1)
graph = [[' '] * N for _ in range(N)]

a = 0
b = N-1

while True:
    if a == b:
        graph[a][b] = '*'
        break
    
    for i in range(a, b+1):
        graph[i][a] = '*'
        graph[i][b] = '*'
        graph[a][i] = '*'
        graph[b][i] = '*'
    a += 2
    b -= 2
    
for g in graph:
    print("".join(g))
    
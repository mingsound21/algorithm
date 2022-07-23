import sys
input = sys.stdin.readline

n = int(input())
adja_matrix = []

for _ in range(n):
    adja_matrix.append(list(map(int, input().split())))

graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if adja_matrix[i][j] == 1:
            graph[i].append(j)

def dfs(s, v, answer):
    
    for i in graph[v]:
        if answer[s][i] == 0:
            answer[s][i] = 1
            dfs(s, i, answer)
    

answer = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    dfs(i, i, answer)
    

for i in range(n):
    for j in range(n):
        print(answer[i][j], end = " ")
    print()

# 1. graph 만들기
# 2. 모든 정점을 시작 정점을 두고, dfs를 돌면서 visit하면 표시
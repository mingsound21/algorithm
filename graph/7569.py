import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int, input().split())
graph = []
tomato = []

for i in range(h):
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().split())))
    graph.append(arr)
                

def bfs(tomato):# tomato는 토마토 들어있는 위치가 모두 들어있는 배열
    queue = deque(tomato)
    day = []
    
    di = [-1, 1, 0, 0, 0, 0]
    dj = [0, 0, -1, 1, 0, 0]
    dk = [0, 0, 0, 0, -1, 1]

    while queue:
        i, j, k = queue.popleft()
        
        for a in range(6):
            ni = i + di[a]
            nj = j + dj[a]
            nk = k + dk[a]
            
            if ni < 0 or ni >= h or nj < 0 or nj >= n or nk < 0 or nk >= m:
                continue
            
            if graph[ni][nj][nk] == 0 :
                graph[ni][nj][nk] = graph[i][j][k] + 1
                day.append(graph[ni][nj][nk])
                queue.append((ni, nj, nk))
    if day:
        maxday = max(day) -1
    else:
        maxday = 0
        
    return maxday

day = []
answer = 0
# 모든 토마토가 처음부터 익은 상태 인지 확인
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                tomato.append((i, j, k))
            if graph[i][j][k] == 0:
                answer += 1
                
# 모든 토마토가 익어있지 않은 경우, bfs해도 토마토 안익은게 있는지 확인        
if answer != 0:
    day = bfs(tomato)
    
    for i in range(h):
        for j in range(n):
            if 0 in graph[i][j]:
                answer = -1
                break
        if answer == -1:
            break

# 토마토가 처음부터 모두 익어있거나, 안익은 토마토가 마지막에도 있지 않은 경우
# 걸리는 시간 중에서 가장 오래걸리는 day 출력
if answer not in (0, -1):
    answer = day

print(answer)



# m : 가로, h : 높이, n: 세로

# 틀린 것을 찾을 수 있었던 반례
'''
3 3 2
0 0 1
0 -1 0
1 0 0
0 1 0
-1 0 0
0 0 0
>>> 맞는 정답 : 3
>>> 내 풀이로 나온 답 : 5
'''
# >> 틀린 이유 : 3중 for문 돌면서 1이 나오면 bfs 돌았더니
# 여러 군데서 퍼지기 시작해서 만날 수도 있다는 것을 간과함

# >> 고치기 : 3중 for문을 bfs 돌기 전에 돌아서 tomato 배열에 tomato 들어있는 위치 모두 담아서
# >> bfs 매개변수로 tomato 배열을 전달
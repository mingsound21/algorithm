import sys
input = sys.stdin.readline
from collections import deque

m, n, h = map(int,input().split()) # mn크기, h상자수

graph = []
queue = deque([]) # 아예 처음 부터 queue에 담아서

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k]) # 토마토의 모든 위치를 담기
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0: # 범위 이렇게 쓰면 깔끔
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0: # 하나라도 토마토 안익은거 있으면 -1 출력하고 바로 종료 -- exit(0) 사용
                print(-1)
                exit(0)
        # 처음부터 토마토 모두 익었을 경우를 아래와 같이 처리
        day = max(day,max(j)) # 토마토가 처음부터 모두 익어있던 경우에는 day = 1
print(day-1)
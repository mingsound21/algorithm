import sys
input = sys.stdin.readline

N = int(input())
find_n = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

graph = [[0] * N for _ in range(N)] # N x N 크기의 0으로 채워진 2차원 배열
n = N**2

x = y = 0
direction = 0
while True:
    graph[x][y] = n
    
    if n == find_n:
        find_x = x + 1
        find_y = y + 1
        
    if n == 1:
        break
        
    n -= 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if nx < 0 or nx >= N or ny < 0 or ny >= N or graph[nx][ny] != 0:
        direction = (direction + 1) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
    
    x = nx
    y = ny

for arr in graph:
    for v in arr:
        print(v, end = " ")
    print()
print(find_x, find_y)


# dx, dy를 아래, 오른쪽, 위쪽, 왼쪽 방향 순으로 저장
# 범위를 벗어나게되거나, 다음 위치에 숫자(0아닌)가 들어있는 경우 방향변경
# 1을 만나면 끝
# >> 마지막 숫자부터 채우기

# 값을 채우면서 찾으려는 n를 발견하면 위치 저장

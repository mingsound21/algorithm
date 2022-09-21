import sys
input = sys.stdin.readline
from collections import deque

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

water = []
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            a = i
            b = j
        
        elif graph[i][j] == '*':
            water.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[-1]*c for _ in range(r)] # -1 : 방문 아직 안했음. 그이외의 숫자 : 방문한 시각을 표현
def bfs(x, y, water):
    q_gosm = deque([(x, y)])
    q_water = deque(water)
    visited[x][y] = 0
    
    # 주의!! 매초마다 ~ 문제
    while True:
        # 1초뒤 물이 들어차는 곳에 고슴도치 갈 수 없으니까, 물을 먼저 체크해줌
        for _ in range(len(q_water)):
            x, y = q_water.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in ['D', 'X', '*']: # 물이 돌과 굴에는 들어찰 수 없음
                    q_water.append((nx, ny))
                    graph[nx][ny] = '*'

        # 고슴도치 이동
        for _ in range(len(q_gosm)):        
            x, y = q_gosm.popleft()
            
            if graph[x][y] == 'D':
                print(visited[x][y])
                exit(0)
                
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == -1 and graph[nx][ny] not in ['*', 'X']:
                    visited[nx][ny] = visited[x][y] + 1
                    q_gosm.append((nx, ny))
        
        if not q_gosm: # 고슴도치 큐가 비었다면(= D에 도착 못함)
            return

bfs(a, b, water)    
print('KAKTUS') # bfs에서 도착 가능하면 exit했으니까


# 비어있는 곳 ., 물 *, 돌 X
# 비버의 굴 D, 고슴도치 위치 S

# 매분마다 고슴도치 상하좌우로 이동가능, 물도 매 분마다 비어있는 칸으로 확장(상하좌우방향으로)
# 고슴도치 물 있는 곳 갈 수 X, 물이 비버의 굴로 들어갈 수 없음
# 고슴도치가 비버의 굴로 이동하기 위해서 필요한 최소시간
# 고슴도치는 물이 찰 예정인 칸으로 이동 불가(즉, 다음 시간에 물이 찰 예정인 칸으로 이동 불가)
# 안전하게 이동 불가능하면 KAKTUS 출력

# 해결과정...
# 메모리 초과 >> 물이 퍼질때 not in ['D', 'X', '*'] 로 물까지 포함시켜주니 해결됨
# 그래도 틀렸습니다 나옴 >> 고슴도치가 돌을 위나, 넘어서 갈 수 없음. 마치 돌 = 벽이었음
# >> 고슴도치 이동시에 not in ['*', 'X']로 변경
import sys
input = sys.stdin.readline
from collections import deque

# 상하좌우, 대각선, 제자리
dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0]
dy = [0, 0, -1, 1, -1, 1, -1, 1, 0]

data = [list(input().rstrip()) for _ in range(8)]
visited = set()

# 벽 위치
walls = set()
for i in range(8):
    for j in range(8):
        if data[i][j] == '#':
            walls.add((i, j))

answer = 0

def bfs():
    global walls
    global visited
    global answer
    
    q = deque([(7, 0)])
    
    while q:
        for _ in range(len(q)): # 대박,, 이거 이 줄 안넣으면, 큐에서 x,y하나씩 꺼낼때마다 wall이동함
            x, y = q.popleft()
            
            # 해당 위치에 벽이 위치하게 되면 pass
            if (x, y) in walls:
                continue
            
            # 도착지점 도달
            if x == 0 and y == 7:
                answer = 1
                break
            
            # 9개 방향에 대해서 
            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= 8 or ny < 0 or ny >= 8 or (nx, ny) in walls or (nx, ny) in visited:
                    continue
                
                visited.add((nx, ny))
                q.append((nx, ny))
        
        # 벽이 있다면 방문 표시 초기화
        if walls:
            visited = set()

        # 1초뒤 벽
        next_wall = set()
        for x, y in walls:
            if x < 7:
                next_wall.add((x+1, y))
        
        # 벽 바꿔치기
        walls = next_wall

bfs()
print(answer)

# 1초마다 모든 벽이 한칸 아래로 이동, 가장 아래에 있다면 사라짐
# 캐릭터 먼저 이동, 그다음 벽 이동
# 벽이 캐릭터 있는 칸으로 이동하면 캐릭터 더이상 이동 못함

# 벽이 아직 있다면, 방문 표시 초기화,,,!!
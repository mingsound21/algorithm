import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, fire):
    fire = deque(fire)
    queue = deque([(x, y)])
    sg_visited = [[0] * w  for _ in range(h)]
    
    sg_visited[x][y] = 1


    while True:
        # 상근 이동 불가 -> while 탈출
        if not queue:
            break
        
        # 불 먼저 이동 -> 그래야 상근이가 불이 다음에 번질곳에 이동 못함
        for _ in range(len(fire)):
            x, y = fire.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위 안에 있고, 불이나 벽이 아닌경우, 불 번지게
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] not in ['#', '*']:
                    graph[nx][ny] = '*' # 이걸 이용해서 fire는 visited 필요 X
                    fire.append((nx, ny))
                    
        
        # 상근 이동
        for _ in range(len(queue)):
            x, y = queue.popleft()
            
            # 테두리에 도착시 return 시간
            if x in [0, h-1] or y in [0, w-1]:
                return sg_visited[x][y]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 범위 안에 있고, 갈 곳이 벽이나 불이 아니라면
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] not in ['#', '*'] and not sg_visited[nx][ny]:
                    sg_visited[nx][ny] = sg_visited[x][y] + 1 # 시간 추가
                    queue.append((nx, ny))
    return -1
                    

for _ in range(int(input())):
    w, h = map(int, input().split())
    graph = [list(input().rstrip()) for _ in range(h)]
    fire = [] # 불 초기 위치 저장
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@': # 상근 초기 위치 저장
                x = i
                y = j
            
            if graph[i][j] == '*':
                fire.append((i, j))
    
    answer = bfs(x, y, fire)
    
    if answer == -1:
        print('IMPOSSIBLE')
    else:
        print(answer)
    
    
    
# 불 : 동서남북으로 매초 퍼져나감
# 상근 : 동서남북 이동 가능
# 단, 벽 통과 X, 불이 1초뒤 붙으려는 곳X, 불이 붙은 곳 X
# 단, 1초뒤에 불이 상근이가 현재 있는 곳으로 오는 것은 가능
# >> 불 먼저 이동한뒤 상근이가 이동
# 얼마나 빨리 탈출 가능한지 출력
# 빈공간 ., 벽 #, 상근 시작 @, 불 *
import sys
input = sys.stdin.readline
from collections import deque

# 틀린 내 풀이
# >> 시간 체크를 time[x][y] + 1이런식으로 하려고 했는데, 두 변중 나중에 닿은면을 기준으로 time 계산이되니까 너무 헷갈림
# >> 그냥 1번의 bfs를 돌면서 주변 공기들만 queue에 담고, 두변의 공기가 닿은 치즈는 공기로 변경만! 하고 -> 1개의 치즈라도 삭제되었다면 시간1추가
# >> 다음 bfs는 다시 [(0,0)] 담긴 queue에서 부터 윗 줄의 과정을 다시 거치기

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0]*m for _ in range(n)]
time = [[0]*m for _ in range(n)]
def bfs():
    # 처음에 치즈에 맞닿아 있는 외부공기 위치들을 queue에 넣어야하는것 같긴한데,,, 어려움
    # >> 이게 문제가 아니라 치즈가 사라지는 시간 계산에서 문제가 있었던 것 같음
    queue = deque([])
    for i in range(n):
        queue.append((i, 0))
        queue.append((i, m-1))
        visited[i][0] = 1
        visited[i][m-1] = 1
        
    for i in range(m):
        queue.append((0, i))
        queue.append((n-1, i))
        visited[0][i] = 1
        visited[n-1][i] = 1
        
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 녹지않은 치즈 위치라면
            if graph[nx][ny] != 0:
                graph[nx][ny] += 1
                if graph[nx][ny] >= 3: # 1은 그냥 치즈임을 나타내고 2부터 1면 외부공기 닿았음을 표시
                    graph[nx][ny] = 0
                    time[nx][ny] = time[x][y] + 1
                    
                    # 이제 외부공기로 변경되었으니까
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                continue
            
            # 방문하지 않은 외부 공기 위치라면
            if not visited[nx][ny] and graph[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                
                # 추가
                if time[x][y] != 0:
                    time[nx][ny] = time[x][y]
    _max = 0
    print('-'*14)  
    for t in time:
        _max = max(_max, max(t))
        print(t)
    return _max - 1

print(bfs())
# 4변 중 2변 이상 외부공기와 접촉하면 녹음
# 치즈가 모두 녹아 없어지는데 걸리는 시간 출력
# 치즈 내에 있는 공기는 접촉해도 상관없으나, "치즈의 내부"라는게 없어지면 그때 부턴 공기접촉시 사라짐
# >> 문제 전제에 모눈종이 맨 가장자리는 치즈가 놓이지 않는 것으로 가정.
# >> 맨 왼쪽 위부터 bfs 시작

# 맞은 다른 사람 풀이 : https://resilient-923.tistory.com/318

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque([0,0])
    visited[0][0] = 1
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 안에 있고, 방문하지 않은 위치라면
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                # 치즈가 있는 위치라면
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1 # 치즈 닿은 변 개수 증가
                else: # 외부 공기 위치라면
                    visited[nx][ny] = 1 # 방문 표시
                    q.append((nx, ny)) # queue에 추가

time = 0
while True:
    visited = [[0] * m for _ in range(n)] # 매 초마다 visited 배열 새로 생성
    
    bfs() # 매초마다 bfs 수행
    flag = 0
    
    # 모든 위치 탐색
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3: # 외부 공기와 2변 이상 닿았다면
                graph[i][j] = 0 # 치즈 삭제 -> 외부 공기로 변경
                flag = 1 # 한개의 치즈라도 삭제되면 flag 1로 변경
            elif graph[i][j] == 2: # 외부 공기와 2변 미만으로 닿았다면
                graph[i][j] = 1 # 다음 초에선 또 다시 bfs를 하니까 다시 한변도 안 닿은것으로 수정
    
    if flag == 1: # 치즈 삭제가 발생했다면
        time += 1 # 시간 추가
    else: # 치즈 삭제가 발생하지 않았다면 중지
        break
    
print(time)

# 2636 치즈 문제에서 더 발전된 문제 인듯
# 시간 체크를 visited[x][y] + 1말고 bfs를 돌때마다 1씩 추가 이런식으로도 할 수 있다는 것을 생각...
# >> 시간 체크를 visited[x][y] + 1 이런식으로 하기 힘든 이유가 중간에 시간이 0인 공기층 구간이 있을 수 있어서...
# 어려웠음....
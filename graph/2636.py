import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split()) # n, m은 최대 100
data = [[0 for _ in range(m+2)]]
for i in range(n):
    arr = [0]
    arr += list(map(int, input().split()))
    arr += [0]
    data.append(arr)
data.append([0 for _ in range(m+2)])


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(before):
    queue = deque(before) # before = 한시간전에 삭제된 치즈위치들(다음삭제될 위치와 가까워서)
    del_cheese = [] # 삭제될 치즈 위치
    visited = [[0 for _ in range(m+2)] for _ in range(n+2)]
    visited[before[0][0]][before[0][1]] = 1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n+2 and 0 <= ny < m+2 and visited[nx][ny] == 0:
                if data[nx][ny] == 1: # 치즈 가장 자리면 
                    del_cheese.append((nx, ny))
                    visited[nx][ny] = 1
                    # 주의) queue에 치즈 가장 자리 위치는 넣지 않음
                    
                elif data[nx][ny] == 0: # 치즈 없는 부분이면
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
    
    return del_cheese

before = [(0, 0)] # 초기 before 설정
answer_time = 0
last_cheese_num = 0

while True:
    del_cheese = bfs(before)
    answer_time += 1
    
    if del_cheese == []:
        break
    
    for x, y in del_cheese: # 가장 자리 치즈 제거
        data[x][y] = 0
    
    last_cheese_num = len(del_cheese)
    before = del_cheese

print(answer_time-1)
print(last_cheese_num)



# 100 x 100 x 50 = 50만

# 치즈의 가장 가장자리는 녹음(단 치즈들로 둘러싸인부분의 안쪽은 녹지 않음) >> 5547 일루미네이션 문제와 유사
# 치즈가 모두 녹아 없어지는데 걸리느 시간과, 모두 녹기 한 시간 전에 치즈조각이 놓여있는 칸의 개수
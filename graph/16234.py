import sys
input = sys.stdin.readline
from collections import deque


n, l, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    move_posi = [(x, y)]
    total = data[x][y]
    visited[x][y] = 1
        
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n and l <= abs(data[x][y]-data[nx][ny]) <= r and visited[nx][ny] == 0: # visited[nx][ny] == 0을 검사안하니까(visited) 검사했던곳 다시 queue에 담아서 무한반복걸림
                visited[nx][ny] = 1
                queue.append((nx, ny))
                total += data[nx][ny]
                move_posi.append((nx, ny))
                    
    
    if len(move_posi) == 1:
        return 0, []
    
    ppl = total // len(move_posi)
    return ppl, move_posi
    
    

answer = 0
while True:

    visited = [[0 for _ in range(n)] for _ in range(n)]        
    move_posis = []
    ppls = []
    check = 0
    
    for i in range(n):
        for j in range(n):
            ppl, move_posi = bfs(i, j, visited)
            check += ppl
            ppls.append(ppl)
            move_posis.append(move_posi)
    
    if check == 0: # 한번도 인구이동이 발생하지 않은경우
        break
    
    # 하루에 모든 국경선 열고, 인구이동을 해야하기 때문에 bfs함수 안에서 data의 값을 변경하면 안됨
    for i in range(len(move_posis)):
        for x, y in move_posis[i]:
            data[x][y] = ppls[i]
    
    answer += 1 

print(answer)


# 시간복잡도 : 250 * 2000 = 500000
# >> 각 좌표마다 4방향 검사한다해도 50만 x 4 = 200만

# 국경선 공유하는 두 나라 인구차이가 L <= x <= R 이면, 국경선 오늘하루 연다
# 인구 이동 : 국경선열려있는 인접한 칸만을 이용해 이동, 그 나라를 오늘 하루 동안은 연합이라고 함
# 연합을 이루는 각 칸의 인구수는 연합인구수/연합 칸 개수 (소수점 버림)
# 인구 이동이 며칠 동안 발생하는지 출력
import sys
input = sys.stdin.readline
from collections import deque

graph = [list(input().rstrip()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    color = graph[x][y]
    queue = deque([(x, y)])
    arr = []
    visited[x][y] = 1
    
    while queue:
        x, y= queue.popleft()
        arr.append((x, y))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and graph[nx][ny] == color:
                queue.append((nx, ny))
                visited[nx][ny] = 1
    
    # 터진 경우
    if len(arr) >= 4:
        # print(color, arr)
        for x, y in arr:
            graph[x][y] = '.'
            
        return 1

    # 터지지 않은 경우
    return 0

    

result = 0 
while True:
    visited = [[0] * 6 for _ in range(12)]
    check = 0
    
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                check += bfs(i, j) # 1개라도 터졌다면, check = 1, 아님 0

    if check == 0:
        break
    else:
        result += 1
        
    for j in range(6):
        idx = 11
        # 맨처음 내려오게 만들 위치를 찾기
        for i in range(11, -1, -1):
            if graph[i][j] != '.':
                idx -= 1
            else: # . 발견시 break해야함...
                break
        
        # 이미 아래에 깔려있는 건 제외하고 idx부터 위로 올라가면서 내릴 수 있는 건 내리기
        for i in range(idx, -1, -1):
            if graph[i][j] != '.':
                graph[idx][j] = graph[i][j]
                graph[i][j] = '.'
                idx -= 1
    
    # print("-"*12)
    # for g in graph:
    #     print(*g)
    # print("-"*12)

print(result)
# 뿌요 놓고 난 뒤, 같은 색 뿌요가 4개이상 상하좌우로 연결되어있으면 한꺼번에 사라짐
# 터질 수 있는 그룹이 여러개면 동시에 터지고, 여러그룹이 터지더라도 연쇄는 1 추가
# 상대방 필드 주어질때 연쇄가 몇번 연속으로 일어날지 계산
# 색상 R, G, B, P, Y
# 하나도 터지지 않으면 0 출력

# 이 두개 반복
# 1. 매초 마다 4개 이상 상하좌우로 연결되어있는지 확인
# 2. 빈자리 생기면 아래로 내리기


# 반례
'''
.....P
....GG
....GG
....GG
....GG
....GG
....GG
....GG
.Y..GG
.YG.GG
RRYGPP
RRYGGP
-------- 아래는 1초뒤의 결과 >> 맨위 p안내려옴
. . . . . P
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . . . . .
. . G . . .
. Y Y G P P
. Y Y G G P
'''

# 내려오게 만드는 걸 짜는게 어려웠던 문제
# 젤 처음에 만나는 문자부터 차례대로 내리면 된다고 생각했었음 -> 틀림, 중간에 빈공백이 있을 수 있었음.
# 와 케이스가 엄청 다양하군,, 어렵다..

# 다른 사람 정답 코드

def bfs(i, j, char):
    q = deque([(i, j)])
    chain.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < 12 and 0 <= ny < 6 and visit[nx][ny] == 0 and graph[nx][ny] == char:
                visit[nx][ny] = 1
                q.append((nx, ny))
                chain.append((nx, ny))
    
def down():
    for i in range(6):
        for j in range(12): # 맨 아래에서 각 행까지 검사해서
            for k in range(11, j, -1): 
                if graph[j][i] != '.' and graph[k][i] == '.': # 기준이되는 j번째 행에는 알파벳이 있고, j행보다 더 아래에 있는 k행은 . 이라면
                    graph[k][i] = graph[j][i] # k행에 j행의 알파벳 넣고,
                    graph[j][i] = '.' # j행에는 .으로 채우기
                    break # 기준이 되는 j번째행의 알파벳 옮기기 목적 달성이후에는 다시 기준이 되는 그 다음 위에 j행으로 변경하도록 break
    

graph = [list(input().rstrip()) for _ in range(12)]
result = 0
while True:
    isTrue = False
    visit = [[0]*6 for _ in range(12)]
    
    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visit[i][j] == 0:
                visit[i][j] = 1
                chain = []
                bfs(i, j, graph[i][j])
                if len(chain) > 3:
                    isTrue = True
                    for x, y in chain:
                        graph[x][y] = '.'
    
    if not isTrue: break # 하나도 터진게 없다면 break
    down()
    result += 1 # 어짜피 초당 여러개 터져도 1개만 추가함
    
print(result)
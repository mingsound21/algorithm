import sys
input = sys.stdin.readline


n = int(input())

# 지뢰 입력
graph = []
for _ in range(n):
    graph.append(list(input().rstrip()))
    
# 게임 결과 입력
game_result = []
for _ in range(n):
    game_result.append(list(input().rstrip()))

# 지뢰 개수 체크 힘수
def check_bomb(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == '*':
            cnt += 1
        
    return cnt

answer = [['.'] * n for _ in range(n)]
click_bomb = False
bomb_position = []

for i in range(n):
    for j in range(n):
        if game_result[i][j] == 'x':
            answer[i][j] = check_bomb(i, j)
            if graph[i][j] == '*':
                click_bomb = True
                
        if graph[i][j] == '*':
            bomb_position.append((i, j))

if click_bomb:
    for x, y in bomb_position:
        answer[x][y] = '*'

# 결과 출력
for i in range(n):
    for j in range(n):
        print(answer[i][j], end = "")
    print()



# 지뢰없으면서 열린 칸 : 0-8 주변 지뢰 개수
# 지뢰 있는 칸 열렸다면, 지뢰 있는 모든 칸 *로 표시
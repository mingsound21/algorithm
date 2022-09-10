import sys
input = sys.stdin.readline

r, c, n = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]

time = [[-1 for i in range(c)] for _ in range(r)] 
# -1 : 빈칸 의미
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'O':
            time[i][j] = 2
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최대 시간 복잡도 : 200 * 200 * 200 * 4 = 3200만 (시간 제한 2초니까 4000만까진 괜찮지 않을까?)
for t in range(2, n+1):
    
    if t % 2 == 0: # 폭탄 설치 - 이때는 폭탄 터지는 것 없음
        for i in range(r):
            for j in range(c):
                if time[i][j] == -1:
                    time[i][j] = 3
                else:
                    time[i][j] -= 1
    else: # 폭탄 터지는 때 
        for i in range(r):
            for j in range(c):
                if time[i][j] > 0: # 폭탄들 시간 1초 지남
                    time[i][j] -= 1
                    
        for i in range(r):
            for j in range(c):
                if time[i][j] == 0: # 폭발까지 남은 시간 0초면 -> 터짐
                    time[i][j] = -1 # 폭탄 제거
                    for idx in range(4):
                        nx = i + dx[idx]
                        ny = j + dy[idx]

                        if nx < 0 or nx >= r or ny < 0 or ny >= c:
                            continue
                            
                        # 이부분을 생각해내는게 어려웠음!!
                        if time[nx][ny] == 0: # 동시에 터지는 것은 연쇄반응되는 것에 포함 X
                            continue
                        
                        time[nx][ny] = -1 # 폭탄 제거

# 결과 출력
for i in range(r):
    for j in range(c):
        if time[i][j] == -1:
            print('.', end = "")
        else:
            print('O', end = "")
    print()
                    
# 폭탄 - 3초뒤 폭발, 폭발 이후에는 인접한 4칸도 함께 파괴되고, 빈칸으로 변함
# 인접한 4군데에 폭탄이 있는 경우 인접한 폭탄은 폭발없이 파괴됨 - 연쇄반응 X

# 0초 - 일부 칸에 폭탄 설치
# 1초 - 아무것도 안함
# 2초 - 폭탄 설치 안된 곳에 폭탄 설치
# 3초 - 초기에 설치 했던 폭탄 폭발
# 4초 - 폭탄 설치 안된 곳에 폭탄 설치
# 5초 - 2초에 설치했던 폭탄들 터짐
# 6초 - 폭탄 설치
# 7초 - 4초에 설치 했던 폭탄 폭발
# 8초 - 폭탄 설치

# 2초 간격으로 폭탄 설치

# >> 폭탄 터질 때까지 남은 시간을 기록해야겠는데?


# 다른 사람 풀이
r, c, n = map(int, input().split())
graph = [list(input().strip()) for i in range(r)]

if n <= 1: # 처음 ~ 1초뒤 >> 처음 상태 그대로
    for g in graph:
        print(''.join(g))
elif n % 2 == 0: # 짝수 초 지난 뒤 >> 모든 칸이 폭탄
    for i in range(r):
        print('O' * c)
else:
    # bombs1 : 초기 입력 기준 폭탄 터진뒤 모양
    bombs1 = [['O'] * c for i in range(r)]
    for x in range(r):
        for y in range(c):
            if graph[x][y] == 'O':
                bombs1[x][y] = '.'
            else:
                for i, j in [(0, 1),(0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x < r and 0 <= y < c and graph[x+i][y+i] == 'O':
                        bombs1[x][y] = '.'
                        break
    
    # bombs2 : bombs1 기준 폭탄 터진뒤 모양
    bombs2 = [['O'] * c for i in range(r)]
    for x in range(r):
        for y in range(c):
            if bombs1[x][y] == 'O':
                bombs2[x][y] = '.'
            else:
                for i, j in [(0, 1),(0, -1), (1, 0), (-1, 0)]:
                    if 0 <= x < r and 0 <= y < c and bombs1[x+i][y+i] == 'O':
                        bombs2[x][y] = '.'
                        break
    
    if n % 4 == 3: # 3, 7, 11 ... 초가 지난뒤에는 bombs1
        for li in bombs1:
            print(''.join(li))
            
    if n % 4 == 1: # 5, 9, 13 ... 초가 지난뒤에는 bombs1
        for li in bombs2:
            print(''.join(li))
            
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())

data = [list(input().rsplit())for _ in range(n)]
pre_o = []
teacher = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 'X': # 장애물이 들어갈 수 있는 위치 저장
            pre_o.append((i, j))
        elif data[i][j] == 'T': # 선생님 위치 저장
            teacher.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for li in list(combinations(pre_o, 3)): # 모든 장애물이 들어갈 수 있는 조합에 대해서
    check = 0 # yes/no 여부
        
    for x, y in li: # 장애물로 3군데 변경
        data[x][y] = 'O'
    
    for X, Y in teacher: # 모든 선생님들 마다
        x = X
        y = Y
        idx = 0
        # 상하좌우방향으로 검사
        while True:
            if idx == 4:
                break
            
            x = x + dx[idx]
            y = y + dy[idx]
            
            if x < 0 or x >= n or y < 0 or y >= n: # 아무것도 발견하지 않고, 끝에 도달한 경우
                idx += 1 # 다음 방향 검사
                x = X
                y = Y
                continue
            
            if data[x][y] == 'O': # 장애물 발견시
                idx += 1 # 다음 방향 검사
                x = X
                y = Y
                continue
            
            if data[x][y] == 'S': # 학생 발견시
                check = 1 # no 여부 저장
                break
            
        if check == 1: # no 나왔으면 다음 장애물 3군데 검사
            break
    
    if check == 0: # 만약 yes면 출력후 종료
        print('YES')
        exit(0)
        
    for x, y in li: # 다시 장애물 원래대로 복구
        data[x][y] = 'X'

print('NO')

# 선생님 T, 학생 S, 장애물 O
# 선생님은 상하좌우 방향으로 감시
# 장애물 뒤편에 숨어있는 학생은 볼 수 없음

# 3개의 장애물 설치해서 모든 학생들을 감시로부터 피할 수 있도록

# 최대 : 34C3 * 5 * 12(선생님기준 가로세로 검사해서 학생발견하는지) = 5984 * 60

# 다른 사람 풀이
n = int(input())
graph = []
teacher = 0
for _ in range(n):
    data = list(input().strip())
    teacher += data.count('T')
    graph.append(data)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 선생님의 위치 x, y로 부터 상하좌우 일직선방향을 검사해 학생 감시 가능한지 검사
def check_S(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True # 학생 감시 가능하면 True 반환
            else:
                nx += dx[i]
                ny += dy[i]
    return False

# 벽을 설치할 수 있는 모든 경우의 수 찾는 함수 - 재귀 방식
def solution(count):
    global answer
    
    if count == 3: # 재귀함수 실행했을때 아직 장애물 3개 채웠으면
        cnt = 0 # 학생 감시 불가하다고 판단한 선생님 수
        
        # 모든 graph를 돌면서
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T': # 선생님이 있는 곳이면
                    if not check_S(i, j): # 학생 감시 불가능하면 False반환
                        cnt += 1 
        
        if cnt == teacher: 
            answer = True
        return
    
    # 모든 graph를 검사하면서
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X': # X인위치 O로 변경하고 count +=1 한뒤, solution 재귀함수 실행
                graph[i][j] == 'O'
                count += 1
                solution(count)
                graph[i][j] = 'X' # 다시 복구
                count -= 1  # 다시 복구

answer = False
solution(0)
if answer:
    print('YES')
else:
    print('NO')

# 14502 연구소 문제와 유사함
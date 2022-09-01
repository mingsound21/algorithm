import sys
input = sys.stdin.readline
import itertools
import copy

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
turn_num = [i for i in range(k)]
turn_nums = list(itertools.permutations(turn_num))
turn = [list(map(int, input().split())) for _ in range(k)]

        
def turnRight(r, c, s, data):
    x1, y1 = r-s-1, c-s-1
    x2, y2 = r+s-1, c+s-1
    
    col = y2 - y1 + 1
    row = x2 - x1 + 1
    
    for i in range(min(col, row) // 2):
        x, y = x1 + i, y1 + i
        
        temp = data[x][y]
        
        # 좌
        for j in range(x, x2-i):
            data[j][y] = data[j+1][y]
        
        # 아래
        for j in range(y, y2-i):
            data[x2-i][j]= data[x2-i][j+1]
        
        # 오른쪽
        for j in range(x2-i, x, -1):
            data[j][y2-i] = data[j-1][y2-i]
        
        # 위
        for j in range(y2-i, y+1, -1):
            data[x][j] = data[x][j-1]

        data[x][y+1] = temp

    
answer = []
for T in turn_nums:
    data = copy.deepcopy(A)
    for t in T:
        r, c, s = turn[t][0], turn[t][1], turn[t][2]
        turnRight(r, c, s, data)
    result = 100*100
    for d in data:
        result = min(result, sum(d))
    answer.append(result)

print(min(answer))
        
# 문제
# 각행의 합 중에서 가장 작은 것을 출력
# 시계방향 회전, 순서는 맘대로 -> 모든 경우의 수 다 따져봐야함 (최대 k가 6, >> 6!*(50*50) = 30만)

# 풀긴했는데,, 배열돌리는게 그냥 생각나는대로 쓴 느낌,,,

# 다른 사람 풀이
from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]

ans = 987654321 # 최솟값을 구하기 위해 처음에 큰 수로 초기화

# 1. 회전 순서 정하기(최대 6! = 720)
for p in permutations(rcs, K):
    # 2. 회전
    copy_a = deepcopy(a)
    for r, c, s in p:
        r -= 1
        c -= 1
        
        for n in range(s, 0, -1):
            tmp = copy_a[r-n][c+n] # 우 상단
            copy_a[r-n][c-n+1:c+n+1] = copy_a[r-n][c-n:c+n] # 위
            # 좌
            for row in range(r-n, r+n):
                copy_a[row][c-n] = copy_a[row+1][c-n]
                
            copy_a[r+n][c-n:c+n] = copy_a[r+n][c-n+1:c+n+1] # 아래
            
            # 오른쪽
            for row in range(r+n, r-n, -1):
                copy_a[row][c+n] = copy_a[row-1][c+n]
            
            copy_a[r-n+1][c+n] = tmp # 우상단, 한칸 아래
                
    # 3. 각 행의 최소값 찾기       
    for row in copy_a:
        ans = min(ans, sum(row))

print(ans)            


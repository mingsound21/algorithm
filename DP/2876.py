import sys
input = sys.stdin.readline

n = int(input())
st = [list(map(int, input().split())) for _ in range(n)]
_max = [0] * 6
dp = [0] * 6

for i in range(n):
    for j in range(2):
        if j == 1 and st[i][1] == st[i][0]: # 문제 주어진 상황상 한 행에 한 사람만 택한다는 조건
            break
        dp[st[i][j]] += 1
        _max[st[i][j]] = max(_max[st[i][j]], dp[st[i][j]])
        
    for j in range(1, 6):
        if j not in st[i]:
            dp[j] = 0

M = max(_max)     
print(M ,_max.index(M))

# 같은 숫자가 연속한 행에 포함된 최대 행 수, 여러개라면 점수가 작은 것
# 문제 이해가 어려웠음...
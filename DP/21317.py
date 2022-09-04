from copy import deepcopy
import sys
input = sys.stdin.readline

n = int(input())
small_jump = [0]
large_jump = [0]
for i in range(n-1):
    a, b = map(int, input().split())
    small_jump.append(a)
    large_jump.append(b)
k = int(input()) # 매우 큰 점프 에너지 (딱 1번 가능)

use_XXL = 0
dp = [0] * (n+1)
if n == 1:
    print(0)
    exit(0)

dp[2] = dp[1] + small_jump[1]
if n == 2:
    print(dp[2])
    exit(0)

for i in range(3, n+1):
    dp[i] = min(dp[i-1] + small_jump[i-1], dp[i-2] + large_jump[i-2])

# 매우 큰 점프 딱 1번 사용가능 >> n 20이니까, 매우 큰 점프 사용하는 모든 경우를 따져보기
answer = dp[n]
for i in range(4, n+1):
    copy_dp = deepcopy(dp)
    
    if copy_dp[i-3] + k < copy_dp[i]:
        copy_dp[i] = copy_dp[i-3] + k
        
    for j in range(i+1, n+1):
        copy_dp[j] = min(copy_dp[j-1] + small_jump[j-1], copy_dp[j-2] + large_jump[j-2])
    answer = min(answer, copy_dp[n])
    
print(answer)

# 작은 점프 : 다음 돌로 이동
# 큰 점프 : 1개 돌 건너뛰고 다음돌로
# 매우 큰 점프 : 2개 돌 건너뛰고 다음돌로

# 최소 에너지 출력
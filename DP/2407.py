import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dp = [0] * 101

dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] * i

print(dp[n]//(dp[m]*dp[n-m]))


# 다른 사람 풀이
# 1. math 모듈의 factorial 함수 사용
import math
n, m = map(int, input().split())
up = math.factorial(n)
down = math.factorial(m) * math.factorial(n - m)
print(up // down)
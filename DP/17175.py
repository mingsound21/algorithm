import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 51
dp[0] = dp[1] = 1

for i in range(2, n+1):
    dp[i] = (dp[i-1] + dp[i-2] + 1) % 1000000007

print(dp[n])

# 피보나치 함수가 호출되는 횟수
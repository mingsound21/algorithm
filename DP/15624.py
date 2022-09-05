import sys
input = sys.stdin.readline

n = int(input())

if n == 0:
    print(0)
    exit(0)
    
dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1] % 1000000007 + dp[i-2] % 1000000007

print(dp[n] % 1000000007)

# n번째 피보나치 수 출력
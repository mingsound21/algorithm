import sys
input = sys.stdin.readline

n = int(input())
dp = [10**5] * (n+1)
dp[0] = 0
coin = [1, 2, 5, 7]

for i in range(1, n+1):
    for j in coin:
        if i-j < 0:
            continue
        dp[i] = min(dp[i-j]+1, dp[i])    

print(dp[n])

# 동전의 개수가 최소가 되도록 지불, 동전 종류 (1, 2, 5, 7)
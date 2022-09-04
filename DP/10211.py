import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = data[0]
    for i in range(1, n):
        dp[i] = max(data[i], dp[i-1] + data[i])

    print(max(dp))
    
# 연속한 일부분의 합 중에서 가장 큰 값
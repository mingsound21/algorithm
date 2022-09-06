import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
dp = []
dp.append(1)

for i in range(1, n):
    d = []
    for j in range(i): # n=1000, 1000 * 1001 /2 = 50만
        if data[i] > data[j]:
            d.append(dp[j] + 1)

    if not d:
        dp.append(1)
    else:
        dp.append(max(d))

print(max(dp))
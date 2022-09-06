import sys
input = sys.stdin.readline

n = int(input())
jump = list(map(int, input().split()))
dp = [10**5] * (n)
dp[0] = 0

for i in range(n): # 100 * 1000 = 10만
    for j in range(i+1, i+1+jump[i]):
        if j >= n:
            continue
        dp[j] = min(dp[j], dp[i] + 1)

if dp[n-1] == 10**5:
    print(-1)
else:
    print(dp[n-1])

# 최소 몇번 점프해서 오른쪽 끝 도착하는지
# 도착 못하는 경우 -1 출력
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
coin = set(sorted([int(input()) for _ in range(n)]))
dp = [-1] * (k+1)
dp[0] = 0


for c in coin:
    for j in range(c, k+1):
        if dp[j-c] == -1:
            continue
        if dp[j] == -1:
            dp[j] = dp[j-c] + 1
        else:
            dp[j] = min(dp[j-c] + 1, dp[j])

print(dp[k])


# 이런식으로 어느때든지 min을 사용하기 위해서 처음에 1e9로 dp를 채우고
# 마지막에 불가능한 경우에는 1e9인지 체크해서 -1 출력하도록 할수도 있음
'''
dp = [1e9]*(k+1)
dp[0] = 0

for c in coin:
    for j in range(c, k+1):
        dp[j] = min(dp[j-c] + 1, dp[j])

if dp[k] == 1e9:
    print(-1)
else:
    print(dp[k])
'''


# 2293번 문제에서는 dp에 coin으로 만들 수 있는 방법의 수를 저장했다면,
# 2294에서는 dp에 사용한 coin의 최소 개수를 저장
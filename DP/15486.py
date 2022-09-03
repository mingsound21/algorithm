import sys
input = sys.stdin.readline

# 주석 - 틀린 풀이
n = int(input()) # 1,500,000
day = [0]
money = [0]
dp = [0] * (n+2)

for i in range(n):
    d, m = map(int, input().split())
    day.append(d)
    money.append(m)
    
_max = 0
for i in range(1, n+1):
    _max = max(_max, dp[i])
    finish_date = i + day[i]
    if finish_date > n+1:
        continue
    # dp[finish_date] = max(dp[finish_date], dp[i] + money[i], dp[i-1] + money[i])
    dp[finish_date] = max(dp[finish_date], _max + money[i])
    # _max = max(_max, dp[i])

print(max(dp))

# 퇴사 이후에는 상담 X
# 한개의 상담이 끝나기전에 다른 상담 X

n = int(input())
t, p = [], []
dp = [0] * (n + 1)

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
    
M = 0
for i in range(n):
    M = max(M, dp[i]) # 현재까지의 최대 pay
    finish_date = i + t[i]
    if finish_date > n: # 상담 종료날이 퇴사날 보다 늦으면 continue
        continue
    
    dp[finish_date] = max(M + p[i], dp[finish_date])
    
print(max(dp))
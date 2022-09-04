import sys
input = sys.stdin.readline

n = int(input())
time = []
pay = []
for i in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)
    
dp = [0] * (n+1) # n번째 날까지 일했을때의 얻을 수 있는 수익이 n+1번째 날에 기록되기 때문
_max = 0
for i in range(n):
    _max = max(_max, dp[i]) # i번째까지 얻을 수 있는 최대 수익
    
    finish_date = i + time[i]
    if finish_date > n:
        continue
    
    dp[finish_date] = max(_max + pay[i], dp[finish_date])

print(max(dp)) # finish_date가 n이상이면 그냥 0인채로 기록되어있을 수 있어서

# dp[i] : i번째 까지 얻을 수 있는 최대 수익
# 얻을 수 있는 최대 수익
# 퇴사2 문제와 차이점 : N의 입력 범위
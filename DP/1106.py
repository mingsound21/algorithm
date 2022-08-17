# 다른 사람 풀이
import sys
input = sys.stdin.readline

INF = 1e9

c, n = map(int, input().split())
data = []

min_cost = [INF] * (c + 100)
min_cost[0] = 0

for _ in range(n):
    # cost, customer num
    data.append(list(map(int, input().split())))

# cost 작은 순으로 정리
data_sort = sorted(data, key = lambda x : x[0])

for cost, cus in data_sort: # 최대 20번
    for i in range(cus, c + 100): # c + 100인 이유 : 딱 c명이 아닌, c명 이상이어도 ok라서. 그리고 손님수 최대 100명이라서.
        min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])
        
print(min(min_cost[c:]))

# 내 풀이
# 계속 index error나서 봤더니, c는 최대 1000이라서 dp 크기를 200이 아닌, 1101로 잡아야했다.
# 난 채울 수 있는 인원 수는 100이 최대라서 201로 했었음....
import sys
input = sys.stdin.readline

INF = 1e9

c, n = map(int, input().split())
ppls = []
dp = [INF] * 1101

for i in range(n):
    cost, ppl = map(int, input().split())
    ppls.append(ppl)
    dp[ppl] = min(cost, dp[ppl])


for i in range(1, c + max(ppls) + 1):
    for ppl in ppls:
        if i - ppl < 1 :
            continue
        dp[i] = min(dp[i], dp[ppl] + dp[i-ppl])

print(min(dp[c:]))

# 호텔의 고객을 적어도 c명 늘리기 위해 투자해야하는 최소 값
# 현재 인원 수 - [ppl]
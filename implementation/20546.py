import sys
input = sys.stdin.readline

J_money = S_money  = int(input())
stock = list(map(int, input().split()))

# 준현
J_stock_cnt = 0

for s in stock:
    if J_money == 0: # 사기만 하니까 돈이 없으면 끝!
        break
    
    if J_money >= s: # 살 수 있다면
        J_stock_cnt += J_money // s
        J_money %= s

J_total = J_money + J_stock_cnt * stock[-1]

# 성민
S_stock_cnt = 0
s_stock_graph = [0] * 14 # 1 : 매수, -1 : 매도
up = down = 1
for i in range (1, 13):
    if stock[i] > stock[i-1]:
        up += 1
    else:
        up = 1
        
    if stock[i] < stock[i-1]:
        down += 1
    else:
        down = 1
    
    if up >= 3:
        s_stock_graph[i+1] = -1
    if down >= 3:
        s_stock_graph[i+1] = 1


for i in range(2, 14):
    if s_stock_graph[i] == 1: # 매수
        S_stock_cnt += (S_money // stock[i])
        S_money %= stock[i]
    elif s_stock_graph[i] == -1: # 매도
        S_money += S_stock_cnt * stock[i]
        S_stock_cnt = 0

S_total = S_money + S_stock_cnt * stock[-1]

# 결과 출력
if J_total > S_total:
    print("BNP")
elif J_total < S_total:
    print("TIMING")
else:
    print("SAMESAME")


# < 문제 >
# 준현
# 주식 살 수 있다면 가능한 만큼 즉시 매수
# 산 주식은 절대 팔지 않음

# 성민
# 전량 매수, 전량 매도
# 3일 연속 가격이 전일 대비 상승하는 주식은 다음날 무조건 가격 하락 -> 전량 매도
# 3일 연속 가격이 전일 대비 하락하면 다음날 무조건 상슴 -> 전량 매수
# >> 단, 전일과 오늘의 주가가 동일하다면 가격이 상승, 하락한 것이 아님

# 자산 : 현금 + 14일 주가 x 주식수
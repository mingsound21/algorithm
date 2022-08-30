import sys
input = sys.stdin.readline

# n, q = map(int, input().split())
# scores = list(map(int, input().split()))
# fake = list(map(int, input().split()))

# for f in fake:
#     scores[f-1] = -scores[f-1]
    
#     total = 0
#     for i in range(n):
#         sum = 1
#         for j in range(4):
#             sum *= scores[(i+j)%n]
#         total += sum
#     print(total)
# 20만 x 20만 x 4 = 1600억 이구나

# 다른 사람 풀이 (dp 사용)

n, q = map(int, input().split())
a = list(map(int, input().split()))
dp = [0]*n

for i in range(n):
    dp[i] = a[i%n] * a[(i+1)%n] * a[(i+2)%n] * a[(i+3)%n]
    
fake = list(map(int, input().split()))

ex_sum = sum(dp)
for idx in fake:
    for i in range(4):
        new_idx = (idx-1-i+n)%n
        dp[new_idx] = -dp[new_idx]
        ex_sum += 2*dp[new_idx]
        
    print(ex_sum)
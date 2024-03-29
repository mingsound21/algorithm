import sys
input = sys.stdin.readline

n = int(input())

if n % 2 == 0:
    print("CY")
else:
    print("SK")
    
# dp
dp = [-1] * 1001
dp[1] = 1
dp[2] = 0
dp[3] = 1
for i in range(4, n + 1):
    if dp[i-1] or dp[i-3]: # 1개 또는 3개를 주울 수 있으니까
        dp[i] = 0
    else:
        dp[i] = 1
print('CY' if dp[n] == 0 else 'SK')
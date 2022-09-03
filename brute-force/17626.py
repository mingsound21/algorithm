import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    min_value = 1e9
    j = 1
    
    while (j ** 2) <= i:
        min_value = min(min_value, dp[i-(j**2)])
        j += 1
    
    dp.append(min_value + 1)
    
print(dp[n])

# 자신의 수보다 작은 수의 제곱수를 뺀 것의 최소를 구하고, 최솟값에 +1을 해주면 됨(제곱수의 것)
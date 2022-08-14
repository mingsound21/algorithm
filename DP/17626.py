import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n + 1):
    min_value = 1e9
    j = 1
    
    while (j**2) <= i: # 자신의 수보다 작은 제곱수들을 모두 검사
        min_value = min(min_value, dp[i - (j**2)])
        j += 1
    dp.append(min_value + 1)
    
print(dp[n])




# 자연수를 4개 이하의 제곱수의 합으로 나타내라
# n을 최소 개수의 제곱수 합으로 표현하는 컴퓨터 프로그램

import sys
input = sys.stdin.readline


n = int(input())
data = list(map(int, input().split()))
dp = [0] * n
dp[0] = 1
check = 0
same = 1

for i in range(1, n):
    if data[i-1] == data[i]:
        dp[i] = dp[i-1] + 1
        same += 1
    elif data[i-1] < data[i]: # 증가
        if check == -1: # 감소
            dp[i] = same + 1
            check = 1
        elif check == 0: # 미정
            check = 1
            dp[i] = dp[i-1] + 1
        else: # 증가
            dp[i] = dp[i-1] + 1
        same = 1
        
    elif data[i-1] > data[i]: # 감소
        
        if check == -1: # 감소
            dp[i] = dp[i-1] + 1
        elif check == 0: # 미정
            check = -1
            dp[i] = dp[i-1] + 1
        else: # 증가
            dp[i] = same + 1
            check = -1
        same = 1

print(max(dp))
        

# 연속해서 커지거나, 연속해서 작아지는 수열중 가장 긴 길이 출력

# 다른 사람 풀이

n = int(input())
data = list(map(int, input().split()))

dp1, dp2 = [1] * n, [1] * n
# dp1 : 상승 수열 개수
# dp2 : 하강 수열 개수

for i in range(1, n):
    if data[i] <= data[i-1]:
        dp1[i] = dp1[i-1] + 1
    if data[i] >= data[i-1]:
        dp2[i] = dp2[i-1] + 1

print(max(max(dp1), max(dp2)))
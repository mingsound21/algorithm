import sys
input = sys.stdin.readline

arr = [1] * 31

for i in range(2, 31):
    arr[i] = i * arr[i-1]

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(arr[b]//(arr[a]*arr[b-a]))
    


# 조합
# nCr = n!/(r! x (n-r)!)

# dp로 푸는 법
dp = [[1] * 31 for _ in range(31)]

for i in range(31):
    dp[1][i] = i
    
for i in range(2, 31): # i = 강 왼쪽 사이트
    for j in range(i+1, 31): # j = 강 오른쪽 사이트
        dp[i][j] = dp[i][j-1] + dp[i-1][j-1] # 이런 규칙이 있음 
        
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(dp[n][m])
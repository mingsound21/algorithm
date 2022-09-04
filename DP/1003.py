import sys
input = sys.stdin.readline

t = int(input())
dp0 = [0] * 41
dp1 = [0] * 41

dp0[0] = dp1[1] = 1

for i in range(2, 41):
    dp0[i] = dp0[i-1] + dp0[i-2]
    dp1[i] = dp1[i-1] + dp1[i-2]

for i in range(t):
    n = int(input())
    print(dp0[n], dp1[n])    
    
    
# 1초에 2000만 >> 0.25초 500만
# 0출력 횟수와 1출력 횟수

import sys
input = sys.stdin.readline

t = int(input())
dp = [[0 for _ in range(3)] for i in range(100001)]

# dp[i] = [끝나는 숫자 1인 경우, 끝나는 숫자 2인 경우, 끝나는 숫자 3인 경우]
dp[1] = [1, 0, 0]
dp[2] = [0, 1, 0]
dp[3] = [1, 1, 1]

for i in range(4, 100001):
    # 이 for문 내부에서도 % 1000000009 계산을 해줘야 시간 초과 안남
    # 파이썬에선 정수 길이의 제한이 없음 >> 단순 덧셈이라도 값이 커질수록 연산에 걸리는 시간 증가  
    dp[i][0] = dp[i-1][1]% 1000000009 + dp[i-1][2]% 1000000009
    dp[i][1] = dp[i-2][0]% 1000000009 + dp[i-2][2]% 1000000009
    dp[i][2] = dp[i-3][0]% 1000000009 + dp[i-3][1]% 1000000009
    
for i in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)

# n을 1, 2, 3의 합으로 나타내는 방법의 수
# 같은 수를 2번 이상 연속으로 사용하면 안됨

# n == 6인 상황에서
# dp[6][0] = dp[5][1] + dp[5][2]  # >> 5 + 1 = 6 >> 마지막에 1을 더해주기 위해서 그 이전 수는 2 또는 3인 경우여야함
# dp[6][1] = dp[4][0] + dp[4][2]  # >> 4 + 2 = 6 >> 마지막에 2을 더해주기 위해서 그 이전 수는 1 또는 3인 경우여야함
# dp[6][2] = dp[3][0] + dp[3][1]  # >> 3 + 3 = 6 >> 마지막에 3을 더해주기 위해서 그 이전 수는 1 또는 2인 경우여야함

# arr = [[0]*n]*m  #>> 모든 arr[i]들이 같은 객체를 가리키고 있음 
# arr2 = [[0 for _ in range(n)] for i in range(m)] # arr2[i]들은 서로 다른 객체

# 같은 수를 연속해서 더할수없다 >> 끝에오는 숫자별로 개수를 저장하자
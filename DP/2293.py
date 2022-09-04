import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for i in coin: # 코인을 돌면서
    for j in range(i, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i] # dp[j-i] : i원짜리 동전을 1개 사용해서 j-i의 합을 만들 수 있는 경우의 수
            
print(dp[k])

# 동적 계획법
# 1. "전체의 문제"를 "부분 문제"로 잘 나눴는가? 그렇다면 부분문제의 점화식은 무엇인가?
# 2. 부분 문제들을 해결하면 얻는 결과값을 메모이제이션하는가?
# 3. 부분 문제의 점화식은 부분 문제들 사이의 "관계"를 빠짐없이 고려하는가?


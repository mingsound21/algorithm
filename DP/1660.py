import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 1]
total = [0, 1]


for i in range(2, 300001):
    dp.append(dp[i-1] + i)
    total.append(total[i-1] + dp[i])
    if total[i] > n:
        last_idx = i-1
        dp.pop()
        total.pop()
        break
    elif total[i] == n:
        last_idx = i
        break

answer = [10**6] * (n+1)
answer[0] = 0
for i in range(1, last_idx+1):
    answer[total[i]] = 1
    
for i in range(2, n+1):
    for j in range(1, last_idx+1):
        if i - total[j] < 0 :
            break
        answer[i] = min(answer[i-total[j]] + answer[total[j]], answer[i])

print(answer[n])

# 만들 수 있는 사면체의 최소 개수

# 다른 사람 풀이 -- 거의 같음
n = int(input())
nums = [] # 나의 total과 같은 것
num = 0
idx = 1
while num < n:
    num += (idx * (idx + 1)) // 2
    nums.append(num)
    idx += 1

dp = [float('inf')] * (n+1) # float('inf'), float('-inf') -> 최소, 최대 구할때 무한수 적용시 이런식으로도 가능(단, int형에는 적용 불가)
for i in range(1, n+1):
    for num in nums:
        if num == i:
            dp[i] = 1
            break
        if num > i : break
        dp[i] = min(dp[i], 1 + dp[i-num])

print(dp[n])
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))

coin.sort(reverse=True)

answer = 0
for i in range(len(coin)):
    if(k // coin[i] == 0):
        continue
    
    answer += (k // coin[i])
    k %= coin[i]
    
    if(k==0):
        break
    
print(answer)
    
    

# 이 문제에선 Ai 가 Ai-1의 배수라고 했으니, 가장 큰 값 부터 "//" 계산하면 됨.
    
# 가장 작은 동전 개수로 거슬러 주기

# 1. 500, 100, 50 처럼 작은 값의 배수가 큰 값이라면, 
#   작은 동전들로 다른 값 만들 수 없음
# 예) 800 거슬러 줄때 (500 + 100 * 3) 밖에 방법 없음.

# 2. 500, 400, 100 처럼 작은 값의 배수가 큰 값이 될 수 없는 경우가 있다면, 
#   작은 동전들로 다른 값 만들 수 있음.
# 예) 800 거슬러 줄때, (500 + 100 * 3) 보다 (400 * 2)가 더 적은 개수
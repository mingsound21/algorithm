import sys
input = sys.stdin.readline

n = int(input())

money = 1000 - n

coin = [500, 100, 50, 10, 5, 1]

answer = 0
for c in coin:
    answer += money // c
    money %= c

    if(money == 0):
        break
    
print(answer)

# 작은 값의 배수가 큰 수라서 이렇게 풀 수 있음
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
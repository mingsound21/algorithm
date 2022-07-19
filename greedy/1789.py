import sys
input = sys.stdin.readline

s = int(input())

n = round((2 * s)**(1/2))

while True:
    sum = n * (n+1) / 2
    if(s >= sum):
        answer = n
        break
    n-=1

print(answer)

# 1~n까지의 합 공식 = n * (n+1) / 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

a, b = map(int, input().split())

cnt = 1
while b != a:
    cnt +=1 
    
    temp = b
    
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    
    if temp == b:
        print(-1)
        exit(0)
print(cnt)

# 다른 사람 풀이
# a로 b를 만드는게 아니라, b로 a를 만든다

# >> 연산 속도 상 우위는 2를 나누는게 아니라 수의 끝의 1을 없애기
# >> 1. b의 끝에 1이 존재하면 1을 지운다
# >> 2. 그렇지 않다면 2로 나눈다(단, 짝수인 경우에만)


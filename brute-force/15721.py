import sys
input = sys.stdin.readline

a = int(input())
t = int(input())
w = int(input())

turn = 2
default_w = [0, 1, 0, 1]
cnt = 0
num = 0
while True:
    for d in default_w:
        if w == d:
            cnt += 1
        if cnt == t:
            print(num%a)
            exit(0)
        num += 1
        
    for i in range(turn):
        if w == 0:
            cnt += 1
        if cnt == t:
            print(num%a)
            exit(0)
        num += 1
    
    for i in range(turn):
        if w == 1:
            cnt += 1
        if cnt == t:
            print(num%a)
            exit(0)
        num += 1
    turn += 1
# 반시계방향, t번째 w를 외치는 사람의 번호를 출력
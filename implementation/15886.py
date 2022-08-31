import sys
input = sys.stdin.readline

n = int(input())
data = list(input().rstrip())

cnt = 0
for i in range(n-1):
    if data[i] == 'E' and data[i+1] == 'W':
        cnt += 1

print(cnt)

# E : 오른쪽 이동, W : 왼쪽 이동
# 최소 몇개의 칸에 선물을 놓으면, 구사과가 항상 선물을 가져가는지

# EW : 이 두개의 칸만을 계속 이동 -> 이 EW의 개수만큼 선물을 놓으면 됨
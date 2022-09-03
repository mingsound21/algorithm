import sys
input = sys.stdin.readline
from itertools import product


n, k = map(int, input().split())
data = list(map(str, input().split()))
data.sort()

save = 0
for i in range(1, 10): # 10까지 해야 100,000,000 1 의 입력이 들어와도 출력 나옴
    for d in list(product(data, repeat = i)):
        num = int("".join(d))
            
        if num > n:
            print(save)
            exit(0)
            
        save = num
# n보다 작거나 같은 자연수 중에서 data안에 있는 수들로만 구성된 것

# 3 ** 8 = 6561
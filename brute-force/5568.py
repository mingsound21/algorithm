import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input()) # n개의 카드 중
k = int(input()) # k개를 선택
card = [int(input()) for _ in range(n)]
result = []

for c in list(permutations(card, k)): #최대 960 (10 x 4 x 24 = 960)
    num = ""
    for i in range(k): # 최대 4
        num += str(c[i])
    if num not in result: # 최대 960
        result.append(num)

print(len(result))

# 최대 시간 복잡도 : 921,600  >> 브루트 포스
# n개의 카드 중 k개를 선택해서 만들 수 있는 정수의 개수
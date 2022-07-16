import copy
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

bCopy = b[:]
bCopy.sort()
bRank = []
for i in range(N):
    idx = bCopy.index(b[i])
    bRank.append(idx)
    if(idx!=N-1 and bCopy[idx] == bCopy[idx+1]):
        bCopy[idx] = -1
# list.index는 별도의 설정 없으면 찾고자하는 값이 가장 처음 나타나는 인덱스 값만 반환

a.sort(reverse=True)

print(bRank)

answer = 0
for i in range(N):
    answer += a[bRank[i]] * b[i]
    
print(answer)

# 내가 틀린 반례
# 5
# 1 2 3 4 5
# 3 3 3 3 0

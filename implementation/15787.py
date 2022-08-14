from collections import deque
import sys
input = sys.stdin.readline

# 1. deque를 사용한 풀이
# n, m = map(int, input().split())
# train = [deque([0]*21) for _ in range(n+1)]

# for _ in range(m):
#     op = list(map(int, input().split()))
#     if op[0] == 1:
#         train[op[1]][op[2]] = 1
#     elif op[0] == 2:
#         train[op[1]][op[2]] = 0
#     elif op[0] == 3:
#         train[op[1]].rotate(1)
#         train[op[1]][1] = 0
#     else:
#         train[op[1]].rotate(-1)
#         train[op[1]][20] = 0
        
# answer = []
# for t in train:
#     if t not in answer:
#         answer.append(t)

# print(len(answer))

#>> deque.rotate(num) : 데크를 num만큼 회전(양수면 오른쪽, 음수면 왼쪽)

# 2. set을 사용한 풀이
n, m = map(int, input().split())
train = [set([]) for _ in range(n+1)]

for _ in range(m):
    op = list(map(int, input().split()))
    if op[0] == 1:
        train[op[1]].add(op[2]) # 자리 숫자를 add
    elif op[0] == 2:
        train[op[1]].discard(op[2])
    elif op[0] == 3:
        tr = list(train[op[1]])
        temp = set()
        for t in tr:
            if t + 1 > 20 :
                continue
            temp.add(t + 1)
        train[op[1]] = temp
    else:
        tr = list(train[op[1]])
        temp = set()
        for t in tr:
            if t -1 < 1 :
                continue
            temp.add(t - 1)
        train[op[1]] = temp

answer = set()
for t in train:
    t = tuple(sorted(t)) # sorted로 동일하게 바꿔서 비교 가능하도록, set 안에는 변경불가능한 값만 포함가능 -> tuple 사용 이유
    answer.add(t)
print(len(answer))

# set.discard(num) : num이 set안에 없어도 에러 X
# set.remove(num) : num이 set안에 없으면 에러 O
# set.add(num)
# set.update([array])

# set.union(setA, setB) , setA | setB
# set.intersection(setA, setB) , setA & setB
# set.symmetric_difference(setA, setB), setA ^ setB
# set.difference(setA, setB), setA - setB



# <문제 이해>
# 문제에서 한칸 뒤로 이동 : 오른쪽으로 한칸 이동

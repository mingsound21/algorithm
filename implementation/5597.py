import sys
input = sys.stdin.readline

attend = [False] * 31

for _ in range(28):
    attend[int(input())] = True

for i in range(1, 31):
    if not attend[i]:
        print(i)
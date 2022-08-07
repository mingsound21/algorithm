import sys
input = sys.stdin.readline

n = int(input()) # 100이하 양의 정수
switch = list(map(int, input().split()))

student = [] # 남 1 여 2
for _ in range(int(input())):
    student.append(list(map(int, input().split())))

def swap(n):
    if switch[n] == 1:
        switch[n] = 0
    else:
        switch[n] = 1
        
for a, b in student:
    if a == 1: # 남자
        for i in range(b-1, n, b):
            swap(i)
    else: # 여자
        for i in range(1, n):
            idx1 = b-1 - i
            idx2 = b-1 + i
            if idx1 == -1 or idx2 == n:
                idx1 += 1
                idx2 -= 1
                break
            if switch[idx1] != switch[idx2]:
                idx1 += 1
                idx2 -= 1
                break
        
        if idx1 == idx2:
            swap(idx1)
        else:
            for i in range(idx1, idx2+1):
                swap(i)

for i in range(n):
    if i != 0 and i % 20 == 0:
        print()
    print(switch[i], end = " ")

# <문제>
# 남학생 : 스위치 번호가 받은 수의 배수이면 스위치 상태 바꿈
# 여학생 : 받은수와 같은 번호가 붙은 스위치를 중심으로 좌우 대칭이면서 가장 많은 스위치 포함하는 구간의 스위치 상태 모두 변경

import sys
input = sys.stdin.readline

inputTime = int(input())

time = [300, 60, 10]

result = []
for t in time:
    result.append(inputTime//t)
    inputTime %= t

if inputTime != 0 :
    print(-1)
else:
    for t in result:
        print(t, end = " ")
        
# 큰 수가 작은 수의 배수
# 딱 시간 맞춰야함 - 못 맞추는 경우 -1 출력
# 최소 버튼 클릭
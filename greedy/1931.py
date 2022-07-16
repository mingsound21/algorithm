from operator import itemgetter
import sys
input = sys.stdin.readline

n = int(input())
time = []
endTime = []
for i in range(n):
    start, end = map(int, input().split())
    newtime = [start, end]
    newtime.append(end - start)
    endTime.append(end)
    time.append(newtime)

timeLine = [1 for _ in range(max(endTime)+1)]

time = sorted(time, key = itemgetter(2, 0))

answer = 0
for i in range(len(time)):
    for j in range(time[i][0]+1, time[i][1]+1):
        if(timeLine[j]==1):
            timeLine[j]=0
            if(j == time[i][1]):
                answer += 1
        else:
            break
print(answer)

# 사용시간이 짧은 것을 선택할수록 많은 회의를 할 수 있다.
import sys
input = sys.stdin.readline

N = int(input())
time = list(map(int, input().split()))


time.sort()

answer = time[0]
semiSum = time[0]
for i in range(1, len(time)):
    semiSum += time[i]
    answer += semiSum
    
print(answer)
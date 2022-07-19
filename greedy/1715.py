from collections import deque
import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()
arr = deque(arr)
answer = 0
while True:
    newArr = deque([])
    sum = arr.popleft() + arr.popleft()
    answer += sum
    newArr.append(sum)
    
    while(arr):
        if len(arr) != 1:
            if newArr[0] < arr[1]:
                sum = arr.popleft() + newArr.popleft()
                answer += sum
                newArr.append(sum)
            else:
                sum = arr.popleft() + arr.popleft()
                answer += sum
                newArr.append(sum)
        else:
            sum = arr.popleft() + newArr.popleft()
            answer += sum
            newArr.append(sum)
    if(len(newArr) == 1):
        break
    arr = deque(list(newArr)[:])
    newArr = deque([])

print(answer)
# 최대한 작은 묶음끼리 먼저
# sort한뒤 더하면서 작은 묶음이 반드시 앞에 있다는 보장이 사라짐
# 20 40 41 42면 (20 + 40) + (41 + 42)
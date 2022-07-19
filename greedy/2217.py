import sys
input = sys.stdin.readline

n = int(input())

rope = []
for i in range(n):
    rope.append(int(input()))

rope.sort(reverse=True)

arr = []

for i in range(n):
    arr.append(rope[i]*(i+1))
    
print(max(arr))

import sys
input = sys.stdin.readline

data = [0] * 367

n = int(input())
maxd = 0
for i in range(n):
    s, e = map(int, input().split())
    maxd = max(maxd, e)
    for j in range(s, e + 1):
        data[j] += 1

answer = 0
w = 0
h = 0
for i in range(1, maxd+2):
    if data[i] == 0:
        if w == 0:
            continue
        
        answer += w * h
        w = 0
        h = 0
        continue
    
    w += 1
    h = max(h, data[i])

print(answer)

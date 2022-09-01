import sys
input = sys.stdin.readline

n, k = map(int, input().split())
cnt = 0

for s in range(n*60*60 + 59*60 + 59 + 1):
    hour = s//60//60
    min = (s - 3600*hour)// 60
    sec = s % 60
    
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
        
    if min < 10:
        min = '0' + str(min)
    else:
        min = str(min)
        
    if sec < 10:
        sec = '0' + str(sec)
    else:
        sec = str(sec)
        
    a = hour.find(str(k))
    b = min.find(str(k))
    c = sec.find(str(k))
    
    if (a + b + c) != -3:
        cnt += 1
        
print(cnt)

# 다른 사람 풀이
n, k = map(int, input().split())
cnt = 0
k = str(k)

for i in range(n+1):
    if i < 10:
        i = '0' + str(i)
    for j in range(60):
        if j < 10:
            j = '0' + str(j)
        for t in range(60):
            if t < 10:
                t = '0' + str(t)
            if k in str(i) + str(j) + str(t):
                cnt += 1
                
print(cnt)

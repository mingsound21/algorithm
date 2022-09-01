import sys
input = sys.stdin.readline
import math

data = list(map(int, input().split()))
a = data[:3]
b = data[3:]

# 첫번째 방정식의 x의 계수가 0인 경우
if a[0] == 0:
    y = a[2] // a[1]
    
    if (b[2] - b[1] * y) == 0:
        x = 0
    else:
        x = (b[2] - b[1] * y) // b[0]
# 두번째 방정식의 y의 계수가 0인 경우
elif b[0] == 0:
    y = b[2] // b[1]
    
    if (a[2] - a[1] * y) == 0:
        x = 0
    else:
        x = (a[2] - a[1] * y) // a[0]
else:
    lcm = math.lcm(a[0], b[0])
    A = lcm // a[0] # a[0] == 0인경우 zeroDivisionError 발생
    for i in range(3):
        a[i] = a[i] * A
        
    B = lcm // b[0]
    for i in range(3):
        b[i] = b[i] * B

    for i in range(3):
        a[i] = a[i] - b[i]

    if a[2] == 0:
        y = 0
    else: 
        y = a[2] // a[1]

    if (b[2] - b[1] * y) == 0:
        x = 0
    else:
        x = (b[2] - b[1] * y) // b[0]
        
print(x, y) 
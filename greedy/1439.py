import sys
input = sys.stdin.readline

str = input().rstrip()

zero = 0
one = 0

if str[0] == '0':
    zero += 1
else:
    one += 1

for i in range(1, len(str)):
    if(str[i-1] == '0' and str[i] == '1'):
        one += 1
    elif(str[i-1] == '1' and str[i] == '0'):
        zero += 1

print(min(zero, one))

# 0에서 1로 변경될때 one += 1
# 1에서 0으로 변경될때 zero += 1
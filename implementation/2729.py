import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = input().split()
    a = list(a)
    b = list(b)
    a.reverse()
    b.reverse()
    for i in range(len(a)-1, -1, -1):
        if a[i] != '0':
            break
        a.pop()
    for i in range(len(b)-1, -1, -1):
        if b[i] != '0':
            break
        b.pop()
    result = []
    lenA = len(a)
    lenB = len(b)
    prev = 0
    lenT = lenA if lenA > lenB else lenB # 삼항연산자
    for i in range(lenT):
        if i == lenB:
            for j in range(i, lenT):
                total = prev + int(a[j])
                if total == 2:
                    result.append('0')
                    prev = 1
                else:
                    result.append(str(total))
                    prev = 0
            break
        elif i == lenA:
            for j in range(i, lenT):
                total = prev + int(b[j])
                if total == 2:
                    result.append('0')
                    prev = 1
                else:
                    result.append(str(total))
                    prev = 0
            break
        
        total = prev + int(a[i]) + int(b[i])
        if total == 2:
            prev = 1
            result.append('0')
        elif total == 3:
            prev = 1
            result.append('1')
        else:
            prev = 0
            result.append(str(total))
    if prev == 1:
        result.append('1')
    result.reverse()
    if not result: # 비어있는 경우
        result = ['0']
    print("".join(result))
    
    
# 0000 0000
# 00100 0010 
# 이런 앞에 쓸데없는 0이 붙어있는 입력이 들어올줄 몰랐음

# 다른 사람 풀이
n = int(input())
for _ in range(n):
    a, b = input().split()
    a = int(a, 2) # 2진수 입력을 10진수로 변경
    b = int(b, 2)
    print(bin(a+b).replace("Ob", "")) # 앞에 붙어있는 Ob를 ""으로 변경
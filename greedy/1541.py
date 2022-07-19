import sys
input = sys.stdin.readline

str = input().rstrip()

arr = []
startIdx = 0
endIdx = 0
for i in range(len(str)):
    if(str[i] in ['+', '-']):
        arr.append(str[startIdx : i])
        arr.append(str[i : i+1])
        startIdx = i+1
arr.append(str[startIdx : len(str)])

def changeToInt(n):
    if(n not in ['+', '-']):
        n.lstrip('0')
        return int(n)
    return n

arr = list(map(changeToInt, arr))

result = arr[0]
semiResult = 0
for i in range(1, len(arr)):
    if(i == len(arr)-1):
        result -= semiResult
        
    if(arr[i] == '-'):
        if(semiResult == 0):
            semiResult = arr[i+1]
        else:
            result -= semiResult
            semiResult = arr[i+1]
    elif(arr[i] == '+'):
        if(semiResult != 0):
            semiResult += arr[i+1]
        else:
            result += arr[i+1]
print(result)
# - (@ + @)
# - 뒤에 + 인 것들을 ()로 묶는다


# < 문자열 이어 붙이기 >
# 1.
# def insert_str(string, str_to_insert, index):
#   return string[:index] + str_to_insert + string[index:]

# 2.
# str = 'ABCDEFG'
# strList = list(str)
# strList.insert(4, '-') # 4번째 인덱스에 - 추가
# "".join(strList)
# >> ABCD-EFG 

# 3.
# list.insert(index, x)
# ex) a = [1, 2, 3]
# a.insert(1, 0)
# >> [1, 0, 2, 3]


# eval 함수 - 문자열로 된 수학식 계산 - 오류 발생가능성 있으니 사용지양

# 다른 사람 풀이

# 최솟값 만들기 위해선 - 기준으로 괄호 치면 됨
# 55 - 50 + 40 - 30 + 20
# >> 55 - (50 + 40) - (30 + 20)

# ['55' , '50 + 40', '30 + 20']
# 각 원소 값 계산 후, 첫 번째 원소에서 나머지 원소들의 값을 빼주면 된다.

str = input().split('-')

num = [] # 계산된 숫자 값 배열

for semiStr in str:
    cnt = 0
    s = semiStr.split('+')
    
    for n in semiStr:
        cnt += int(n)
        
    num.append(cnt)
    
result = num[0]

for i in range(1, len(num)):
    result -= num[i]
    
print(result)

# 비슷하지만 또 다른 풀이
str = input().split('-')

for i in range(len(arr)):
    semiStr = arr[i]
    temp = sum(list(map(int, semiStr.split('+'))))
    if i == 0:
        answer = temp
    else:
        answer -= temp

print(answer)
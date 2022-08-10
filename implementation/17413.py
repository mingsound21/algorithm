from curses.ascii import isalnum
import sys
input = sys.stdin.readline

# 문자열 슬라이싱 사용
word = list(input().rstrip())
i = 0
start = 0

while i < len(word):
    if word[i] == '<': # 열린 괄호 만나면
        i += 1
        while word[i] != '>': # 닫힌 괄호 만날 때 까지 i 증가
            i += 1
        i += 1 # 닫힌 괄호 만났을때 i 증가
    elif word[i].isalnum(): # 숫자나 알파벳 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start: i]
        tmp.reverse()
        word[start:i] = tmp # 거꾸로 바꿔서 다시 word에 저장
    else: # 공백이면 
        i += 1 # 그냥 i 증가
        
print("".join(word))


# 스택을 사용한 풀이
text = list(input().rstrip())

flag = False
result = ""
stack = ""

# <, ' '를 만나기 전에는 모두 스택에 넣고
# <를 만나면 다른 스택에 넣어두고
# >를 만나면 스택이랑 합침

for i in text:
    if flag == False: # 열린 괄호 만나지 않은 경우
        if i == '<':
            flag = True
            stack += i
        elif i == ' ': # 공백 만나면
            stack += i
            result += stack # 단어 거꾸로 저장되어있는 stack을 결과에 더해줌
            stack = '' # 스택 초기화
        else: # 영어, 숫자
            stack = i + stack # 앞에 있던 stack을 뒤로 붙임 -> 거꾸로 저장
    
    elif flag == True: # 열린 괄호 만난 이후
        stack += i
        if i == '>': # 닫힌 괄호를 만나면
            flag = False
            result += stack
            stack = ""
            
print(result + stack)
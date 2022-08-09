import sys
input = sys.stdin.readline

string = input().rstrip()
openTag = False
idx = 0

for i in range(len(string)):
    if openTag:
        if string[i] != '>':
            print(string[i], end = "")
        else:
            print(string[i],end = "")
            idx = i + 1
            openTag = False
        continue
        
        
    if string[i] in ['<', ' ']:
        if string[i] == '<':
            openTag = True
            if i == 0: 
                print(string[i], end = "")
                continue
            
        if idx == 0:
            word = string[i-1::-1]
        else:
            word = string[i-1:idx-1:-1]
        print(word, end = "")
        idx = i+1
        
        print(string[i], end = "")
        
    if i == len(string) -1 :
        if idx == 0:
            word = string[i::-1]
        else:
            word = string[i:idx-1:-1]
        print(word,end = "")

# string을 거꾸로 출력하고 싶을 때,
# string[len(string)-1: -1: -1] -> 안됨
# string[len(string)-1: : -1] -> 끝을 아예 비워놔야됨

# 풀긴 풀었는데 시간 오래걸림,, 문자열 다루는게 익숙치 않은 듯,,,
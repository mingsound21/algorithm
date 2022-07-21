import sys
input = sys.stdin.readline

dict_alp = {}
alp_word = []

n = int(input())
for i in range(n):
    str = input().rstrip()
    alp_word.append(str)
    
    idx = 1
    
    for j in range(len(str)-1, -1, -1):
        alp = str[j]
        if alp in list(dict_alp.keys()):
            if(dict_alp[alp] < idx):
                dict_alp[alp] = idx
        else:
            dict_alp[alp] = idx
            
        idx += 1

# print(dict_alp)

dict2 = dict(sorted(dict_alp.items(), key=lambda x : x[1], reverse=True))

num = 9
for key in list(dict2.keys()):
    dict2[key] = num
    num -= 1

# print(dict2)
    
answer = 0
for word in alp_word:
    sum = 0
    for j in range(len(word)):
        sum = sum*10 + dict2[word[j]]
    answer += sum
print(answer)
        
        
    
# 가장 높은 자릿수의 알파벳일수록 큰 숫자를 할당

# arr에 [알파벳, 위치] 형태로 넣기
# 이미 arr에 있는 알파벳이 더 높은 자릿수에 위치한 경우, 위치값

# 아스키 코드 -> 문자 : chr() 
# 문자 -> 아스키 코드 : ord()

# 딕셔너리 정렬, key값에 따라, value값에 따라, 오름차순, 내림차순
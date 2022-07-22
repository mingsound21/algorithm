import sys
input = sys.stdin.readline

dict_alp = {}
digit = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]

n = int(input())
for i in range(n):
    str = input().rstrip()
    idx = 0
    for j in range(len(str)-1, -1, -1):
        alp = str[j]
        
        if alp in list(dict_alp.keys()):
            dict_alp[alp] += digit[idx]
        else:
            dict_alp[alp] = digit[idx]
            
        idx += 1

dict2 = dict(sorted(dict_alp.items(), key=lambda x : x[1], reverse=True))

num = 9
answer = 0

for key, item in list(dict2.items()):
    answer += num * item
    num -= 1
    
print(answer)

# 가장 높은 자릿수의 알파벳일수록 큰 숫자를 할당

# arr에 [알파벳, 위치] 형태로 넣기
# 이미 arr에 있는 알파벳이 더 높은 자릿수에 위치한 경우, 위치값

# 아스키 코드 -> 문자 : chr() 
# 문자 -> 아스키 코드 : ord()


# 이 풀이는 틀림
# -> 예외적으로 가장 높은 자릿수의 알파벳에 큰 숫자를 할당했을경우 답이 아닐 수 있음
# 반례)
# 10
# ABB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB

# 988 + (88 * 9) = 1780
# 899 + (99 * 9) = 1790


# 정답 풀이
# 그리디) 가장 큰 비율을 차지하는 알파벳에 큰 수를 부여

# ! 그리디) 그 해법이 정당한지 검토 필요 !
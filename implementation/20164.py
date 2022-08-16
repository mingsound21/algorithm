import sys
input = sys.stdin.readline().rstrip

n = input()

min_v = 1e9
max_v = 0

def cnt_odd(n : str):
    odd_n = 0
    for i in n:
        if int(i) % 2 != 0:
            odd_n += 1
    return odd_n

def solve(n, odd_n):
    global max_v, min_v # global이라서 재귀를 사용해도 전체적인 max_v, min_v 비교가 가능
    
    if len(n) == 1:
        min_v = min(min_v, odd_n)
        max_v = max(max_v, odd_n)
    elif len(n) == 2:
        temp = str(int(n[0]) + int(n[1]))
        solve(temp, odd_n + cnt_odd(temp))
    else:
        for i in range(1, len(n)-1): # 문자열 분해 어렵....
            for j in range(i+1, len(n)):
                a = n[:i]
                b = n[i:j]
                c = n[j:]
                temp = str(int(a) + int(b) + int(c))
                solve(temp, odd_n + cnt_odd(temp))

solve(n, cnt_odd(n))
print(min_v, max_v)

# 구현, 재귀**
# 자를 수 있는 모든 경우의 수를 해봐야 할듯

# 참고
# 파이썬(3.6부터) 함수 매개변수 타입 선언 가능
'''
def function_name(parameter1 : type) -> return_type:
    함수 내용 작성
'''
    

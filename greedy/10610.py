import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, str(n)))
n_sum = sum(n_list)

# 30배수 가능한지
if(0 not in n_list):
    print(-1)
elif n_sum % 3 != 0:
    print(-1)
else:
    n_list.sort(reverse=True)
    print("".join(list(map(str, n_list)))) # join은 str type이어야함
    

# 숫자 순서 변경해서 제일 큰 30의 배수 만들기 - 못 만들면 -1 출력
# 3의 배수 판정법 : 모든 자리 수의 합이 3의 배수이다

# 숫자를 각 자리수의 list로 변환
# n_list = list(map(int, str(n)))
# 또는 
# [int(a) for a in str(정수)]
import sys
input = sys.stdin.readline

n = int(input())
data = [float(input()) for _ in range(n)]
dp = [0] * n
dp[0] = data[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] * data[i], data[i])


print('%.3f' % max(dp)) # round 함수 사용시 틀렸다고 나옴


# 연속된 수들의 곱이 최대가 되는 부분을 찾아 출력

# 소수점 제한
# 1. round(반올림하고자 하는 값, 자릿수[defualt : 0])
# >> 자릿수 적지 않으면, 소수점 첫번째 자리에서 반올림함

# 2. format 서식 지정
# "{인덱스 : 소수점 자릿수}".format(값0, 값1)
# print("format example : {: .2f}, {: .2f}".format(1.2345, 3.254))
# +++) 변수 지정도 가능
# "{num}, {gender}".format(num = 123, gender = '여')
# 참고 : https://blockdmask.tistory.com/424

# 3. f-string
# f' {변수 : 소수점 자릿수}'
# num = 1.234
# print(f'f-string example : {num : .1f}')
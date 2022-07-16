import sys
input = sys.stdin.readline

N = int(input())

time = [[0]*2 for _ in range(N)]
for i in range(N):
    s, e = map(int, input().split())
    time[i][0] = s
    time[i][1] = e

time. sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)

# 정답
# 회의가 빨리 끝난 것을 택하고, 회의가 끝나는 시간이 같다면 빨리 시작하는 것을 택한다
# 예) 2
#     2 2
#     1 2
# 이경우 (2, 2)를 먼저 택하면, (1, 2)의 시작시간이 (2, 2)의 끝나는 시간보다 작아서 택해지지 않음

# 회의 시작시간과 끝나는 시간이 같을 수 있다 => (2, 2)와 같은 case 생각

# 첫 시도
# 사용시간이 짧은 것을 선택할수록 많은 회의를 할 수 있다.
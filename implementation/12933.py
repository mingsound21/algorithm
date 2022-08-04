import sys
input = sys.stdin.readline

sound = input().rstrip() # rstrip() 안하면 마지막에 '\n'까지 포함됨
cnt = [0] * 5
duck = 'quack'
answer = 0

for s in sound:
    idx = duck.find(s)
    
    if idx == 0:
        cnt[idx] += 1
        continue
    
    if cnt[idx-1] >= cnt[idx] + 1: 
        if s == 'k':
            answer = max(answer, cnt[0]-cnt[-1])
        cnt[idx] += 1
    else: # 순서에 맞지 않게 소리나면 오류
        print(-1)
        exit(0)

if cnt[0] != cnt[-1]: # quack가 완벽하게 나오지 않았다면 오류
    print(-1)
    exit(0)
    
print(answer)
    

# 울음소리 연속될 필요 없으나, "순서"는 "quack"

# 파이썬 문법 정리
# >> find - 찾는 문자열 없으면 -1 리턴
#         - 문자열 변수에만 사용가능, (리스트, 튜플, 딕셔너리에선 find 사용불가)
# >> index - 찾는 문자열 없으면 ValueError 발생
#          - 문자열, 리스트, 튜플 자료형에 사용 가능 (딕셔너리에선 사용 불가)

# 문제 이해가 어려웠음
# >> 단순히 quack 소리 개수를 세는 게 아니라 동시간대에 quack 소리가 난 개수를 찾아야함!

import sys
input = sys.stdin.readline

case = 1
while True:
    # 연속하는 p일 중 l일 동안 사용가능, v일 짜리 휴가 시작
    l, p, v = map(int, input().split()) 
    
    # 종료
    if not l and not p and not v: # l==p==v==0: 도 가능
        break
    
    # day = (v // p) * l + (v % p) - 틀림, 반례 2 8 20 -> answer : 6이어야함. (내 답 : 8)
    # v % p > l 일 수 있음
    day =  (v // p) * l
    if v % p > l :
        day += l
    else:
        day += v % p
    print('Case ' + str(case) + ': ' + str(day)) # 문자 + str(숫자)
    
    case += 1
    

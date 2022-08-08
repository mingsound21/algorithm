import sys
input = sys.stdin.readline



eng = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
kor = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0, 1, 1, 1, 1],
       [0, 0, 0, 0, 1, 1, 1]] # 0 왼손 1 오른손

def position(alp):
    for i in range(3):
        idx = eng[i].find(alp)
        if idx != -1:
            return i, idx
        
def move_time(alp):
    global lx, ly, rx, ry
    x, y = position(alp)
    
    if kor[x][y] == 0: # 왼손 이동
        time = abs(x - lx) + abs(y - ly)
        lx = x
        ly = y
    else: # 오른손 이동
        time = abs(x - rx) + abs(y - ry)
        rx = x
        ry = y
        
    return time

l, r = input().rstrip().split()
string = list(input().rstrip())

lx, ly = position(l)
rx, ry = position(r)

answer = 0
for s in string:
    answer += move_time(s) + 1


print(answer)
    

# find
# >> 찾는 문자 없으면 -1 리턴
# >> 문자열에만 사용가능

# index
# >> 찾는 문자 없으면 에러 발생 -> in으로 확인한뒤 index 사용
# >> 문자열, 리스트, 튜플 사용 가능 (딕셔너리 불가)
import sys
input = sys.stdin.readline

n, m ,r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
op = list(map(int, input().split())) # r개의 입력


def vertical():
    for i in range(n//2):
        temp = data[i]
        data[i] = data[n-i-1]
        data[n-i-1] = temp

def horizontal():
    for i in range(n):
        for j in range(m//2):
            temp = data[i][j]
            data[i][j] = data[i][m-j-1]
            data[i][m-j-1] = temp

def right90():
    global data, n, m 
    temp = [[0] * n for _ in range(m)]
    for i in range(n):
        d = data[i]
        for j in range(m):
            temp[j][n-i-1] = d[j]
    data = temp
    n, m = m, n 
    
def left90():
    global data, n, m 
    temp = [[0] * n for _ in range(m)]
    for i in range(n):
        d = data[i]
        for j in range(m):
            temp[j][i] = d[m-j-1]
    data = temp
    n, m = m, n 
    
def right4group():
    N = n//2
    M = m//2
    for i in range(n//2):
        temp = data[i][:M]
        data[i][:M] = data[N+i][:M]
        data[N+i][:M] = data[N+i][M:]
        data[N+i][M:] = data[i][M:]
        data[i][M:] = temp
            
def left4group():
    N = n//2
    M = m//2
    for i in range(n//2):
        temp = data[i][:M]
        data[i][:M] = data[i][M:]
        data[i][M:] = data[N+i][M:]
        data[N+i][M:] = data[N+i][:M]
        data[N+i][:M] = temp
        

for i in op:
    if i == 1:
        vertical()
    elif i == 2:
        horizontal()
    elif i == 3:
        # data = right90()
        right90()
    elif i == 4:
        # data = left90()
        left90()
    elif i == 5:
        right4group()
    else:
        left4group()

for d in data:
    for a in d:
        print(a, end = ' ')
    print()

# print(*1차원배열) 이런형태로 작성 가능
'''
for d in data:
    print(*d)
'''

# 문제해석
# 1. 상하반전
# 2. 좌우반전
# 3. 오른쪽으로 90회전
# 4. 왼쪽 90회전
# 5. 4개 그룹을 오른쪽으로 회전
# 6. 4개 그룹을 왼쪽으로 회전

# 파이썬 문법
# global
# 함수 안에서 함수밖에 선언한 변수를 사용한다는 것을 밝히기 위해서,
# 함수 안에서 "global 전역변수" 이러한 형태로 사용함


# 문제 풀때 3, 4번 operation할때 새로운 배열을 만들어서 옮기면 메모리가 많이 나올까봐 걱정됐는데
# 가로 세로 길이가 달라서 도저히 원래 배열에서는 어떻게 해야할지 모르겠어서 새로운 배열을 선언함

# 맞긴했으나,, 복잡했다...

# 다른 사람 풀이도 유사했다... temp라는 새로운 배열을 만들고 옮기고 다시 data = temp이런식으로....


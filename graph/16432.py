import sys
input = sys.stdin.readline
from collections import deque

def dfs(cnt, dduks, yesterday): # cnt = dduks의 len, dduck = 각 날짜마다 먹은 떡 담기, yesterday = 이전날에 먹은 떡 종류
    global answer
    
    if cnt == n: # 만약 n개의 떡을 채웠다면
        for d in dduks: # 모든 떡 출력 후 종료
            print(d)
        exit()
    
    for dduk in days[cnt]: # 해당 날짜의 모든 떡을 돌면서
        if dduk != yesterday and not ate[cnt][dduk-1]: # 만약 이전날에 먹은 떡의 종류와 다르고, 해당 날짜에 이미 그 종류의 떡을 먹지 않았다면(해당날짜에 이미 그 떡을 먹은 경우는 이미 다른 가능한 경우가 있었다는 것)
            ate[cnt][dduk-1] = True # 먹었다고 표시
            dfs(cnt+1, dduks + [dduk], dduk) # 다음 날로 이동
    
    
    
n = int(input())
days = []
answer = []
for _ in range(n):
    m, *dduk = map(int, input().split()) # *를 사용해서 이렇게 숫자 + 배열 형태로 받을 수 있음
    days.append(dduk)

ate = {i : [False for _ in range(10)] for i in range(n+1)} # 딕셔러니 형태 {날짜 : [0-9까지의 False]}
dfs(0, [], 0)
print(-1)

# 떡 종류는 9개 (1~9)
# 전날 먹었던 떡과 같은 종류의 떡이면 먹지 않음
# 줄 수 있는 떡 없으면 호랑이한테 잡아 먹힘
# n일동안 떡을 팔러 나감
# n일동안 호랑이에게 잡아먹히지 않도록 호랑이에게 줄 떡 고르기

#------------------------------------------------------
# *args : 파라미터를 몇개 받을지 모르는 경우 사용
# 튜플 형태로 전달됨

# **kwargs : 파라미터명을 같이 보낼 수 있다
# 딕셔너리 형태로 전달됨

def print_param_args(*args):
    print(args)
print_param_args('a', 'b', 'c')
# ('a', 'b', 'c')


def print_param_kwargs(**kwargs):
    print(kwargs)
print_param_kwargs(first = 1, second = 'b', third = 'c')
# {'first': 1, 'second': 'b', 'third': 'c'}

# >> 참고 : https://sshkim.tistory.com/182


# 어렵.....

# 여러가지 경우가 가능해서 bfs보다는 dfs가 나은 풀이 인듯...

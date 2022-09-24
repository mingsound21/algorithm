import sys
input = sys.stdin.readline
from collections import deque

# x = 51
# str_x = str(x)
# str_x = (4-len(str_x)) * '0' + str_x

# nx = int(str_x[1:] + str_x[0])
# print('L', nx)

# nx = int(str_x[len(str_x)-1] + str_x[:len(str_x)-1])
# print('R', nx)



def bfs(a, b):
    visited = [0] * 10001
    queue = deque([(a, [])])
    visited[a] = 1
    
    while queue:
        x, arr = queue.popleft()
        
        if x == b:
            print("".join(arr))
            return
            
        nx = 2*x % 10000
        if not visited[nx]:
            visited[nx] = 1
            queue.append((nx, arr + ['D']))
        
        nx = x-1 if x != 0 else 9999
        if not visited[nx]:
            visited[nx] = 1
            queue.append((nx, arr + ['S']))
            
        str_x = str(x)
        str_x = (4-len(str_x)) * '0' + str_x
        
        nx = int(str_x[1:] + str_x[0])
        if not visited[nx]:
            visited[nx] = 1
            queue.append((nx, arr + ['L']))


        nx = int(str_x[len(str_x)-1] + str_x[:len(str_x)-1])
        if not visited[nx]:
            visited[nx] = 1
            queue.append((nx, arr + ['R']))


for _ in range(int(input())):
    a, b = map(int, input().split())
    bfs(a, b)
    
    
# 4개의 명령어 D S L R
# D : 2n % 10000 을 레지스터에 저장
# S : n-1을 레지스터에 저장(n==0이면 9999가 저장됨)
# L : n의 각 자릿수를 왼편으로 회전시켜 레지스터에 저장
# R : n의 각 자릿수를 오른편으로 회전시켜 레지스터에 저장
# L, R의 경우 0이 포함된 경우를 주의!!

# A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램

# 처음엔 15 -> R : 51, L : 51인줄 알았는데 이게 아니라, 15 -> R : 5001, L : 510이었음
# >> 그래서 15 -> 0015로 바꾸어서 해결

# 다른 사람 풀이

for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, ""))
    visit = [False] * 10000
    
    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == b:
            print(path)
            break
        
        # 1
        num2 = (2*num) % 10000
        if not visit[num2]:
            q.append((num2, path + "D"))
            visit[num2] = True
            
        # 2
        num2 = (num-1) % 10000
        if not visit[num2]:
            q.append((num2, path + "S"))
            visit[num2] = True

        # 3
        num2 = (10 * num + (num // 1000)) % 10000 # 이렇게 계산하는게 더 시간이 적게 걸리네...
        if not visit[num2]:
            q.append((num2, path + "L"))
            visit[num2] = True
        
        # 4
        num2 = (num//10 + (num%10) * 1000) % 10000
        if not visit[num2]:
            q.append((num2, path + "R"))
            visit[num2] = True

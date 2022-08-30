import sys
input = sys.stdin.readline

k = int(input())
n = int(input())
final = list(input().rstrip())
data = [list(input().rstrip()) for _ in range(n)]
before = [''] * k
after = [''] * k

ch = 'A'
for j in range(k):
    
    idx = j
    for i in range(n):
        if data[i][0] == '?':
            break
        
        if idx < k-1 and data[i][idx] == '-':
            idx += 1
        elif idx-1 >= 0 and data[i][idx-1] == '-' :
            idx -= 1
            
    before[idx] = ch
    ch = chr(ord(ch) + 1)
    
    idx = j
    for i in range(n-1, -1, -1):
        if data[i][0] == '?':
            break
        
        if idx < k-1 and data[i][idx] == '-':
            idx += 1
        elif idx-1 >= 0 and data[i][idx-1] == '-' :
            idx -= 1
    
    after[idx] = final[j]

dx = [-1, 0, 1]
check = [0] * k
answer = ['*'] * (k-1)
for i in range(k):
    for j in range(3):
        nx = i + dx[j]
        if nx < 0 or nx >= k:
            continue
        if before[i] == after[nx]:
            check[i] = 1
            if j==2:
                answer[i] = "-"
            
if(sum(check) == k):
    print("".join(answer))
else:
    print('x' * (k-1))

# 하나의 가로 줄이 감춰진 사다리르 받아 적절한 곳에 놓아 참가자들의 최종 순서가 원하는 순서대로 나오도록
# 막대 없으면 *, 있으면 -, 감춰진건 ?
# 어떻게 해도 원하는 순서 얻을 수 없으면 x로
# >> before, after(감춰진곳 바로 전, 후의 상태) 비교했을때 이동해야하는 거리가 1이상이면


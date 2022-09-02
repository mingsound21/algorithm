from itertools import combinations
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
# ice[a][b] = True >> a와 b는 같이 먹으면 안되는 조합
ice = [[False for _ in range(n)] for _ in range(n)] # 최대 200

for i in range(m): # 최대 10000
    a, b = map(int, input().split())
    ice[a-1][b-1] = True
    ice[b-1][a-1] = True

result = 0

# 최대 1,313,400
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1
            
# for i in combinations(range(n), 3):
#     if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
#         continue
#     result += 1
                
print(result)


# 내 풀이 >> 시간 초과
import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
data = list(combinations([i for i in range(1, n+1)], 3))
dont = [[] for _ in range(201)]

for i in range(m):
    a, b = map(int, input().split())
    dont[a].append(b)
    
answer = 0
for d in data: # 최대 1,313,400
    check = 0
    for i in range(1, n+1): # 최대 200
        if i in d: # 최대 200
            for j in range(len(dont[i])):
                if dont[i][j] in d:
                    check = 1
                    
        if check == 1:
            break
        
    if check == 0:
        answer += 1

print(answer)
import sys
input = sys.stdin.readline
n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
    
check = [[0]*n for _ in range(n)]

def dfs(x, y):
    if check[x][y] != 0:
        return check[x][y]
    if data[x][y] == 0 and x == n-1 and y == n-1:
        return 1
    if data[x][y] == 0 and x != n-1 and y != n-1:
        return 0
    
    nx = x + data[x][y]
    ny = y + data[x][y]
    a = b = 0
        
    if 0 <= nx < n:
        a = dfs(nx, y)
    if 0 <= ny < n:
        b = dfs(x, ny)
    check[x][y] = a + b
    return a + b

print(dfs(0, 0))

# 맞추긴했다...
# 마지막칸을 제외하고도 중간에 0이 있을 수 있다는 생각을 못했음...

# 다른 사람 풀이
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)] # 해당 위치
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        
        d = i + data[i][j] # 아래
        r = j + data[i][j] # 오른쪽
            
        if d < n:
            dp[d][j] += dp[i][j]
        if r < n:
            dp[i][r] += dp[i][j]
            
            
print(dp[i][j])
# 마지막 칸이 아니지만, 0인 칸이 있더라도 잘못된 dp값이 다른 곳으로 영향을 미치지 않아서 괜찮다.
# >> 내 생각... 정확하지 않을 수 있음...
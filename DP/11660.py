import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [ [0] + list(map(int, input().split())) for _ in range(n)]
data = [[0 for _ in range(n+1)]] + data

for j in range(2, n+1):
    data[1][j] += data[1][j-1] # 첫 행
    
for i in range(2, n+1):
    data[i][1] += data[i-1][1] # 첫 열
    for j in range(2, n+1):
        data[i][j] = data[i][j] + data[i-1][j] + (data[i][j-1] - data[i-1][j-1])

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = data[x2][y2] - data[x2][y1-1] - data[x1-1][y2] + data[x1-1][y1-1]
    print(answer)
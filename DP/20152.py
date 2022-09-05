import sys
input = sys.stdin.readline

h, n = map(int, input().split())
if h > n:
    h, n = n, h

# h가 n보다 작다고 가정
data = [[0 for i in range(n+1)] for j in range(n+1)]


data[h][h] = 1
for i in range(h+1, n+1):
    for j in range(h, i+1):
        if i-1 < 0:
            data[i][j] = 1
            continue
        data[i][j] = data[i-1][j] + data[i][j-1]

print(data[n][n])

# 상하좌우 1칸씩 이동
# 집에서 pc방까지 최단 경로로 이동
# y>x 인 (x, y)는 침수 >> 맨윗줄에서 부터 역으로 계단 만들어진 형태는 이동 불가능
# pc방 == 집인 경우는 경로 : 1
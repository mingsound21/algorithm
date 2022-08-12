import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
data = [list(map(int, input().split(" "))) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = data[x][y]
        
        # 좌
        for j in range(i + 1, n - i):
            x = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
            
        # 하
        for j in range(i + 1, m - i):
            y = j
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
        
        # 우
        for j in range(i + 1, n - i):
            x = n - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
        
        # 상
        for j in range(i + 1, m - i):
            y = m - j - 1
            prev_value = data[x][y]
            data[x][y] = temp
            temp = prev_value
        
for i in range(n):
    for j in range(m):
        print(data[i][j], end = " ")
    print()
    

# 배열 돌리기... temp...

# n, m <= 300, r = 1000이길래
# 이런식으로 돌려도 괜찮을 거라 생각 못했는데
# 위의 방법도 생각해보니, 시간복잡도 O(300000)인듯,,,
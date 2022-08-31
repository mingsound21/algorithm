import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

row = n
col = m
for i in range(min(n, m) // 2):
    totalLen = (n-(2*i) + m-(2*i)) * 2 - 4
    turn = r % totalLen
    # print(totalLen, turn)
    for R in range(turn):
        
        temp = data[i][i]
        # 위
        data[i][i:col-1] = data[i][i+1:col]

        # 오른쪽
        for j in range(i, row-1):
            data[j][col-1] = data[j+1][col-1]
            
        # 아래
        data[row-1][i+1:col] = data[row-1][i:col-1]
        
        # 왼쪽
        for j in range(row-1, i, -1): # 여기 i대신 1로 써서 계속 틀림....
            data[j][i] = data[j-1][i]
            
        data[i+1][i] = temp
        
    row -= 1
    col -= 1
    
# print(">" * 11)
for d in data:
    print(*d)
    
# 구현 : 차분히 생각하고 풀자
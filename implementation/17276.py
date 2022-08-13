import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n, d = map(int, input().split()) # n 홀수, d 각도
    data = []
    # 시계방향이면 -1, 반시계면 + 1
    # position을 반시계 방향으로 저장해서 18번째 줄에 -a를 했음
    position = [(0, n//2), (0, 0), (n//2, 0), (n-1, 0),(n-1, n//2), (n-1, n-1), (n//2, n-1),(0, n-1)]
    move = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    for i in range(n):
        data.append(list(map(int, input().split())))
    a = d // 45
    start_position = []
    line = []
    for i in range(0, 4):
        idx = (i - a + 8) % 8
        start_position.append(idx)

        x, y = position[i]
        dx, dy = move[i]
        arr = [data[x][y]]
        for j in range(n-1):
            x += dx
            y += dy
            arr.append(data[x][y])
        line.append(arr)
        
    for i in range(4):
        idx = start_position[i]
        x, y = position[idx]
        dx, dy = move[idx]
        data[x][y] = line[i][0]
        for j in range(1, n):
            x += dx
            y += dy
            data[x][y] = line[i][j]
    
    for i in range(n):
        for j in range(n):
            print(data[i][j], end = " ")
        print()
    
    
# 풀면서 이 방법이 맞는지는 모르겠다...는 마음으로 풀긴했음...
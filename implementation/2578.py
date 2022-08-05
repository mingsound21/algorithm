import sys
input = sys.stdin.readline

graph = []
number = []
check = [[0] * 5 for _ in range(5)]

for _ in range(5):
    graph.append(list(map(int, input().split())))

for _ in range(5):
    number.append(list(map(int, input().split())))


def check_line():
    # 가로
    cnt = 0
    for line in check:
        if sum(line) == 5:
            cnt += 1
    
    # 세로 
    for j in range(5):
        line_sum = 0
        for i in range(5):
            line_sum += check[i][j]
        
        if line_sum == 5:
            cnt += 1
            
    # 대각선
    line_sum = 0
    for i in range(5):
        line_sum += check[i][i]
    if line_sum == 5:
            cnt += 1
            
    line_sum = 0
    for i in range(5):
        line_sum += check[i][4-i]
    if line_sum == 5:
            cnt += 1
    
    if cnt >= 3:
        return True
    return False

# 다른 사람 풀이 참고해서 만든 빙고 검증 함수
def check_line2():
    cnt = 0
    
    # 대각선
    if [check[k][k] for k in range(5)].count(1) == 5:
        cnt += 1
    
    if [check[k][4-k] for k in range(5)].count(1) == 5:
        cnt += 1
    
    # 가로
    for line in check:
        if line.count(1) == 5:
            cnt += 1

    # 세로
    for j in range(5):
        if [check[k][j] for k in range(5)].count(1) == 5:
            cnt += 1
    
    if cnt >= 3:
        return True
    return False

call = 0
for num in number:
    for n in num:
        call += 1
        for i in range(5):
            for j in range(5):
                if graph[i][j] == n:
                    check[i][j] = 1
                    if check_line2():
                        print(call)
                        exit(0)
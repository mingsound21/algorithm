import sys
input = sys.stdin.readline

graph = []
for _ in range(19):
    graph.append(list(map(int, input().split())))
    
# 오른쪽, 아래, 우하향, 우상향(가장 왼쪽 위 위치 출력해야해서)
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if graph[x][y] in [1, 2]:
            win = graph[x][y]
            
            for i in range(4):
                nx = x - dx[i]
                ny = y - dy[i]
                if 0 <= nx < 19 and 0 <= ny < 19 and graph[nx][ny] == win:
                    continue
                
                cnt = 1 # 이미 현재 위치는 0이 아님이 확인되었고, 아래의 for문에서도 확인하지 않음
                check = False # 혹시 연속 6알인지 체크
                ax = x
                by = y
                
                for j in range(5): # x, y위치를 제외하고 확인
                    
                    ax += dx[i]
                    by += dy[i]
                    
                    if ax < 0 or ax >= 19 or by < 0 or by >= 19:
                        break
                    
                    if j == 4 and graph[ax][by] == win:
                        check = True
                        break
                    
                    if graph[ax][by] == win:
                        cnt += 1
                    else:
                        break
                
                if check ==  True:
                    continue # 여기를 break로 둬서 계속 틀렸었음...
                
                if cnt == 5 and check == False:
                    print(win)
                    print(x + 1, y + 1)
                    exit(0)
                
print(0)

# <문제>
# 가로, 세로, 대각선으로 딱 5개 연속적으로 놓인 경우 이김
# 흰색 승(2), 검은색 승(1), 아직 승부 X(0)
# 승부 났으면 가장 왼쪽 위에 있는 바둑알의 가로, 세로를 출력

import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))
    

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

boolean = False

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                
                if x < 0 or x >= r or y < 0 or y >= c:
                    continue
                
                if graph[x][y] == 'S':
                    boolean = True
                    break
                
if boolean:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '.':
                graph[i][j] = 'D'
    
    for k in graph:
        print(''.join(k))

# 울타리 설치해 늑대가 양 칸으로 갈 수 없도록

# hint : 울타리 개수 제한 x, 예제 3에서 늑대가 없는데 울타리를 가운데 설치


# 예제에선 D를 몇군데만 설치해서 헷갈렸는데, 그냥 모든 가능한 자리에 D를 설치해도 정답으로 인정이 되는 것이었다.
from collections import deque

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # deque 생성
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치 벗어났는지 확인
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            
            # 벽으로 막혀있는지 확인
            if graph[nx][ny] == 0:
                continue
            
            # 1이 아닌 다른 값이면 이미 다른 최단 경로가 있다는 소리
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                
    return graph[n-1][m-1]

print(bfs(0, 0))

# 어느 한 곳의 위치에 서로 다른 경로로 도착 할 수 있어서, 각각의 경로의 계산에 서로가 영향을 미치지 않아야하기에 도착한 곳의 위치값을 변경하면 안된다고 생각했음.
# >> 근데 어느 한 곳에 어떤 경로가 먼저 도착했을 경우, 그 경로가 최단경로라는 말이 되므로, 경로를 이동할때마다 위치값을 변경해도 된다는 생각으로 바뀜.

# 숫자를 각자리 숫자 list로 : list(map(int, str(숫자)))


'''
# DFS, BFS 모두 적합한 유형 : 단순히 모든 정점 방문이 중요한 문제

# DFS가 적합한 유형 : 
    1. 그래프가 큰 경우(정점, 간선 개수 많을 때)
    2. 경로의 특징을 저장해야하는 경우
        예) 각 정점에 숫자 적혀 있고, a에서 b까지 가는 경로 구할때, 경로에 같은 숫자가 있으면 안됨
        >> BFS는 경로의 특징 가지지 못함
        
# BFS가 적합한 유형 : 
    1. 최단거리 구하기 
        cf. DFS는 처음으로 발견되는 해답이 최단거리라는 보장 X
        BFS는 현재 노드에서 가까운 곳부터 찾기 때문에 경로 탐색시 첫번 째로 찾아지는 해답이 곧 최단거리
'''

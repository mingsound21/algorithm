from copy import deepcopy
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(virus):
    # 주의! bfs 내에서는 모두 다 copy_graph로 체크를 해야함. 그냥 graph로 했더니 틀림.
    copy_graph = deepcopy(graph)
    visited = [[0]*n for _ in range(n)]
    queue = deque(virus)
    for x, y in virus:
        copy_graph[x][y] = 3 # 활성된 건 3
        visited[x][y] = 1 # 시간 나중에 최종적으로는 -1
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 안에 있고, 벽이 아니며, 방문하지 않았다면 (주의. 비활성인것도 감염시킬 필요X, 그대신 통과는 가능함)
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and copy_graph[nx][ny] != 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    # 주의! 여기에서는 시간의 max를 구해서 return
    _min = 0
    for i in range(n):
        for j in range(n):
            if copy_graph[i][j] in [1, 2]:# 벽이거나 비활성 바이러스인 경우(비활성은 감염X)
                continue
            
            if visited[i][j] == 0: # 벽X, 비활성X이면서 방문하지 않은 경우
                return -1
            
            _min = max(_min, visited[i][j])
    
    return _min-1

virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))


answer = 50000 # 이걸 초기값을 500이라고 했더니, 틀림. 생각해보니 2500까진 가능했던 값이었음...
for vi in list(combinations(virus, m)):
    result = bfs(vi)
    if result == -1:
        continue
    # 주의. 여기에서는 최대시간의 min값 구해야함
    answer = min(answer, result)

if answer == 50000:
    print(-1)
else:
    print(answer)
    
# 바이러스 : 활성 / 비활성
# 처음에는 모두 비활성
# 활성 바이러스는 상하좌우 인접한칸으로 동시에 복제 (1초 걸림)
# m개의 바이러스 활성 상태로 변경

# 빈칸 0, 벽 1, 바이러스 2

# 연구소의 상태가 주어졌을때, 모든 빈칸에 바이러스를 퍼뜨리는 최소시간 구하기

# ************ 연구소 2와의 차이가 뭐지? ************
# >> 비활성바이러스는 감염 시킬 필요가 없음(시간체크에 포함하지 않아도됨)
# >> 비활성 바이러스는 통과 가능하다는 점에서는 빈칸과 같고, 감염시키지 않아도되기에 시간체크에는 포함되지 않는다는 점에서는 벽과 같다
# >> 참고 ) https://www.acmicpc.net/board/view/98175
'''
예 1)
4 1
1 1 1 1
1 1 1 1
1 1 1 1
0 2 2 0
>> 2를 통과할 수 없다고 하면 답이 -1, 그러나 답은 2

4 1
1 1 1 1
1 1 1 1
1 1 1 1
2 0 0 2
>> 2를 감염시켜야 한다고 판단하면, 답이 3, 그러나 답은 2
'''
from collections import deque
import sys
input = sys.stdin.readline

# 시간 초과 코드...

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
connect = [] # 각각 개별 연결 요소들의 좌표 배열 담고 있음
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs를 사용해서 각각의 연결 요소 좌표 담은 배열 반환
visited = [[0 for _ in range(m)] for _ in range(n)]
def count(x, y):
    arr = []
    queue = deque([(x, y)])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        arr.append((x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    return arr

zeros = [] # 0 좌표들
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0: # 1이고, 아직 방문 안했으면
            connect.append(count(i, j))
        if graph[i][j] == 0:
            zeros.append((i, j))

_max = 0
for x, y in zeros: # 모든 0 좌표들에 대해서
    check = [0 for _ in range(len(connect))]
    for i in range(4): # 4방향 체크
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있다면
            for k in range(len(connect)): # 연결요소 개수만큼 돌면서
                if (nx, ny) in connect[k]: # 해당 연결요소 좌표안에 (nx, ny)가 있는지
                    if check[k] == 0:
                        check[k] = 1
                    break
    
    cnt = 1
    for i in range(len(check)):
        if check[i] == 1:
            cnt += len(connect[i])
    
    _max = max(_max, cnt)

print(_max)
            
# 1이 들어있는 인접한 칸 끼리 연결했을때 연결 요소에 포함되어있는 1의 개수
# 칸 하나에 들어있는 수를 변경해서 만들 수 있는 모양의 최대 크기

# 다른 사람 정답 코드
n, m = map(int, input().split())
grpah = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    cnt = 1
    q = deque([(i, j)])
    visited[i][j] = num
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = num
                q.append((nx, ny))
                cnt += 1
    return cnt
    
num = 2
group = dict() # 배열의 1들을 그룹핑
# key = num, value = 해당 num(연결요소)의 1의 개수
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j)
            group[num] = cnt
            num += 1
            
result = 0
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            s = set() # 연결요소 번호를 담고 있음
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and visited[nx][ny] not in s:
                    s.add(visited[nx][ny])
            
            res = 1
            
            for ss in s:
                res += group[ss]
            result = max(res, result)
            
print(result)

# 내 풀이와의 차이점
# connect라는 각 연결 요소 좌표를 저장한 배열을 선언
# visited에 각 연결요소를 같은 숫자로 표시

# tip!
# in set을 사용하면 시간 단축 할 수 있다!


# in 의 시간복잡도
# 1. list, tuple
# >> O(n)
# >> 하나 하나 순회하기 때문

# 2. set, dictionary
# >> 평균 : O(1), 최악 : O(n)
# >> 내부적으로는 hash를 통해서 자료들을 저장해서 시간 복잡도 O(1)이 가능하고 O(n)인 경우에는 해시가 성능이 떨어진 경우(충돌이 많은 경우에 발생)

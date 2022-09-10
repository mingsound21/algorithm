from collections import deque
import sys
input = sys.stdin.readline

w, h = map(int, input().split())
graph = [[0 for _ in range(w+2)] for _ in range(h+2)] # 입력받은것에 둘레에 건물 없는 공간을 추가(가로 세로 길이 +2)
for i in range(1, h+1):
    graph[i][1:w+1] = map(int, input().split())
    
dx = [-1, 0, 1, 1, 0, -1]
dy = [[0, -1, 0, 1, 1, 1], [-1, -1, -1, 0, 1, 0]] # 홀, 짝 이동범위 다름

# (0, 0)에서 시작해서 정육각형 범위로 탐색을 하면서 회색건물을 만나면 cnt += 1
# 핵심 : 회색건물을 탐색하는 것이 아니라 주변 흰색 부분을 탐색
# >> 회색 건물에 둘러싸인 흰색 부분을 탐색하지 않음

def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[False for _ in range(w+2)] for _ in range(h+2)]
    visited[x][y] = True
    cnt = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= nx < h+2 and 0 <= ny < w+2:
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                elif graph[nx][ny] == 1:
                    cnt += 1
                    
    return cnt

print(bfs(0, 0))

# 밖에서 보이는 부분만 장식
# 조명을 장식할 벽면의 길이의 합
# 1 : 건물 있음, 0 : 건물 없음

# 벌집 모양
# x 행, y 열
# 행이 홀수 : 아래 좌표 (x+1, y)
# 행이 짝수 : 오른쪽 아래 (x+1, y)


# ++++++그래프++++++
# >> 벌집모양일 수 있구나,,,
# 회색을 기준으로 방문처리하고 queue에 넣고하려고 했는데, 흰색을 기준으로 해야 풀리는 경우도 있겠구나,,,

# 해설 참고 : https://reliablecho-programming.tistory.com/110
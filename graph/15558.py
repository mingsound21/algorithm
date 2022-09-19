import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
graph = []
graph.append(list(map(int, list(input().rstrip()))))
graph.append(list(map(int, list(input().rstrip()))))

visited = [[-1 for _ in range(n)] for _ in range(2)] # 방문하지 않았다면 -1, -1이 아닌 숫자인 경우, 방문한 시각을 표시

dx = [-1, 1, k]
def bfs():
    queue = deque([(0, 0)]) # [위치, 줄]
    visited[0][0] = 0
    success = 0
    
    while queue:
        
        x, line = queue.popleft()
            
        for i in range(3):
            nx = x + dx[i]
            time = visited[line][x] + 1
            
            if nx >= n: # 성공하면 종료
                return 1
            
            if i == 2:
                # 이동하려는 칸이 사라지지 않았고, 안전한 칸이라면
                if time <= nx < n and graph[int(not line)][nx] and visited[int(not line)][nx] == -1: # 주의) visited[][] == -1 임!! visited[][] != -1이 아님!!!
                        queue.append((nx, int(not line))) # line 변경
                        visited[int(not line)][nx] = time
            else:
                # 이동하려는 칸이 사라지지 않았고, 안전한 칸이라면
                if time <= nx < n and graph[line][nx] and visited[line][nx] == -1: 
                    queue.append((nx, line))
                    visited[line][nx] = time
            
        # time += 1  # >> 이러면 예를 들어 3초일때 방문하게되는칸 여럿일 수 있는데, 시간은 더 빠르게 흐름
        
    return success

print(bfs())

# 안전한 칸(1) - 이동 가능, 위험한 칸(0) - 이동 불가
# 매초 마다 3가지 중 1가지 행동을 함
# 1. 한칸 옆으로 이동
# 2. 한칸 뒤로 이동
# 3. 반대편 줄로 이동, 원래 있던 칸 + k칸 앞으로 이동

# 매초마다 각 줄의 첫 칸이 사라짐
# 유저먼저 움직이고 칸 사라짐

# 게임 클리어 할 수 있는지 없는지 출력

# 맨 처음에는 왼쪽 1번칸 위치

# 주의!!!
# >> 매초마다 무언가의 값을 +1해라 -> 위치 조심!!!

# visited의 값을 어떤 것을 나타내도록 할지

# visited 검사를 안해도된다고 생각했는데 해야하는구나


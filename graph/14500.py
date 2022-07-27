from multiprocessing.connection import answer_challenge
import sys
input = sys.stdin.readline

def dfs(x, y, idx, total):
    global answer
    # 가지치기 - answer(현재까지의 4개 합 최대)가 현재까지 더한 total에 나머지 칸들이 최대라고 생각했을 때의 값 보다크면,
    # >> answer > 현재 만들 수 있는 최댓값
    # >> 더이상의 진행은 무의미
    if answer >= total + max_val * (3 - idx):
        return
    
    # 4개의 블럭 값을 모두 더했을 때
    if idx == 3:
        answer = max(answer, total)
    
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
                if idx == 1: # 2칸 째 칠할때, ㅓ ㅜ ㅗ ㅏ 모양 만들기 위함
                    visit[nx][ny] = 1
                    dfs(x, y, idx + 1, total + arr[nx][ny])
                    visit[nx][ny] = 0
                visit[nx][ny] = 1
                dfs(nx, ny, idx + 1, total + arr[nx][ny])
                visit[nx][ny] = 0
                
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [([0] * m) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0
max_val = max(map(max, arr))
# map(max, arr) : max함수를 arr 각 원소에 적용 - arr 각 열의 max 추출
# max(map(max, arr)) : 각 열의 max값들 중 max 값 추출 - 2차원 배열 속 max 값

for x in range(n):
    for y in range(m):
        visit[x][y] = 1
        dfs(x, y, 0, arr[x][y])
        visit[x][y] = 0

print(answer)

# >> dfs, bfs를 너무 반복해야할 것 같을 때 => 한번의 dfs, bfs만으로 모든 경우를 계산할 수 있을까 생각
# -> 2206번 벽 부수고 이동하기 때랑 비슷한 느낌

# idea
# 특정 좌표로 부터 dfs를 거리 3까지만 돌면 모든 테트로미노 모양을 만들 수 있음
# + 미리 컷하는 가지치기

# 어렵다,,
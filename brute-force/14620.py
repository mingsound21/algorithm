from pydoc import visiblename
import sys
input = sys.stdin.readline
from itertools import combinations

# 풀이 1. 조합 사용
# 꽃을 피울 15평의 좌표 정하기
# 최악의 경우 : n = 10 >> 64 C 3 = 41664 (조합 사용하기 적당)

def check(li):
    global answer
    visited = [] # 꽃잎이 서로 닿지 않는지 확인
    total = 0 # 대여비용의 합
    for r, c in li: # li에는 (r, c) 3개가 들어있음
        visited.append((r, c)) # 꽃의 중앙좌표를 먼저 담음
        total += fields[r][c] # 꽃의 중앙 좌표의 대여비를 초기값으로 잡음
        for idx in range(4): # 중앙으로부터 인접한 4방향 칸을 확인
            nr = r + d[idx][0]
            nc = c + d[idx][1]
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                total += fields[nr][nc]
            else: # 꽃잎에 서로 닿게 되는 경우에는 해당 li는 탈락 >> check함수 종료
                return
    answer = min(answer, total) # 최솟값

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n = int(input())
answer = int(1e9)
fields = [list(map(int, input().split())) for _ in range(n)]
candidates = [(r, c) for r in range(1, n-1) for c in range(1, n-1)]

for li in combinations(candidates, 3):
    check(li)
print(answer)

# 풀이 2. dfs 이용
# 풀이 1. 조합은 꽃을 피울 수 있는 후보 좌표들을 미리 담아두어 진행, dfs는 차례대로 탐색
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def check(i, j , visited): # 중앙에서 4방면으로 꽃잎이 이미 자리 잡았는지 체크
    for idx in range(4):
        ni = i + d[idx][0]
        nj = j + d[idx][1]
        if (ni, nj) in visited:
            return False
    return True

def dfs(visited, total):
    global answer
    if total >= answer : return # 시간 절약을 위해서 이미 total이 지금까지의 최솟값보다 크다면 종료
    if len(visited) == 15:
        answer = min(answer, total)
    else:
        for i in range(1, n-1):
            for j in range(1, n-1):
                if check(i, j, visited) and (i, j) not in visited: # 중앙과 4방면으로 visited하지 않았다면
                    temp = [(i, j)]
                    temp_cost = fields[i][j]
                    for idx in range(4):
                        ni = i + d[idx][0]
                        nj = j + d[idx][1]
                        temp.append((ni, nj))
                        temp_cost += fields[ni][nj]
                    dfs(visited + temp, total + temp_cost)

n = int(input())
answer = int(1e9)
fields = [list(map(int, input().split())) for _ in range(n)]
dfs([], 0)

print(answer)

# 다른 꽃잎과 닿게 되거나, 화단밖에 핀것은 죽음
# 화단의 대여가격은 격자마다 다름
# 세개의 씨앗이 모두 피게하면서, 싼 가격(꽃 하나당 5개 땅 구입)


# 연구소, 치킨배달, 감시피하기 문제와 유사...

# 어렵다.... 위 풀이는 https://velog.io/@djagmlrhks3/Algorithm-BaekJoon-14620.-%EA%BD%83%EA%B8%B8-by-Python 참고
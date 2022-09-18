import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
# 딕셔너리 사용!
ladder = {}
snake = {}
for i in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
    
for i in range(m):
    a, b = map(int, input().split())
    snake[a] = b

visited = [0] * 101
def bfs():
    queue = deque([1])
    visited[1] = 1
    
    while queue:
        x = queue.popleft()
        if x == 100:
            break
        
        for i in range(1, 7):
            nx = x + i
            if nx > 100:
                continue
            
            if nx in ladder.keys():
                nx = ladder[nx]
            elif nx in snake.keys():
                nx = snake[nx]
                
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[x] + 1


bfs()
        
print(visited[100]-1)

# 주사위 1-6
# 보드판 : 100칸, 1~100까지수가 하나씩 순서대로 적혀져있음
# 100번 칸 넘어가면 이동불가
# 사다리면 사다리타고 위로 올라감 (값 커짐)
# 뱀이면 뱀 따라서 내려감 (값 작아짐)
# 1번 칸에서 시작해 100번칸에 도착하기 위해서 주사위를 굴려야하는 횟수의 최솟값 구하시오

# 비슷한 문제 : 14226번 (사다리와 뱀을 딕셔너리로 받는다는 점)

# dp, bfs 차이
# dp : 큰 문제를 풀기 위해서 작은 문제들의 결괏값 사용, 메모제이션된 전의 계산결과를 사용
# bfs : 같은 레벨 노드 전부 탐색해, 가능한 수를 모두 계산하고 원하는 결과를 찾음

# bfs를 적용하기 위해서는,,
# 1) 문제를 그래프로 표현 가능해야함
# 2) 그래프 간선의 비용이 모두 동일해야함
# 3) 어떤 노드에 방문했을때, 해당 노드까지의 경로가 최적화된 값이 어야함

# dp를 적용하기 위해서는,,
# 문제를 그래프로 모델링 했을때, 그래프가 DAG일때 dp 적용가능(즉, 사이클 발생하면 X)

# 참고 https://onlyhim.tistory.com/22

# dp, bfs 구분 참고문제 : 1600, 2206, 1697, 1520
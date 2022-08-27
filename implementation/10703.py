import sys
input = sys.stdin.readline


n, m = map(int, input().split())
data = [input().rstrip() for _ in range(n)]
stone = [-3333] * m # 유성의 가장 낮은 위치
ground = [-1] * m # 땅의 가장 높은 위치
result = [['.'] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] == 'X':
            stone[j] = i
        if data[i][j] == '#' and ground[j] == -1:
            ground[j] = i

min_diff = min((j-i for i, j in zip(stone, ground))) -1

for i in range(n):
    for j in range(m):
        if data[i][j] == 'X':
            result[i+min_diff][j] = 'X'
        if data[i][j] == '#':
            result[i][j] = '#'
# print(">>>>>>>>>>>>>>>>>>>>>")
for r in result:
    print("".join(r))

# 문제 풀기
# X : 유성의 일부, # : 땅의 일부, . : 나머지
# 유성이 떨어지고 난 뒤의 사진을 복구해라

# 각 세로의 가장 아래 있는게 땅에 닿을때까지만 떨어질 수 있음

# 세로로 아래부터 위까지 돌면서 diff만큼 내리기 (맨 윗줄은 .으로 채우기)


# 틀렸던 이유>>
# 처음에는 stone의 초기값을 -1로 설정했더니 min_diff를 계산할때 
# ground - (-1) 이 가장 최소값으로 계산되는 오류가 있었나보다


# 파이썬 문법
# zip : 순회가능한 객체를 인자로 받고, 
# 각 객체가 담고 있는 원소를 튜플의 형태로 차례로 접근할 수 있는 반복자 반환
'''
numbers = [1, 2, 3]
letters= ["A", "B", "C"]
for pair in zip(numbers, letters):
    print(pair)

결과 >> 
(1, 'A')
(2, 'B')
(3, 'C')
'''

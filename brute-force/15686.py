import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
chicken = []
data = [list(map(int, input().split())) for _ in range(n)]

# 모든 치킨집 위치 chicken배열에 저장
for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chicken.append((i, j))
            
answer = 1e9
for li in list(combinations(chicken, m)): # 모든 치킨집중에서 m개를 뽑은 조합중에서
    total = 0
    for i in range(n): # 모든 그래프위치를 확인해서
        for j in range(n):
            if data[i][j] == 1: # 집이면
                _min = 1000
                for x, y in li: # 집으로부터 치킨집까지의 거리중에서 가장 작은것을 구해서
                    _min = min(_min, abs(i-x) + abs(j-y))
                total += _min # total에 더함
    answer = min(answer, total) # answer는 모든 도시 치킨 거리 중에서 가장 작은 값

print(answer)

    
# 각칸은 빈칸 0, 치킨집 2, 집 1 중 하나
# r, c는 1부터 시작
# 치킨 거리 = 집과 가장 가까운 치킨집 사이 거리
# 도시 치킨 거리 = 모든 집의 치킨 거리의 합
# 최소의 치킨 거리를 만드는 m개의 치킨 집 고르기

# 최대 : 1716*(13C6) * 100 * 13 >> brute force


# 다른 사람 풀이 - 거의 유사함
n, m = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(n))
result = 1e9
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])

for li in combinations(chicken, m):
    temp = 0
    for h in house:
        chi_len = 999
        for j in range(m):
            chi_len = min(chi_len, abs(h[0] -li[j][0] + abs(h[1] - li[j][1])))
        temp += chi_len
    result = min(result, temp)

print(result)



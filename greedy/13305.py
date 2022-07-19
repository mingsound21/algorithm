import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
oil = list(map(int, input().split()))

cheap = oil[0]
roadSum = 0
answer = 0
for i in range(len(oil)-1):
    if(oil[i]>=cheap):
        roadSum += road[i]
    else: # 더 싼 oil 값 발견
        answer += roadSum * cheap
        cheap = oil[i]
        roadSum = road[i]

answer += roadSum * cheap# 마지막
print(answer)

# 최소 기름값
# 기름 값 배열을 순회하면서 
# 더 작은 기름값이 나올때까지 road 거리 더하기
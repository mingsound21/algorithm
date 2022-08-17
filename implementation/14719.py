import sys
input = sys.stdin.readline().rstrip

# 풀이 1)
h, w = map(int, input())
data = list(map(int, input().split()))

answer = 0
for i in range(1, w-1):
    # 현재 idx의 좌, 우에서 가장 높은 기둥 높이 찾기
    left_max = max(data[:i])
    right_max = max(data[i+1:])

    # 좌, 우 중 더 낮은 높이 찾기
    lower_max = min(left_max, right_max)
    
    # 현재 기둥 높이가 좌, 우 중 더 낮은 높이 보다 작으면 물이 고임
    if data[i] < lower_max:
        answer += lower_max - data[i]
        
print(answer)

# 풀이 2)
h, w = map(int, input())
data = list(map(int, input().split()))

maxH = 0
maxIdx = 0
# 최대 높이인 index를 찾기
for i in range(len(data)):
    if maxH < data[i]:
        maxH = data[i]
        maxIdx = i
        
# 왼쪽부터 최대 높이까지 검사하면서, 물이 고였을때의 총 높이 저장
total = 0
temp = 0
for i in range(maxIdx + 1):
    if data[i] > temp:
        temp = data[i]
    total += temp
    
# 오른쪽 부터 최대 높이전까지 검사하면서, 물이 고였을때의 총 높이 저장
total = 0
temp = 0
for i in range(w-1, maxIdx, -1):
    if data[i] > temp:
        temp = data[i]
    total += temp
    
# 물이 고였을때의 총 높이 - 기둥 높이
print(total - sum(data))
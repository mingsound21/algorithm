import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())
data = [[1], [1, 1]]
for i in range(2, r + w):
    arr = [1]
    for j in range(1, i-1):
        arr.append(data[i-1][j-1]+data[i-1][j])
    arr.append(1)
    data.append(arr)


answer = 0
row = 1
for i in range(r, r+w):
    for j in range(c-1, c-1+row):
        answer += data[i][j]
    row += 1

print(answer)
        

# r번째 줄 c번째 수를 위 꼭짓점으로 하는 한 변이 포함하는 수의 개수가 w개인 정삼각형의 내부에 있는 수의 합

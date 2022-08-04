import sys
input = sys.stdin.readline

n = int(input())
graph = []

class_graph = [[0] * n for _ in range(n)]

for _ in range(n**2):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for arr in graph:
    arr2 = []
    
    student = arr[0]
    fav = arr[1:]
    
    
    
    for x in range(n):
        for y in range(n):
            if class_graph[x][y] != 0:
                continue
            empty = 0
            fav_fr = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<= nx < n and 0 <= ny < n:
                    if class_graph[nx][ny] == 0:
                        empty += 1
                    if class_graph[nx][ny] in fav:
                        fav_fr += 1
            arr2.append((fav_fr, empty, x, y))
    arr2.sort(key = lambda x : (x[0], x[1], -x[2], -x[3]))

    px = arr2[-1][2]
    py = arr2[-1][3]
    
    class_graph[px][py] =  student
    
answer = 0
graph.sort(key = lambda x : (x[0]))
score = [0, 1, 10, 100, 1000]
for x in range(n):
    for y in range(n):
        cnt = 0
        student = class_graph[x][y]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if class_graph[nx][ny] in graph[student-1][1:]:
                    cnt += 1
        answer += score[cnt]

print(answer)
    



# 학생 최대 20명 -> 400 * 20 = 8000
# 각 칸 모두 돌면서 비어 있는 칸이면 배열에 (인접한 좋아하는 학생수, 인접한 비어 있는 칸 수, x, y) => sort lambda 사용해서 정렬한뒤 첫번째꺼 꺼내기

'''
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
'''
# 인접 = 상하좌우

'''
Tip)

arr : 2차원 배열
>> 2차원 배열의 각 원소 속의 원소 값을 가지고 정렬을 하고 싶을 때
>> 여러개의 우선순위를 가지고 배열을 정렬하고 싶을 때
arr.sort(key = lambda x : (x[0], x[1], -x[2], -x[3]))
'''

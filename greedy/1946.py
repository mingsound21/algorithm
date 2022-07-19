import sys
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    score = []
    for i in range(n):
        score.append(list(map(int, input().split())))
    arr = sorted(score, key = lambda x : x[0])
    
    cnt = 1
    rank = arr[0][1]
    for i in range(1, n):
        if(arr[i][1] < rank):
            cnt += 1
            rank = arr[i][1]
    print(cnt)
        
# 서류 심사 / 면접 성적 모두 떨어지면 선발 X
# 최대 신입 사원 채용 인원 수
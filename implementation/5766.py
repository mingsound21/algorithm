import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    d = {}
    for i in range(n):
        for a in list(map(int, input().split())):
            if a not in d.keys(): # keys 대신 list(d.keys()) 사용했을때는 시간 초과, key in d.keys()는 시간 복잡도 O(1)
                d[a] = 1
            else:
                d[a] += 1
    result = sorted(d.items(), key = lambda x : x[1], reverse=True)
    score_2 = result[1][1]
    answer = []
    for i in range(1, len(result)):
        if result[i][1] == score_2:
            answer.append(result[i][0])
    answer.sort()
    for a in answer:
        print(a, end = " ")
    print()

        
# 딕셔너리 sort
# sorted(dictionary.items()) : 딕셔너리 key값 순으로 정렬하고 (키, 값) 리스트
# sorted(dictionary) : 딕셔너리의 key만 빠져서 리스트
# sorted(dictionary.items(), key = lambda x : x[1])
# 내림차순은 sorted(list, reverse=True)

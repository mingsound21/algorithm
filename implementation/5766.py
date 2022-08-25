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


# 다른 사람 풀이
while True:
    player = [[0, i] for i in range(10001)]
    n, m = map(int, input().split())
    if not n and not m:
        break
    for _ in range(n):
        for a in map(int, input().split()):
            player[a][0] += 1
    player.sort(key=lambda x : [-x[0], +x[1]]) # 점수는 내림차순, 점수가 같다면 사람 번호는 오름차순으로 정렬
    second_score = player[1][0]
    second_place = [player[1][1]]
    for i in range(2, 10001):
        if player[i][0] == second_score:
            second_place.append(player[i][1])
        else:
            break
    print(*second_place) # list안의 모든 값들을 사이사이 공백과 함께 출력
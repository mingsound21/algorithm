import sys
input = sys.stdin.readline
a = 'A'
check = [0] * 26

n = int(input())
data = []
for _ in range(n):
    word = list(input().rstrip().split())
    check1 = 0
    for i in range(len(word)):
        temp = ord(word[i][0].upper()) - ord('A')
        if not check[temp]:
            check[temp] = 1
            word[i] = '[' + word[i][0] + ']' + word[i][1:]
            check1 = 1
            break
    if check1 != 1:
        check2 = 0
        for i in range(len(word)):
            for j in range(len(word[i])):
                temp = ord(word[i][j].upper()) - ord('A')
                if not check[temp]:
                    check[temp] = 1
                    word[i] = word[i][:j] + '[' + word[i][j] + ']' + word[i][j+1:]
                    check2 = 1
                    break
            if check2 == 1:
                break
    print(" ".join(word))

# +++ 주의 +++
# for w in word:
#     w = '[' + w + ']' 
# >> w를 변경한다고 해서 word 배열의 요소의 값이 변경되지는 않음

# 1. 각 단어 첫글자 살펴보기
# 2. 왼쪽 부터 차례대로 알파벳 보면서 단축키 지정 안된게 있으면 지정
# 대소문자 구별 X
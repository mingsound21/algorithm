import sys
input = sys.stdin.readline

n, k = map(int, input().split())
course = list(map(int, input().split()))

sum = 0
if k == 0:
    print(1)
    exit(0)
    
for i in range(n):
    sum += course[i]
    if k < sum:
        print(i+1)
        exit(0)
    elif k == sum:
        print(i+2)
        exit(0)

for i in range(n-1, -1, -1):
    sum += course[i]
    if k < sum:
        print(i+1)
        exit(0)
    elif k == sum:
        print(i-2)
        exit(0)

# n = 10만이라서 O(n) 한번 쭉 도는건 시간복잡도상 괜찮을거라 생각...

# 다른 사람 풀이)
for i in range(n):
    k -= course[i]
    if k < 0: # k == 0 이면 다음 코스를 출력해야하기 때문
        print(i+1)
        break
else:
    for i in range(n-1,-1,-1):
        k -= course[i]
        if k < 0:
            print(i+1)
            break

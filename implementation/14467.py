import sys
input = sys.stdin.readline

cow_arr = [[] for _ in range(11)]
cnt = 0

for i in range(int(input())):
    cow, place = map(int, input().split())
    
    if len(cow_arr[cow])==0: # 비어있으면
        cow_arr[cow].append(place)
    elif cow_arr[cow][0] != place:
        cow_arr[cow][0] = place
        cnt += 1

print(cnt)
        

# 이전에 있던 장소와 다르면 길 건넌 것
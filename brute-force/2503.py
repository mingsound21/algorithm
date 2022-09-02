import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
num = list(permutations([i for i in range(1, 10)], 3)) # 가능한 모든 경우의 수

for _ in range(n):
    test, s, b = map(int, input().split())
    test = list(str(test))
    remove_cnt = 0
    
    for i in range(len(num)):
        s_cnt = b_cnt = 0
        i -= remove_cnt # 계속 삭제하니까 index 바뀌어서
        
        for j in range(3):
            test[j] = int(test[j])
            if test[j] in num[i]:
                if j == num[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        
        if s_cnt != s or b_cnt != b:
            num.remove(num[i])
            remove_cnt += 1
        
print(len(num))
from platform import java_ver
import sys
input = sys.stdin.readline

def nextPermutation(arr):
    # 1. 맨 뒤에서 부터 비교해 앞에 것이 더 작은 곳을 i로 정함
    i = len(arr)-2
    while i>=0 and arr[i] >= arr[i+1]:
        i -= 1
    # 더 작은 것이 없다면 false
    if i == -1:
        return False
    
    # 맨 뒤에서 부터 i 보다 큰 값을 찾아 j로 정함
    j = len(arr)-1
    while arr[i] >= arr[j]:
        j -= 1
        
    # i, j서로 변경
    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i+1]
    
    # i뒤에 있는 것들을 뒤집어줌
    result.extend(list(reversed(arr[i+1:])))
    return result
    
    
t = int(input())
for _ in range(t):
    _input = list(input().rstrip())
    answer = nextPermutation(_input())
    
    if not answer:
        print("".join(_input()))
    else:
        print("".join(answer))
        
# ++ 문제 ++ 
# 주어진 단어를 사전 순으로 정렬, 주어진 단어 다음에 나오는 단어 찾기


# idea 
# 사전순 -> 숫자 정렬

# 첫 시도 : permutation -> set(중복 삭제) -> sort 
# >> 메모리 초과, 시간 초과

# 다른 사람의 정답 풀이
# c++에는 있는 next_permutation 알고리즘을 사용.
# 그냥 바로 다음 순서의 값을 도출
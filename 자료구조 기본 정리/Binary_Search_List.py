# 이진 탐색
#>> 찾으려는 ㄷ터와 중간점 위치에 있는 데이터를 반복적으로 비교해, 탐색 범위를 계속 절반으로 줄여감

# point
# 1. 시간 복잡도: O(logN)
# 2. 정렬된 데이터에 대해서 사용
# 3. 탐색 범위가 2000만을 넘어가면 이진탐색으로 문제에 접근해보기
# 처리할 데이터의 개수가 1000만 단위 이상으로 넘어가면 이진 탐색과 같이 O(logN)속도를 내야하는 알고리즘 떠올려야 할 수 있음

# --------------------------------------------------------------------------------------
# 1. 재귀 함수

def binary_search(array, target, start, end):
    if start > end :
        return None
    
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
n, target = list(map(int,input().split()))

array = sorted(list(map(int, input().split())))
# array = list(map(int, input().split())).sort() # >> 결과 None으로 나옴

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)
    
# 2. 반복문

def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
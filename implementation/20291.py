import sys
input = sys.stdin.readline

n = int(input())
file = {}

for _ in range(n):
    data = list(input().rstrip().split("."))
    if file.get(data[1]) is None:
        file[data[1]] = 1
    else:
        file[data[1]] += 1

file_sort = sorted(file.items())
for name, cnt in file_sort:
    print(name, cnt)
    

# arr = {"red" : 1, "blue" : 2}
# print(arr.keys())
# print(arr.values())

# 문법)
# [sorted] VS [sort]
# sorted - 모든 iterable한 객체
# sort - 리스트
#-----------------------------------------------------------------------------------------------------

# 딕셔너리 정렬 = sorted 
# >> sorted함수는 정렬이 완료된 새로운 "리스트"반환 (나중에 dict함수를 통해서 다시 딕셔너리로 변환)

# 1. Key만 정렬해서 Key만 반환
# >> sorted(dict)
# >> 딕셔너리 객체 자체를 넣게 되면 딕셔너리의 key만 빠져서 리스트됨

# 2. Key 기준 정렬
# >> sorted(dict.items()) 
# >> [(key, value), (key, value), ...] 

# 3. Value 기준 정렬
# >> sorted(dict.items(), key = lambda x : x[1])

#-----------------------------------------------------------------------------------------------------

# 딕셔너리 함수
# 1. Key만 반환
# dict.keys() - 반환type dict_keys

# 2. Value만 반환
# dict.values() - 반환type dict_values 

# 3. key-value 쌍 반환
# dict.items() - 반환type [()]

# 4. key로 value 얻기
# dict.get('키')
# >> 키가 존재하면 값을 반환, 없다면 NoneType을 반환 (키 유무 판별에 사용)

# 5. key 값 존재 유무 확인
# 키 in dict - 반환type bool
# >> 키가 존재하면 True, 없으면 False
# >> 딕셔너리에서 in으로 원소 확인시에는 key를 기준으로 훑는다

# 6. 딕셔너리 생성
# dict = {} 
# dict.clear()

#-----------------------------------------------------------------------------------------------------

# <문제>
# 확장자별 파일 개수
# 확장자 이름의 사전 순으로 출력
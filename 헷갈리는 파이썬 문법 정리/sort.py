# 1. sort VS sorted
# --- sort --- 
# return None
# 원래의 함수를 정렬시킴
# 리스트만 정렬 가능

# --- sorted ---
# 정렬시킨 리스트를 리턴
# 원래의 함수에는 아무런 영향이 없음
# 문자열, 튜플, 딕셔너리 등 "반복가능한 객체"를 정렬

data = [('a', 100), ('b', 30), ('c', 60)]
# 2. key = lambda
print(sorted(data)) # [('a', 100), ('b', 30), ('c', 60)]
print(sorted(data, key = lambda x : x[1])) # [('b', 30), ('c', 60), ('a', 100)]

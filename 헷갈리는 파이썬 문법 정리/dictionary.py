# 딕셔너리의 key값은 중복 X

# +++++ 추출 +++++
d = {'a' : 3, 'b' : 5, 'c' : 100}

# key 추출
print(d.keys()) # dict_keys(['a', 'b', 'c'])
print('a' in d.keys()) # True O(1)
print('a' in d) # 위와 같이 key안에 'a'가 있는지 확인함
print('f' in d.keys()) # False O(1)

# value 추출
print(d.values()) # dict_values([3, 5, 100])
print(3 in d.values()) # True O(1)
print(40 in d.values()) # False O(1)

# 키-값 쌍 추출
print(d.items()) #dict_items([('a', 3), ('b', 5), ('c', 100)])


# +++++ 정렬 +++++
d2 = {'z' : 40, 'y' : 5, 'x' : 100}

#--- key ---
# key 기준 오름차순 정렬
print(sorted(d2.items())) # [('x', 100), ('y', 5), ('z', 40)]
# key 기준 내림차순 정렬
print(sorted(d2.items(), reverse=True)) # [('z', 40), ('y', 5), ('x', 100)]
# key값들만 빼서 오름차순 정렬
print(sorted(d2)) # ['x', 'y', 'z']

#--- value ---
# value 기준 오름차순 정렬
print(sorted(d2.items(), key = lambda x : x[1])) # [('y', 5), ('z', 40), ('x', 100)]
# value 기준 내림차순 정렬
print(sorted(d2.items(), key = lambda x : x[1], reverse=True)) # [('x', 100), ('z', 40), ('y', 5)]


# +++++ 기본 함수 +++++
d3 = {}
# 추가
d3['a'] = 1
print(d3)

# 삭제 
del d3['a']
print(d3)

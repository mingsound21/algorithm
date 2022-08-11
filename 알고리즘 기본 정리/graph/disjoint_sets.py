# 서로소 집합 : 공통 원소가 없는 두 집합
# 서로소 집합 자료구조 : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
# 연산 : union, find
# 서로소 집합 자료구조 구현시 "트리 자료구조"사용해 집합 표현
# ------------------------------------------------------------------------------------

# 1. union 연산을 확인해, 서로 연결된 두 노드 A, B를 확인
# 2. A, B의 루트 노드 A', B'을 찾음
# 3. A'을 B'의 부모 노드로 설정
# ------------------------------------------------------------------------------------

# find bad version을 경로 압축 기법을 사용해 최적화 가능
# bad version은 최악의 경우 find 함수 시간 복잡도 : O(V)
def find_parent_bad_version(parent, x):
    if parent[x] != x:
        return find_parent_bad_version(parent, parent[x])
    return x

# bad version과의 차이점 : find 함수를 실행하면서 아예 parent[x]의 값을 갱신
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
# 노드 개수, 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블초기화

# 부모 테이블에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end = '')
for i in range(1, v + 1):
    print(find_parent(parent, i), end = " ")
    

print("부모 테이블: ", end = "")
for i in range(1, v + 1):
    print(parent[i], end = " ")

# ------------------------------------------------------------------------------------
# 서로소 집합은 "무방향 그래프" 내 사이클 판별에 사용 가능

# 1. 각 간선을 확인하며 두 노드의 루트 노드를 확인
# 2 -1. 루트 노드가 서로 다르면 두 노드에 대해서 union 연산 수행
# 2 -2. 루트 노드가 서로 같으면 사이클 발생!!
# 그래프에 포함된 모든 간선에 대해서 위의 과정을 반복

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
v, e = map(int, input().split())
parent = [0] * (v + 1)

for i in range(1, v + 1):
    parent[i] = i
    
cycle = False

for i in range(e):
    a, b = map(int, input().split())
    
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)
        
if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")
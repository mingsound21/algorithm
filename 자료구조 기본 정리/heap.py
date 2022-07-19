import heapq 

heap = [] # deafault _ min heap

# 추가 _ heapq.heappush(heap, item)
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap) # [10, 50, 20]

# 삭제 _ heapq.heappop(heap)
print(heapq.heappop(heap)) # 10
print(heap) # [20, 50]
print(heapq.heappop(heap)) # 20
print(heap) # [50]



# 리스트를 heap으로 즉각 변환 _ heapq.heapify(list) : O(N)
heap2 = [40, 10, 30]
heapq.heapify(heap2)

print(heap2) # [10, 40, 30]

# *** 삭제하지 않고 접근만 하려면 인덱싱 통해서
print(heap2[0]) # 10
print(heap2) # [10, 40, 30]


# < max heap >
heap_items = [1, 3, 5, 7, 9]

max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item)) # 튜플의 첫번 째 원소를 우선순위로 힙 구성
    
print(max_heap) # [(-9, 9), (-7, 7), (-3, 3), (-1, 1), (-5, 5)]

# 최대 값 pop
# 반환된 튜플의 두번째자리에 실제 원소 값이 있음
max_item = heapq.heappop(max_heap)[1] # 9

# 특정한 규칙을 가지는 트리
# 최대, 최솟값을 빠르게 찾기 위해 고안된 완전 이진 트리를 기본으로 함

# min heap (최소힙) : 부모 노드의 key 값 < 자식 노드의 key 값
# max heap (최대힙) : 부모 노드의 key 값 > 자식 노드의 key 값

# key값의 대소관계는 부모-자식 간에만 성립
# 형제 노드 사이에는 대소관계 X
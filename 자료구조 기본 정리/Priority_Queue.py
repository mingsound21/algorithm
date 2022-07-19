from queue import PriorityQueue

que = PriorityQueue()
que = PriorityQueue(maxsize=4) # 크기 제한 가능

#원소 추가 _ put() : O(logn)
que.put(5)
que.put(3)
que.put(1)

print(que)

# 원소 삭제 _ get() : O(logn)
print(que.get()) # 1
print(que) 

# 정렬 기준 변경 _ (우선순위, 값)의 튜플 형태로 추가/제거
que2 = PriorityQueue()

que2.put((3, 'Apple'))
que2.put((1, 'Banana'))
que2.put((2, 'Cherry'))

print(que2.get()[1]) # Banana
print(que2.get()[1]) # Cherry
print(que2.get()[1]) # Apple

# 큐/스택과 유사하나, 각 원소들이 우선순위를 가짐
# 제거시 가장 작은 값 제거 
# 내부적으로 데이터 정렬된 상태로 보관
# heapq 모듈 사용

# 우선순위 큐는 힙 자료구조로 구현

# heap
# 완전 이진 트리
# 부모 노드의 값이 항상 자식 노드들의 값보다 크거나 작아야함
# 루트 노드의 값이 최대혹은 최소값
# 우선순위 큐, 힙 정렬 구현시 사용
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(start):
    queue = deque([{'graph' : [start-1, start+1, 2*start] , 'depth' : 0}])
    
    while queue:
        dic = queue.popleft()
        if k in dic['graph']:
            return dic['depth'] + 1
        
        for value in dic['graph']:
            queue.append({'graph' : [value-1, value+1, 2*value], 'depth': dic['depth']+1})

        
print(bfs(n))

# depth를 위해 생각한 방법
# 1) 각 depth의 마지막 노드 다음에 0을 넣기 _ 실패
# 2) 딕셔너리 사용
        
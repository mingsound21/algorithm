import sys
input = sys.stdin.readline

k = int(input())
way = list(map(int, input().split()))
tree = [[] for _ in range(k)] # 각 높이마다 배열 생성

# arr = 서브트리, x = 현재 깊이
def makeTree(arr, x):
    mid = (len(arr)//2)
    tree[x].append(arr[mid])
    if len(arr) == 1: # 리프노드
        return
    makeTree(arr[:mid], x + 1) # 왼쪽 먼저 
    makeTree(arr[mid+1:], x + 1)
    
makeTree(way, 0)
for i in range(k):
    print(*tree[i])

# 문제 읽었을 땐, 중위 순회(왼 중 오)
# 마지막 레벨을 제외한 모든 집은 왼쪽 자식과 오른쪽 자식을 갖는다.
# i번째 줄에는 레벨이 i인 빌딩의 번호 출력

# 문제 풀이
# 입력된 배열의 중간값이 루트, 루트 기준으로 왼쪽 서브루트, 오른쪽 서브루트로 나눌 수 있음
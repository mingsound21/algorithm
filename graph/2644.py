import sys
input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [0 for _ in range(n+1)]
for i in range(m):
    p, c = map(int, input().split())
    graph[c] = p
    
# print(graph) #

def dfs(v, pArr):
    pArr.append(v)
    if graph[v] == 0:
        return pArr
    return dfs(graph[v], pArr)
p1Arr = dfs(p1, [])
p2Arr = dfs(p2, [])

# print(p1Arr)
# print(p2Arr)

answer = -1
for i in range(len(p1Arr)):
    if p1Arr[i]  in p2Arr:
        answer = i +  p2Arr.index(p1Arr[i])
        break
print(answer)
    
# x : 부모, y : 자식
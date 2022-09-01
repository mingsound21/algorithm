import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = [list(input().rstrip()) for _ in range(n)]

# A, T, G, C
dna = ['A', 'C', 'G', 'T'] # 사전순이라서
result = ''
result_hd = 0
for j in range(m):
    arr = [0]*4
    for i in range(n):
        if data[i][j] == 'A':
            arr[0] += 1
        elif data[i][j] == 'C':
            arr[1] += 1
        elif data[i][j] == 'G':
            arr[2] += 1
        else:
            arr[3] += 1
    _max = max(arr)
    
    result_hd += (n - _max)
    result += dna[arr.index(_max)]

print("".join(result))
print(result_hd)
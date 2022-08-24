import sys
input = sys.stdin.readline

word = list(input().rstrip())
result = [''] * len(word)

def func(arr, start):
    if not arr: # 빈 배열이면 종료
        return
    
    _min = min(arr) # arr에서 사전순에서 가장 빠른 알파벳
    idx = arr.index(_min) # 해당 알파벳 인덱스
    result[start+idx] = _min
    print("".join(result))
    func(arr[idx+1:], start+idx+1)
    func(arr[:idx], start)
    
func(word, 0)



# 다른 사람 풀이
# print("".join(['a', "", "", "b"])) # ab 
# 재귀...

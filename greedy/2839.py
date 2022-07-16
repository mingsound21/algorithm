import sys
input = sys.stdin.readline

N = int(input())

bag = 5000 # 초기값

for i in range(N//5+1):
    n = N
    
    newbag = i
    n-=(5*i)
    
    if(n%3!=0):
        continue
    
    newbag += (n//3)
    
    if(newbag<bag):
        bag = newbag
        
if(bag == 5000):
    bag = -1

print(bag)
    
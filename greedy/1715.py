import heapq
from random import sample
import sys
input = sys.stdin.readline

n = int(input())
card_deck = []
for _ in range(n):
    heapq.heappush(card_deck, int(input()))
    
if len(card_deck) == 1: # 1개만 받는 예외 케이스 생각
    print(0)
else:
    answer = 0
    while len(card_deck) > 1 :
        small_1 = heapq.heappop(card_deck)
        small_2 = heapq.heappop(card_deck)
        answer += small_1 + small_2
        heapq.heappush(card_deck, small_1, small_2)
        
print(answer)

# 그리디 - 현재 상황에서 가장 작은 수 2개씩 묶어 나가야 가장 효율적
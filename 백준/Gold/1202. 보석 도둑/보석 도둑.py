import sys
from heapq import heappop, heappush, heapify

N, K = map(int, sys.stdin.readline().split())
stone = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    heappush(stone, (M, V))
cap = sorted([int(sys.stdin.readline()) for _ in range(K)])

ans = 0
candidate_stone = []
for c in cap:
    while stone and c >= stone[0][0]:
        m, v = heappop(stone)
        heappush(candidate_stone, -v)
    
    if candidate_stone:
        ans += - heappop(candidate_stone)

    
print(ans)
import sys
from heapq import heapify, heappush, heappop

N = int(sys.stdin.readline())
station = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
heapify(station)
l, p = map(int, sys.stdin.readline().split())

ans = 0
tmp = []
while p < l:
    while station and station[0][0] <= p:
        d, f = heappop(station)
        heappush(tmp, (-f, d))
    
    if tmp:
        f, d = heappop(tmp)
        p += -f
        ans += 1

    else:
        ans = -1
        break
print(ans) 
import sys
from heapq import heapify, heappop, heappush

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
heapify(nums)
if len(nums) == 1:
    print(0)

else:
    ans = 0
    while len(nums) > 1:
        tmp = heappop(nums) + heappop(nums)
        ans += tmp
        heappush(nums, tmp)
    print(ans)
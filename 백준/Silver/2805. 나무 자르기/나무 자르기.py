import sys
from collections import Counter
n,m = map(int, sys.stdin.readline().split())
t = Counter(map(int, sys.stdin.read().split()))

s = 1
e = max(t.items())[0]

while s<=e:
    mid = (s+e)//2
    tot = sum((h-mid)*i for h,i in t.items() if h>mid)

    if tot >= m:
        s = mid+1
    elif tot <m:
        # ans = mid
        e = mid-1

print(e)
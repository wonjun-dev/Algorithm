import sys

N, M = map(int, sys.stdin.readline().split())
T = [int(sys.stdin.readline()) for _ in range(N)]

s = min(T)
e = max(T) * M
ans = 0

while s <= e:
    mid = (s + e) // 2
    cnt = 0

    for t in T:
        cnt += mid // t
    
    if cnt >= M:
        e = mid - 1
        ans = mid
    else:
        s = mid + 1

print(ans)
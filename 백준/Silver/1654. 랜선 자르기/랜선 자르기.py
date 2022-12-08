import sys

K, N = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(K)]

s = 1
e = max(nums)

while s <= e:
    m = (s + e) // 2
    cnt = 0
    for n in nums:
        cnt += n // m

    if cnt < N:
        e = m - 1
    elif cnt >= N:
        s = m + 1

print(e) 
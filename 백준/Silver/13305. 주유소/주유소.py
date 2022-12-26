import sys

N = int(sys.stdin.readline())
dist = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

ans = 0
min_p = float('inf')
for i in range(N-1):
    min_p = min(min_p, price[i])
    ans += min_p * dist[i]

print(ans)
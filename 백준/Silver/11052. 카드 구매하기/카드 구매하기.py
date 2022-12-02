import sys

N = int(sys.stdin.readline())
price = [0] + list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * (N+1)
dp[1] = price[1]

if N >= 2:
    for i in range(2, N+1):
        tmp = []
        for j in range(1, i+1):
            tmp.append(dp[i-j] + price[j])
        dp[i] = max(tmp)

print(dp[N])
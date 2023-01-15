import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
dp = [0] * len(A)

for b in B:
    cnt = 0
    for idx, a in enumerate(A):
        if cnt < dp[idx]:
            cnt = dp[idx]
        elif b == a:
            dp[idx] = cnt + 1
print(max(dp))
import sys

A, B, V = map(int, sys.stdin.readline().split())

ans = (V - A) // (A - B)
if (V - A) % (A - B) == 0:
    ans += 1
else:
    ans += 2
print(ans)
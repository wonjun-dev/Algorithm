import sys

n, k = map(int, sys.stdin.readline().strip().split())
coin = sorted([int(sys.stdin.readline()) for _ in range(n)])

table = [0 for _ in range(k+1)]
table[0] = 1

for c in coin:
    for i in range(c, k+1):
        if i-c >= 0:
            table[i] = table[i] + table[i-c]

print(table[k])
import sys

N = int(sys.stdin.readline())
table = [0 for _ in range(N+1)]

if N == 1:
    print(1)

else:
    table[1], table[2] = 1, 3

    for i in range(3, N+1):
        table[i] = (table[i-1] + 2*table[i-2]) % 10007

    print(table[N] % 10007)


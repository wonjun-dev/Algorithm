import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    table = [(0, 0) for _ in range(N+1)]
    if N == 0:
        print(*(1, 0))
    elif N ==1:
        print(*(0, 1))
    else:
        table[0], table[1] = (1, 0), (0, 1) 

        for i in range(2, N+1):
            table[i] = (table[i-1][0] + table[i-2][0], table[i-1][1] + table[i-2][1])

        print(*table[N])
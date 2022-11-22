import sys

N = int(sys.stdin.readline())
tri = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
table = [0 for _ in range(N)]

if N == 1:
    print(tri[0][0])
else:
    i = 2
    for j in range(1, N):
        for k in range(i):
            if k == 0:
                tri[j][k] = tri[j-1][k] + tri[j][k]
            elif k == j:
                tri[j][k] = tri[j-1][k-1] + tri[j][k]
            else:
                tri[j][k] = tri[j][k] + max(tri[j-1][k-1], tri[j-1][k])
        i += 1
    print(max(tri[-1]))

import sys
from collections import defaultdict

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
G = defaultdict(list)

for _ in range(M):
    s, e, p = map(int, sys.stdin.readline().strip().split())
    G[s].append([e, p])

S, D = map(int, sys.stdin.readline().strip().split())
d = [float('inf') for _ in range(N+1)]
d[S] = 0
visit = [0 for _ in range(N+1)]
visit[0], visit[S] = 1, 1

start = S
f = lambda i: d[i]
while 0 in visit:
    for e, p in G[start]:
        if d[e] > p + d[start]:
            d[e] = p + d[start]
    
    start = min([i for i in range(N+1) if visit[i]==0], key=f)
    visit[start] = 1

print(d[D])
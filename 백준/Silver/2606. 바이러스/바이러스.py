import sys
from collections import deque, defaultdict

cm = int(sys.stdin.readline().strip())
nn = int(sys.stdin.readline().strip())

G = defaultdict(list)
for _ in range(nn):
    u, v  = map(int, sys.stdin.readline().strip().split())
    G[u].append(v)
    G[v].append(u)


q = deque()
vis = [0 for _ in range(cm+1)]
q.append(1)
vis[1] = 1

ans = 0
while q:
    u = q.popleft()
    for v in G[u]:
        if not vis[v]:
            q.append(v)
            vis[v] = 1
            ans += 1
print(ans)
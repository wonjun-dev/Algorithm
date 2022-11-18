import sys
from collections import defaultdict, deque

N, M, V = map(int, sys.stdin.readline().strip().split())

G = defaultdict(list)

for _ in range(M):
    n1, n2 = map(int, sys.stdin.readline().strip().split())
    G[n1].append(n2)
    G[n2].append(n1)

def dfs(G, start):
    for k, v in G.items():
        G[k] = sorted(v, reverse=True)

    s = list()
    visit = [False] + [False for _ in range(N)]
    s.append(start)
    ans = []

    while s:
        node = s.pop()
        if not visit[node]:
            visit[node] = True
            ans.append(node)

            for idx in G[node]:
                s.append(idx)
    
    return ans


def bfs(G, start):
    for k, v in G.items():
        G[k] = sorted(v)

    q = deque()
    visit = [False] + [False for _ in range(N)]
    visit[start] = True
    q.append(start)
    ans = [start]

    while q:
        node = q.popleft()
        for idx in G[node]:
            if not visit[idx]:
                visit[idx] = True
                q.append(idx)
                ans.append(idx)
    return ans
print(*dfs(G, V))
print(*bfs(G, V))
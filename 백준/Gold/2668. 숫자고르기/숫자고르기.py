import sys

N = int(sys.stdin.readline())
G = {i: int(sys.stdin.readline()) for i in range(1, N+1)}

def dfs(node, visit=[]):
    visit.append(node)

    if G[node]not in visit:
        dfs(G[node], visit)

    return visit


ans = []
for start in range(1, N+1):
    visit = dfs(start, visit=[])
    if G[visit[-1]] == start and start not in ans:
        ans += visit
    
print(len(ans))
for i in sorted(ans):
    print(i)
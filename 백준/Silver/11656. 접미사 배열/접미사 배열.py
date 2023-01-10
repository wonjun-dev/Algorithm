import sys

S = sys.stdin.readline().strip()

ans  = []
for i in range(len(S)):
    ans.append(S[i:])

for a in sorted(ans):
    print(a)
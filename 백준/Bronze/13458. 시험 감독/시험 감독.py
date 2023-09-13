import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

ans = []
for a in A:
    if a-B <= 0:
        ans.append(1)
        continue
    
    if (a-B) % C == 0:
        ans.append((a-B) // C + 1)
    else:
        ans.append((a-B) // C + 2)
print(sum(ans)) 
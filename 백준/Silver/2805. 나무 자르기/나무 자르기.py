import sys

N, M = map(int, sys.stdin.readline().strip().split())
tree = sorted(list(map(int, sys.stdin.readline().strip().split())))

s = 0
e = tree[-1]
h = (s + e) // 2

while True:
    cut = 0
    for t in tree:
        if t > h:
            cut += t - h 
    
    if cut > M:
        s = h
        h = (s + e) // 2
    elif cut < M:
        e = h
        h = (s + e) // 2
    else:
        break
    
    if h == e or h == s:
        break

print(h)
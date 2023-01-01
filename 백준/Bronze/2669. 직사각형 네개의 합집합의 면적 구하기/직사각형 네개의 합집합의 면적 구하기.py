import sys

rect = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
visit = []

cnt = 0
for r in rect:
    for x in range(r[0], r[2]):
        for y in range(r[1], r[3]):
            if (x, y) not in visit:
                visit.append((x, y))
                cnt += 1
print(cnt)
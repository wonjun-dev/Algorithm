import sys

rect = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
visit = [[0]*101 for _ in range(101)]  

for r in rect:
    for x in range(r[0], r[2]):
        for y in range(r[1], r[3]):
            visit[x][y] = 1
            
print(sum(map(sum, visit)))
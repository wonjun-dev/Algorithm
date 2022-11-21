import sys
from collections import deque

num_test = int(sys.stdin.readline().strip())
q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(num_test):
    cnt = 0
    m, n, k = map(int, sys.stdin.readline().strip().split())
    visit_baechu = {tuple(map(int, sys.stdin.readline().strip().split())): 0 for _ in range(k)}
    for idxs, vis in visit_baechu.items():
        if vis == 0:
            q.append(idxs)
            visit_baechu[idxs] = 1

            while q:
                x, y = q.popleft()
                for i  in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if (nx, ny) in visit_baechu.keys() and visit_baechu[(nx, ny)] == 0:
                        q.append((nx, ny))
                        visit_baechu[(nx, ny)] = 1 
            cnt += 1
    print(cnt)
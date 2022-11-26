import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().strip().split())
board = [[0] * N for _ in range(M)]
visit = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    for row in board[y1:y2]:
        row[x1:x2] = [1] * (x2-x1)

q = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0
areas = []
for y in range(M):
    for x in range(N):
        if visit[y][x]: continue

        if board[y][x] == 0:
            q.append((y, x))
            visit[y][x] = 1
            area = 1

            while q:
                y, x = q.popleft()

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if 0<=nx<N and 0<=ny<M:
                        if not visit[ny][nx]:
                            if board[ny][nx] == 0:
                                visit[ny][nx] = 1
                                q.append((ny, nx))
                                area += 1
                
            cnt += 1
            areas.append(area)
print(cnt)
print(*sorted(areas))
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


q = deque()
visit[0][0][0] = 1
q.append((0, 0, 0))

while q:
    x, y, w = q.popleft()

    if x == N-1 and y == M-1:
        print(visit[x][y][w])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >=0 and nx <= N-1 and ny <= M-1:
            if board[nx][ny] == 0 and visit[nx][ny][w] == 0:
                visit[nx][ny][w] = visit[x][y][w] + 1
                q.append((nx, ny, w))
            elif board[nx][ny] == 1 and w == 0:
                visit[nx][ny][1] = visit[x][y][w] + 1
                q.append((nx, ny, 1))

else:
    print(-1)



import sys
from collections import deque

N = int(sys.stdin.readline())
board = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visit = [[False] * N  for _ in range(N)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque()
ans = []

for x in range(N):
    for y in range(N):
        if visit[x][y] or board[x][y] == 0:
            continue

        visit[x][y] = True
        q.append((x, y))
        cnt = 1
        while q:
            idxs = q.popleft()
            for i in range(4):
                nx = idxs[0] + dx[i]
                ny = idxs[1] + dy[i]

                if nx >= 0 and ny >=0 and nx <=N-1 and ny <=N-1:
                    if not visit[nx][ny] and board[nx][ny] == 1:
                        visit[nx][ny] = True
                        q.append((nx, ny))
                        cnt += 1 
        ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)
import sys
from collections import deque

X, Y = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(X)]

num_cheese = 0
for b in board:
    num_cheese += b.count(1)

visit = [[0] * Y for _ in range(X)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    q = deque()
    visit = [[0] * Y for _ in range(X)]
    q.append((0, 0))
    visit[0][0] = 1
    cnt = 0 

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= X-1 and 0 <= ny <= Y-1:
                if not visit[nx][ny]:
                    if board[nx][ny] == 0:
                        q.append((nx, ny))
                        visit[nx][ny] = 1
                    
                    if board[nx][ny] == 1:
                        board[nx][ny] = 0
                        visit[nx][ny] = 1
                        cnt += 1
    
    return cnt

time = 0
ans = [num_cheese]
while num_cheese > 0:
    melted =  bfs()
    if melted > 0:
        time += 1
        num_cheese -= melted
        ans.append(num_cheese)

print(time)
print(ans[-2])
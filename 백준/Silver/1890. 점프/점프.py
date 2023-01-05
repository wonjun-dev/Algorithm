import sys

N = int(sys.stdin.readline())
BOARD = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]

def dfs(start):
    x, y = start
    if (x, y) == (N-1, N-1):
        return 1
    
    if dp[x][y] == -1:
        dp[x][y] = 0

        jump = BOARD[x][y]
        direction = [(x+jump, y), (x, y+jump)]

        for x_, y_ in direction:
            if x_ < N and y_ < N:
                dp[x][y] += dfs((x_, y_))
    
    return dp[x][y]
    
dfs((0, 0))
print(dp[0][0])
import sys

N = int(sys.stdin.readline())
BOARD = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]


def quad_tree(x, y, n):
    check = BOARD[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != BOARD[i][j]:
                check = -1
                break
    
    if check == 1:
        print('1', end='')
    
    elif check == 0:
        print('0', end='')
    
    else:
        n = n // 2
        print('(', end = '')
        quad_tree(x, y, n)
        quad_tree(x, y + n, n)
        quad_tree(x + n, y, n)
        quad_tree(x + n, y + n, n) 
        print(')', end='')

quad_tree(0, 0, N)
import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

num_test = int(sys.stdin.readline())


def dfs(a):
    visit[a] = True
    for b in G[a]:
        # 지목된 학생이 매칭 된 책이 없거나 / 매칭 된 책이 있어도 새로운 책으로 매칭 될 수 있는 경우
        if B[b] == -1 or (not visit[B[b]] and dfs(B[b])):   
            A[a] = b
            B[b] = a
            return True
    return False

for _ in range(num_test):
    N, M = map(int, sys.stdin.readline().split())
    G = defaultdict(list)
    for i in range(1, M+1):
        a, b = map(int, sys.stdin.readline().split())
        for j in range(a, b+1):
            G[j].append(i)

    match = 0
    A = [-1 for _ in range(N+1)]
    B = [-1 for _ in range(M+1)]
    for i in range(1, N+1):
        if A[i] == -1:  # i번째 책이 매칭된 학생이 없다면
            visit = [False for _ in range(N+2)] # dfs에서 매칭 되지 않은 학생의 경우 -1을 참조하므로 넉넉하게 배열 설정 
            if dfs(i): match +=1

    print(match)
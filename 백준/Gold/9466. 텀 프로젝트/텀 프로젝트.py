import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    S = [0] + list(map(int, sys.stdin.readline().strip().split()))

    visit = [0] * (N+1)
    stack = []
    ans = []
    
    for i in range(1, N+1):
        if not visit[i]:
            visit[i] = 1
            stack.append((i, S[i]))
            cycle = [i]

            while stack:
                start, end = stack.pop()

                if visit[end]:
                    if end in cycle:
                        cycle = cycle[cycle.index(end):]
                    
                    else:
                        cycle = []
                    
                else: 
                    cycle.append(end)
                    stack.append((end, S[end]))
                    visit[end] = 1

            ans += cycle


    print(N-len(ans))


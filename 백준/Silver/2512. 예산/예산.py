import sys

N = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
bank = int(sys.stdin.readline())

s = 1
e = max(money)

while s<=e:
    ub = (s + e) // 2
    total = 0
    for m in money:
        if m >= ub:
            total += ub
        else:
            total += m
    if total > bank:
        e = ub - 1
    elif total < bank:
        s = ub + 1
    else:
        break

if total == bank:
    print(ub)
else:
    print(e)
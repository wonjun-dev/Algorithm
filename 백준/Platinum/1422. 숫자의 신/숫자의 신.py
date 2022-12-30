import sys
from functools import cmp_to_key

K, N = map(int, sys.stdin.readline().split())
nums = sorted([int(sys.stdin.readline()) for _ in range(K)])
select = []
max_num = nums[-1]

for _ in range(N - K + 1):
    select.append(max_num)
select += nums[:-1]
select = sorted(list(map(str, select[:])), key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)

ans = int(''.join(select))
print(ans)
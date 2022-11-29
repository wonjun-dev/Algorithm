import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))

for i in range(1, N):
    nums[i] = max(nums[i] + nums[i-1], nums[i])

print(max(nums))
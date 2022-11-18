l, u = map(int, input().split())

def check(N):
    nums = [1 for _ in range(N)]

    for i in range(2, int(u**0.5 + 1)):
        square = i*i
        for j in range(l//square*square, u+1, square):
            if j <= u and j >= l:
                nums[j-l] = 0
    return nums

nums= check(u-l+1)
print(sum(nums))
import sys

K = int(sys.stdin.readline())
bracket = list(sys.stdin.readline().strip().split())
nums = [False for _ in range(10)]

results = []
def dfs(elem, k):
    if k <= K-1:
            b = bracket[K-k-1]
            if b == '>':
                if elem[-2] < elem[-1]:
                    return
            else:
                if elem[-2] > elem[-1]:
                    return
    
    if k == 0:
        results.append(elem[:])
        return


    for i in range(10):
        if not nums[i]:
            elem.append(i)
            nums[i]= True
            dfs(elem, k-1)
            elem.pop()
            nums[i] = False

dfs([], K+1)

print(''.join(list(map(str, results[-1]))))
print(''.join(list(map(str, results[0]))))

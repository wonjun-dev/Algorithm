import sys

n = int(sys.stdin.readline().strip())
arr = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline().strip())
    arr[num] += 1
   
for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            sys.stdout.write(str(i)+"\n")
    
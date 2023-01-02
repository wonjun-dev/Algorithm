import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

def binary_search(A, num):
    start = 0
    end = len(A) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if A[mid] > num:
            end = mid - 1
        elif A[mid] < num:
            start = mid + 1
        else:
            return 1
    return 0

A = sorted(A)
for b in B:
    print(binary_search(A, b))
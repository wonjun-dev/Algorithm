import sys
from collections import deque

N = int(sys.stdin.readline())
heap = deque([float('-inf')])

def push(x):
    heap.append(-x)
    idx = len(heap) - 1
    while heap[idx] < heap[idx//2]:
        tmp = heap[idx//2]
        heap[idx//2] = heap[idx]
        heap[idx] = tmp
        idx = idx // 2

def pop():
    if len(heap) == 1:
        return 0
    else:
        root = heap[1] * -1
        if len(heap) == 2:
            heap.pop() 
            return root
        else:
            heap[1] = heap.pop()
            
            idx = 1
            while True:
                lc_idx, rc_idx = 2*idx, 2*idx+1
                try:
                    lc, rc = heap[lc_idx], heap[rc_idx]
                    if lc < rc:
                        if heap[idx] > lc:
                            tmp = heap[idx]
                            heap[idx] = lc
                            heap[lc_idx] = tmp
                            idx = lc_idx
                        else:
                            break
                    else:
                        if heap[idx] > rc:
                            tmp = heap[idx]
                            heap[idx] = rc
                            heap[rc_idx] = tmp
                            idx = rc_idx
                        else:
                            break
                except:
                    if len(heap)-1 == lc_idx:
                        lc = heap[lc_idx]
                        if heap[idx] > lc:
                            tmp = heap[idx]
                            heap[idx] = lc
                            heap[lc_idx] = tmp
                            idx = lc_idx
                        else:
                            break
                    else:
                        break
            return root

for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        print(pop())
    else:
        push(x)
 
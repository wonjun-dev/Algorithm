import sys
from collections import deque

N = int(sys.stdin.readline())
heap = deque([(float('-inf'), float('inf'))])

def swap(idx1, idx2):
    tmp = heap[idx2]
    heap[idx2] = heap[idx1]
    heap[idx1] = tmp


def push(x):
    heap.append((abs(x), x))
    idx = len(heap) - 1
    while heap[idx][0] <= heap[idx//2][0]:
        if heap[idx][0] == heap[idx//2][0]:
            if heap[idx][1] < heap[idx//2][1]:
                swap(idx, idx//2)
                idx = idx // 2 
            else:
                return
        else:
            swap(idx, idx//2)
            idx = idx // 2

def pop():
    if len(heap) == 1: return 0
    elif len(heap) == 2: return heap.pop()[1]
    else:
        root = heap[1]
        new_root = heap.pop()
        heap[1] = new_root

        idx = 1
        while True:
            idx_lc, idx_rc = 2*idx, 2*idx+1
            try:
                lc, rc = heap[idx_lc], heap[idx_rc]
                
                if lc[0] < rc[0]:
                    if heap[idx][0] > lc[0]:
                        swap(idx, idx_lc)
                        idx = idx_lc
                    elif heap[idx][0] == lc[0]:
                        if heap[idx][1] > lc[1]:
                            swap(idx, idx_lc)
                            idx = idx_lc
                        else:
                            break
                    else:
                        break
                elif lc[0] > rc[0]:
                    if heap[idx][0] > rc[0]:
                        swap(idx, idx_rc)
                        idx = idx_rc
                    elif heap[idx][0] == rc[0]:
                        if heap[idx][1] > rc[1]:
                            swap(idx, idx_rc)
                            idx = idx_rc
                        else:
                            break
                    else:
                        break
                else:
                    if lc[1] < rc[1]:
                        if heap[idx][0] > lc[0]:
                            swap(idx, idx_lc)
                            idx = idx_lc
                        elif heap[idx][0] == lc[0]:
                            if heap[idx][1] > lc[1]:
                                swap(idx, idx_lc)
                                idx = idx_lc
                            else:
                                break
                        else:
                            break
                    elif lc[1] > rc[1]:
                        if heap[idx][0] > rc[0]:
                            swap(idx, idx_rc)
                            idx = idx_rc
                        elif heap[idx][0] == rc[0]:
                            if heap[idx][1] > rc[1]:
                                swap(idx, idx_rc)
                                idx = idx_rc
                            else:
                                break
                        else:
                            break
                    else:
                        if heap[idx][0] > lc[0]:
                            swap(idx, idx_lc)
                            idx = idx_lc
                        elif heap[idx][0] == lc[0]:
                            if heap[idx][1] > lc[1]:
                                swap(idx, idx_lc)
                                idx = idx_lc
                            else:
                                break
                        else:
                            break

            except:
                if len(heap)-1 == idx_lc:
                    lc = heap[idx_lc]
                    if heap[idx][0] > lc[0]:
                        swap(idx, idx_lc)
                        idx = idx_lc
                    elif heap[idx][0] == lc[0]:
                        if heap[idx][1] > lc[1]:
                            swap(idx, idx_lc)
                            idx = idx_lc
                        else:
                            break
                    else:
                        break
                else:
                    break

        return root[1]


ans = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        ans.append(pop())
    else:
        push(x)

for a in ans:
    print(a)
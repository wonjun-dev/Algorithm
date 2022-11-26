import sys
from collections import deque

num_test = int(sys.stdin.readline().strip())

answer = []
for _ in range(num_test):
    command = sys.stdin.readline().strip()
    size = int(sys.stdin.readline().strip())
    array = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    reverse_cnt = 0
    for c in command:
        if c == 'R':
            reverse_cnt += 1
        elif c == 'D':
            if array and size !=0:
                if reverse_cnt % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
                size -= 1
            else:
                answer.append('error')
                break
    else:
        if reverse_cnt % 2 == 0: 
            answer.append("[" + ",".join(array) + "]")
        else:
            array.reverse()
            answer.append("[" + ",".join(array) + "]")

for a in answer:
    print(a)
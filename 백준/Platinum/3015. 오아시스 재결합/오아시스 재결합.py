import sys

n = int(sys.stdin.readline().strip())
stack = []
cnt = 0
cnt_dict = {}

for i in range(n):
    h = int(sys.stdin.readline().strip())
    
    while stack and i < n:
        if stack[-1] < h:
            num = stack.pop()
            cnt += 1
            cnt_dict[num] -= 1
            
        elif stack[-1] == h:
            cnt += cnt_dict[h]
            if len(stack) > cnt_dict[h]:
                cnt += 1 
            break
            
        else:   # stack[-1] > h:
            cnt += 1
            break

    stack.append(h)
    if h not in cnt_dict:
        cnt_dict[h] = 1
    else:
        cnt_dict[h] += 1

print(cnt)
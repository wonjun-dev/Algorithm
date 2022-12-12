import sys

N, C = map(int, sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house = sorted(house)

s = 1
e = house[-1] - house[0]

while s <= e:
    mid = (s + e) // 2
    cur = house[0]
    cnt = 1

    for i in range(1, len(house)):
        if house[i] >= cur + mid:
            cnt += 1
            cur = house[i]
    
    if cnt < C:
        e = mid - 1
    else:
        s = mid + 1
    

print(e)

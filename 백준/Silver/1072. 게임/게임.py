import sys

x, y = map(int, input().split())

s = 1
e = x
r = sys.maxsize

z = (y * 100) // x

if z >= 99:
    print(-1)
else:
    while s <= e:
        mid = (s + e) // 2
        tmp = ((y + mid) * 100) // (x + mid)
        
        if tmp <= z:
            s = mid + 1
        else:
            r = min(mid, r)
            e = mid - 1
            
    if r == sys.maxsize:
        print(-1)
    else:
        print(r)

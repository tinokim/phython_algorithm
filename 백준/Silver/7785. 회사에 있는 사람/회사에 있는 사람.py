n = int(input())
r = set()
for i in range(n):
    a, b = input().split()
    if b == 'enter':
        r.add(a)
    elif b == 'leave' and a in r:
        r.discard(a)

for i in sorted(r, reverse=True):
    print(i)
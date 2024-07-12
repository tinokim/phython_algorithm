n = input().split('-')
r = 0

if '+' in n[0]:
    r += sum(map(int, n[0].split('+')))
else:
    r += int(n[0])

for i in n[1:]:
    if '+' in i:
        r -= sum(map(int, i.split('+')))
    else:
        r -= int(i)

print(r)

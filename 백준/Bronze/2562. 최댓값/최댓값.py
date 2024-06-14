a = []
chk = 0

for i in range(9):
    a.append(int(input()))
    if chk < a[i]:
        chk = a[i]
        max_i = i
print(max(a))
print(max_i+1)
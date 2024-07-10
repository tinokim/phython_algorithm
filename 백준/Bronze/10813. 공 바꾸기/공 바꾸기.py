n, m = map(int,input().split())
number = [i for i in range(1, n+1)]
for _ in range(m):
    i, j = map(int,input().split())
    number[i-1], number[j-1] = number[j-1], number[i-1]
print(*number)

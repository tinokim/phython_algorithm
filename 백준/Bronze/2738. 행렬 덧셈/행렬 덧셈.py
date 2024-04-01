r = []  
n, m = map(int, input().split())  

for i in range(n):
    nl = list(map(int, input().split()))  
    r.append(nl)  

for i in range(n):
    ml = list(map(int, input().split()))  
    for j in range(m):
        r[i][j] += ml[j]  

for i in range(n):
    for j in range(m):
        print(r[i][j], end=' ')
    print()

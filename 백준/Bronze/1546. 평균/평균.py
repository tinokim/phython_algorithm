n = int(input())
jum = list(map(int, input().split()))
maxJum = max(jum)
avg = 0.0
for i in jum:
    avg = avg + ((i / maxJum) * 100)
    
print(avg / n)
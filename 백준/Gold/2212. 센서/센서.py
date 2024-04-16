n = int(input())  
k = int(input())  
s = list(map(int, input().split()))

s.sort()

d = []
for i in range(n-1):
    d.append(s[i+1] - s[i])

# 거리를 역으로 정렬
d.sort(reverse=True)

# 길이 합 계산
ml = 0
if k < n:
    for i in range(k-1, len(d)):
        ml += d[i]
else:
    ml = 0

print(ml)
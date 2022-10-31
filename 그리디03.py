n, m  = map(int, input().split())
a=[]

for i in range(n):
    a.append(list(map(int, input().split())))


# for i in range(n):
#     print(a)
#     for j in range(m):
#         if b >= int(a[i][j]):
#             b = a[i]
#     print(b)
answer = 0
for i in range(n):
    minimum = 10000 
    for j in range(m):
        if minimum >= a[i][j]:
            minimum = a[i][j]
    if answer <= minimum:
        answer = minimum
print(answer)

# answer = 0
# for row in a:
#     tmp = min(row)
#     answer = max(tmp, answer)

# print(answer)
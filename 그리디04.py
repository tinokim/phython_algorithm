# a, b = map(int, input().split())
# aa=a
# bb=b
# c=0
# d=0
# while a >= b :
#     aa-=1
#     d+=1
#     if aa//bb != 0:
#         c = a//b
#         bb = b/a
# print(d)
n, k = map(int, input().split())
answer = 0
while n >= k:
    if n//k != 0 :
        n = n % k
        answer += 1
    else :
        n-=1
        answer += 1
answer += n
print(answer)
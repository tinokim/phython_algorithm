n = int(input())
a = list(map(int, input().split()))

nge = [-1] * n
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        nge[stack.pop()] = a[i]
    stack.append(i)

print(' '.join(map(str, nge)))
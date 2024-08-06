import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
stack = []

results = []

for i in range(1, n + 1):
    command = list(map(int, data[i].split()))
    
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2:
        if stack:
            results.append(stack.pop())
        else:
            results.append(-1)
    elif command[0] == 3:
        results.append(len(stack))
    elif command[0] == 4:
        results.append(0 if stack else 1)
    elif command[0] == 5:
        results.append(stack[-1] if stack else -1)

# 모든 결과를 한 번에 출력
print('\n'.join(map(str, results)))

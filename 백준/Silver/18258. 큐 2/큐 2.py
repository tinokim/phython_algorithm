import sys
from collections import deque

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
que = deque()

results = []

for i in range(1, n + 1):
    command = data[i].split()
    
    if command[0] == 'push':
        que.append(int(command[1]))
    elif command[0] == 'pop':
        if que:
            results.append(que.popleft())
        else:
            results.append(-1)
    elif command[0] == 'size':
        results.append(len(que))
    elif command[0] == 'empty':
        results.append(1 if not que else 0)
    elif command[0] == 'front':
        results.append(que[0] if que else -1)
    elif command[0] == 'back':
        results.append(que[-1] if que else -1)

print('\n'.join(map(str, results)))

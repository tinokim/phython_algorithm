arr = [list(map(int, input().split())) for _ in range(9)]

max_value = max(map(max, arr))

print(max_value)

for i in range(9):
    for j in range(9):
        if arr[i][j] == max_value:
            print(f'{i + 1} {j + 1}')
            exit()

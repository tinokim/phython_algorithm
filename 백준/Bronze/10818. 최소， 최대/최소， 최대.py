n = int(input())

a = list(map(int, input().strip().split()))

min_value = min(a)
max_value = max(a)

print(f"{min_value} {max_value}")

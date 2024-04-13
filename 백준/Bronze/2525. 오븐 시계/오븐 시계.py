a, b = map(int, input().split())
c = int(input())

total_minutes = b + c  # 총 분을 계산합니다.
a += total_minutes // 60  # 추가된 시간을 시간에 더하고, 24시간 형식을 유지합니다.
b = total_minutes % 60  # 분을 60으로 나눈 나머지가 새로운 분이 됩니다.

a %= 24

print(str(a) + ' ' + str(b))

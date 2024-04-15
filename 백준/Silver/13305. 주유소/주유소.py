n = int(input())
lenth = list(map(int, input().split()))
money = list(map(int, input().split()))

min_money = money[0]
r = 0

for i in range(n - 1):
    # 최소 갱신
    if money[i] < min_money:
        min_money = money[i]
    # 최소 가격 * 거리
    r += min_money * lenth[i]
print(r)
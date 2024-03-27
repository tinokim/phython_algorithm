# 세 개의 주사위 눈을 입력
a, b, c = map(int, input().split())

# 계산되는 값 변수하나 지정
result = 0

# 조건1 3개의 값이 같은 경우
if a == b == c:
    result = 10000 + a * 1000

# 조건2 2개만 같은 경우
elif a == b or a == c:
    result = 1000 + a * 100
elif b == c:
    result = 1000 + b * 100

# 조건3 모두 다른 경우
else:
    result = max(a, b, c) * 100

# 출력
print(result)

a, b = input().split() # 두 수를 문자열로 입력받음

# 각 수를 뒤집고 정수로 변환
r_a = int(a[::-1])
r_b = int(b[::-1])

# 뒤집은 수를 비교하여 더 큰 수 출력
print(r_a if r_a > r_b else r_b)
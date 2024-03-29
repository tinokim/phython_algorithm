# 입력을 받습니다.
n = int(input())

# 주어진 식을 계산합니다.
try:
    result = ((n-2) * (n-1) * (2*n - 3) + 3 * (n-2) * (n-1)) / 12
    print(int(result))  # 결과를 정수로 변환하여 출력합니다.
    print(3)
except Exception as e:
    print(e)  # 예외 발생 시, 예외 메시지를 출력합니다.

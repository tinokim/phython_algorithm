# n개의 정수를 입력.
n = int(input())

 # n개 만큼 반복
for i in range(n+1):
    # 0일때 제외
    if i > 0:
        # 파이썬은 숫자 * 문자 하면 그만큼 반복됨 2중반복문을 안써도 된다.
        print(i*"*") 
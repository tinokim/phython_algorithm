n = int(input())

if n == 4:
    print('long int')
else:
    dap = 'long ' * (n // 4) + 'int'
    print(dap.strip())  # 마지막에 추가된 공백을 제거

# 홀 분모 + 1 분자 - 1
# 짝 분모 - 1 분자 + 1
n = int(input()) # n개 입력
line = 1         # 대각선 길이를 나타냄 초기값 1

# 입력 받은 값이 라인 수보다 크면 반복
while n > line: # n이 속한 대각선을 알기 위해
    n -= line   # 입력 받은 값 - 라인
    line += 1   # 라인 + 1
    
# 짝수일경우
if line % 2 == 0:
    a = n
    b = line - n + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - n + 1
    b = n

print(f'{a}/{b}')
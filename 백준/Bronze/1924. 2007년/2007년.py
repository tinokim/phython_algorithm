# 날짜 분류 31일, 30일, 28일
m31 = [1, 3, 5, 7, 8, 10, 12]
m30 = [4, 6, 9, 11]
# 요일 분류
week = ['MON','TUE','WED','THU','FRI','SAT','SUN']

# x, y 입력
x, y = map(int, input().split())

# 일자 계산을 위한 변수
d = y

# 월만큼 반복 일자계산
for i in range(1, x):
    # 월이 31일인지 체크
    if i in m31:
        d += 31
    # 월이 30일인지 체크
    elif i in m30:
        d += 30
    # 2월이면 나머지 28일 더하기
    else:
        d += 28

# 합산된 d의 값을 7로 나눈 나머지 값이 속한 날이 요일
# week의 인덱스는 0부터 시작하므로 -1
print(week[(d % 7) - 1])

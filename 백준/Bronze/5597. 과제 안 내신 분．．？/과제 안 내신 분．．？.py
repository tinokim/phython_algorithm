# 제출한 학생의 출석번호를 입력받기
submitted = []
for _ in range(28):
    submitted.append(int(input().strip()))

# 1부터 30까지의 모든 출석번호 리스트
all_students = set(range(1, 31))

# 제출하지 않은 학생의 출석번호 찾기
not_submitted = sorted(all_students - set(submitted))

# 결과 출력
for student in not_submitted:
    print(student)

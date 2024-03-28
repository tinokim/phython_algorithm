# 과목의 수를 입력
n = int(input())

# 성적을 입력받아 리스트로 저장
scores = list(map(int, input().split()))

# 최댓값 M을 찾음
M = max(scores)

# 모든 점수를 점수/M*100으로 조작
scores_2 = []  # 저장할 빈 리스트 생성
for score in scores:
    f_s = (score / M) * 100  # 점수를 조작
    scores_2.append(f_s)  # 조작된 점수를 리스트에 추가

# 조작된 점수의 평균을 계산
real_avg = sum(scores_2) / n

# 새로운 평균 출력
print(real_avg)
# 반복값 입력
n=int(input())

# n번 반복문 실행
for _ in range(n):
    # 반복 횟수 R과 문자열 S를 공백으로 구분하여 입력받음
    R, S=input().split()
    # R을 정수형으로 변환
    R=int(R)
    
    # 새 문자열 P 초기화
    P = ''
    
    # 문자열 S의 각 문자를 R번 반복하여 P에 추가
    for char in S:
        P+=char * R
    
    # 결과 문자열 P 출력
    print(P)

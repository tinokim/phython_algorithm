def solution(l, r):
    answer = []
    
    for num in range(l, r+1):
        # 숫자가 "0"과 "5"로만 이루어져 있는지 확인
        if all(c in "05" for c in str(num)):
            answer.append(num)
    
    # 정답 리스트가 비어있다면 -1을 리턴
    return answer if answer else [-1]

# board 인형 공간, moves 크레인 움직일 위치
# 크레인이 움직이면 moves에 가장 위 인형 뽑기 이후 0
# 뽑은 인형 리스트에 마지막 인형과 체크 후 담기

def solution(board, moves):
    l = []
    answer = 0

    for move in moves:
        for i in range(len(board)):
            # 크레인이 집는 가장 위 인형
            if board[i][move-1] != 0:
                # 마지막 인형과 같은지 확인
                if l and l[-1] == board[i][move-1]:
                    l.pop()  # 인형 제거
                    answer += 2  # 터트린 인형 2개 추가
                else:
                    l.append(board[i][move-1])  # 인형 추가
                board[i][move-1] = 0  # 인형 제거
                break  # 다음 move로 넘어감

    return answer
from collections import deque

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())  # 문서의 개수와 궁금한 문서의 위치
  level = list(map(int, input().split()))
  queue = deque([(value, idx) for idx, value in enumerate(level)])  # enumerate 함수는 리스트의 각 요소와 인덱스를 튜플 형태로 반환
  cnt = 0

  while queue:
    max_doc = -1
    for doc in queue:  # 제일 큰 값 찾기
        if doc[0] > max_doc:
            max_doc = doc[0]

    if queue[0][0] < max_doc:
        # 앞의 문서가 가장 중요한 문서가 아니면 마지막으로 이동
        queue.append(queue.popleft())
    else:
        # 가장 앞의 문서가 가장 중요한 문서라면, 이 문서를 인쇄
        cnt += 1
        printed = queue.popleft()

        # 인쇄한 문서가 궁금한 문서인 경우 출력하고 반복 종료
        if printed[1] == m:
            print(cnt)
            break
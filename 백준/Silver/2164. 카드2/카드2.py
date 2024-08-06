import sys
from collections import deque

input = sys.stdin.read
n = int(input())
card = deque(range(1, n + 1))

while len(card) > 1:
    card.popleft()  # 가장 앞의 카드 제거
    card.append(card.popleft())  # 가장 앞의 카드를 맨 뒤로 이동

print(card[0])  # 마지막 남은 카드 출력

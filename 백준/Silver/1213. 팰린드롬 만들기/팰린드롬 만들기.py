from collections import Counter
import sys

word = sys.stdin.readline().strip()
w_cnt = Counter(word)

odd_cnt = 0
center = ""
answer = ""

for k, v in w_cnt.items():
  if v % 2 == 1:
    odd_cnt += 1
    center = k
    if odd_cnt > 1:
      print("I'm Sorry Hansoo")
      exit()

for k, v in sorted(w_cnt.items()):
  answer += (k * (v // 2))

print(answer + center + answer[::-1])
# 함수
def chk(s):
  steck = []
  for c in s:
    if c == '(':
      steck.append(c)
    elif c == ')':
      if not steck:
        return False
      steck.pop()
  return not steck
  
# 입력
for _ in range(int(input())):
  s = input()
  print("YES" if chk(s) else "NO")


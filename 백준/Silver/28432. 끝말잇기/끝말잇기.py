import sys

N = int(sys.stdin.readline())
strings = [ sys.stdin.readline().rstrip() for _ in range(N) ]

s, e = "", ""

for i in range(N):
  if strings[i] == '?':
    if i > 0:
      s = strings[i-1][-1]
    if i < N-1:
      e = strings[i+1][0]

M = int(sys.stdin.readline())

for _ in range(M):
  x = sys.stdin.readline().rstrip()

  if N == 1:
    print(x)
    break

  if x in strings:
    continue

  if not s:
    if x[-1] == e:
      print(x)
  elif not e:
    if x[0] == s:
      print(x)
  elif x[0] == s and x[-1] == e:
    print(x)

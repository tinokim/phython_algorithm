n = int(input())
l = list(map(int, input().split()))
r = 0.0
m_s = max(l)
for i in l:
  r+=i/m_s*100
print(r/n)
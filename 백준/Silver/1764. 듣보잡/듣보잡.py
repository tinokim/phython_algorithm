n, m = map(int, input().split())

nl = [] # 듣
for _ in range(n):
    nl.append(input())

ml = [] # 보
for _ in range(m):
    ml.append(input())

nl.sort()
ml.sort()

r = []    # 듣보

ml_set = set(ml)


for name in nl: # 듣만큼 반복 후 중복제거된 set과 값 비교하여 듣보에 추가
    if name in ml_set:
        r.append(name)

print(len(r))
for name in r:
    print(name)

# 문제 좆같이 읽느건 만나서하고
# 반복된 행동을 계쏙 한줄한줄 쓸거면 반복문을 써라
# 똑같은거 반복해서 받을거면 리스트를 써라
# 변수명 좀 알아먹게 적어라
n,m,k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[-1]
second = data[-2]

total = (first * k + second) * m//(k+1)
print(total)
#total += (first * (m % (k + 1)))
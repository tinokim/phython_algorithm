n = int(input())
a = list(map(int, input().split()))

a.sort()  # 순서대로 정렬
total = 0  # 총 시간
accumulated = 0  # 누적 대기 시간

for time in a:
    accumulated += time  # 누적 대기 시간
    total += accumulated  # 누적 대기 시간을 총 대기 시간에 추가

print(total)  # 각 사람이 돈을 인출하는데 필요한 시간

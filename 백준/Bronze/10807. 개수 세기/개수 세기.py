# 첫째 줄에 정수의 개수 N을 입력받습니다.
N = int(input().strip())

# 둘째 줄에 N개의 정수를 입력받습니다.
numbers = list(map(int, input().strip().split()))

# 셋째 줄에 찾으려고 하는 정수 v를 입력받습니다.
v = int(input().strip())

# numbers 리스트에서 v의 개수를 셉니다.
count_v = numbers.count(v)

# 결과를 출력합니다.
print(count_v)

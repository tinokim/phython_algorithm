def find_sum_s(idx, sum_so_far):
    global count
    if idx >= n:  # 인덱스가 수열의 길이를 넘어서면
        if sum_so_far == s:  # 현재까지의 합이 S와 같다면
            count += 1  # 경우의 수 1 증가
        return
    find_sum_s(idx + 1, sum_so_far)  # 현재 인덱스의 수를 포함하지 않는 경우
    find_sum_s(idx + 1, sum_so_far + nums[idx])  # 현재 인덱스의 수를 포함하는 경우

n, s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0  # S를 만족하는 부분수열의 개수

find_sum_s(0, 0)

if s == 0:  # S가 0일 경우, 빈 수열도 포함되므로 1을 빼준다
    count -= 1

print(count)

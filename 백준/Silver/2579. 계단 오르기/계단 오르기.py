n = int(input())

s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = int(input())

# dp[i]는 i번째 계단까지의 최대 점수
max_s = [0] * (n + 1)
max_s[1] = s[1]
if n > 1:
    max_s[2] = s[1] + s[2]

for i in range(3, n + 1):
    # i-2번째 계단에서 바로 i번째 계단으로 올라가는 경우
    # i-3번째 계단에서 i-1번째 계단을 거쳐 i번째 계단으로 올라가는 경우
    max_s[i] = max(max_s[i - 2] + s[i], 
                        max_s[i - 3] + s[i - 1] + s[i])

print(max_s[n])
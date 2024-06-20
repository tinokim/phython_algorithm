def convert_number(number):
    result = number
    while number > 0:
        result += number % 10
        number //= 10
    return result

def solution(N):
    for M in range(1, N):
        if convert_number(M) == N:
            return M
    return 0

N = int(input())
print(solution(N))
def solution(a, b):
    first_a = int(str(a) + str(b))
    first_b = 2 * int(a) * int(b)
    
    if first_a > first_b:
        return first_a
    else:
        return first_b
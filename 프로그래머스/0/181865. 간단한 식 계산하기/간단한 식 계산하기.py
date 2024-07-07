def solution(binomial):
    calc = ['+', '-', '*', '/']
    binomial_list = binomial.split(' ')
    a = int(binomial_list[0])
    b = int(binomial_list[2])
    operator = binomial_list[1]
    
    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    elif operator == '*':
        answer = a * b
    elif operator == '/':
        answer = a / b
    
    return answer

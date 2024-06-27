def solution(myString, pat):
    transformed_string = ""
    
    for char in myString:
        if char == 'A':
            transformed_string += 'B'
        else:
            transformed_string += 'A'
    if pat in transformed_string:
        return 1
    else:
        return 0

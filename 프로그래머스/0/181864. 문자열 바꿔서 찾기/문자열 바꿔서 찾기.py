def solution(myString, pat):
    transformed_string = myString.translate(str.maketrans('AB', 'BA'))
    if pat in transformed_string:
        return 1
    else:
        return 0

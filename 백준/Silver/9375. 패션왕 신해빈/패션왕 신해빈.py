for _ in range(int(input())):  # 테스트 케이스의 수
    a = {} 
    for _ in range(int(input())):  # 의상의 수 type:{a,b,c,d} 식으로 딕셔너리에 값 넣기
        name, type = input().split()
        if type in a:
            a[type].append(name)
        else:
            a[type] = [name]
    cnt = 1
    for type in a:
        cnt *= len(a[type]) + 1  # 해당 종류의 의상 개수 + 1
    print(cnt - 1)  # 모든 의상을 입지 않는 경우 제외
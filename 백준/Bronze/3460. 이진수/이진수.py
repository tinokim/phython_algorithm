T = int(input())

for _ in range(T):
    # 순서 거꾸로
    bnum = list(reversed(bin(int(input()))[2:]))  # 0b 제거 / string type
    for i in range(len(bnum)):
        if bnum[i] == '1':
            print(i, end = ' ')
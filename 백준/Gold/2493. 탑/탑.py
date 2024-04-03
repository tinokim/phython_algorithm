N = int(input()) # 5
l = list(map(int, input().split())) # 6 9 5 7 4
r = [0] * N # 0

stack = []  # 인덱스를 저장할 스택 0

for i in range(N): # 0 1 2 3 4
    # 스택이 비어있지 않고 현재 타워가 스택의 top에 있는 타워보다 높을 때
    while stack and l[i] > l[stack[-1]]:
        stack.pop()  # 스택의 top에 있는 타워가 현재 타워보다 낮으면 pop

    if stack:  # 스택이 비어있지 않고 현재 타워보다 높은 타워가 존재
        r[i] = stack[-1] + 1
    else:  # 스택이 없으면 현재 타워보다 높은 타워가 왼쪽에 없음
        r[i] = 0  # 없을 경우 0

    stack.append(i)  # 현재 타워의 인덱스를 스택에 push

for i in r:
    print(i, end=' ')

# 가장 높게 쏜 번호를 기억해두고 낮은놈은 pop하면서 기록
# 스택을 쓰는 이유 : 처음부터 젤 왼쪽에 나보다 큰 값을 찾는게 우선이여서 마지막 정보를 알아야 할 때는 스택을 사용해야 함
# 즉 내가 알아야 할 정보는 최근에 높았던 녀석 출력 후 삭제 = 후입 선출
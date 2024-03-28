n = int(input())

fruits = {} # 과일 담을 공간
for _ in range(n):
    name, num = input().split() # 과일이름 숫자 입력
    num = int(num)  # 숫자를 정수로 변환

    if name in fruits:  # 같은 이름의 과일이 있을 때 +
        fruits[name] += num
    else:   # 없을 때 신규 등록
         fruits[name] = num

# 5개인 과일이 하나라도 있으면 YES를 출력하고, 아니면 NO를 출력합니다.
chk = False # YES가 이미 출력되었는지 확인하는 플래그
for count in fruits.values():
    if count == 5:  # 5개인 과일만 YES
        print("YES")
        chk = True
        break  # 하나라도 찾으면 더 이상 확인할 필요가 없으므로 반복문을 종료합니다.

if not chk:  # YES가 출력되지 않았다면 NO를 출력
    print("NO")

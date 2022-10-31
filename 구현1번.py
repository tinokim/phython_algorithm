money = int(input())
# n700=0
# n400=0
# n100=0
# n700=money//700
# money%=700
# n400=money//400
# print(n400)
# money%=400
# print(money)
# n100=money//100
# money%=100

# print("700 : %d "  %n700)
# print("400 : %d "  %n400)
# print("100 : %d "  %n100)
# print("나머지 : %d"  %money)

# 변수 생각하고 만들고
# 적절한 자료구조와 반복문
data = [700, 400, 100]

for x in data:
    target = money // x
    money = money % x
    print(target)
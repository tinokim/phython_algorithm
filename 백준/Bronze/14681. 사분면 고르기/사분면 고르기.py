"""
(12, 5)인 점 A는 x좌표와 y좌표가 모두 양수이므로 제1사분면에 속한다. 
점 B는 x좌표가 음수이고 y좌표가 양수이므로 제2사분면에 속한다.
단, x좌표와 y좌표는 모두 양수나 음수라고 가정한다.
"""

x = int(input())
y = int(input())

if x >= 0 and y >= 0:
    print(1)
elif x >= 0 and y < 0:
    print(4)
elif x < 0 and y >= 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
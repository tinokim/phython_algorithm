a = input().upper()  # 입력받은 문자열을 대문자로 변환
a_cnt = {}  # 알파벳의 횟수를 저장할 딕셔너리

# 문자열의 각 문자 갯수를 센다
for char in a:
    if char in a_cnt:
        a_cnt[char] += 1
    else:
        a_cnt[char] = 1

# 가장 많이 출현한 알파벳의 개수를 찾는다
max_cnt = max(a_cnt.values())

most_a = []
for letter, cnt in a_cnt.items():
    if cnt == max_cnt:
        most_a.append(letter)

# 가장 많이 출현한 알파벳이 여러 개인 경우 '?'를 출력하고, 그렇지 않으면 해당 알파벳을 출력한다
if len(most_a) > 1:
    print('?')
else:
    print(most_a[0])
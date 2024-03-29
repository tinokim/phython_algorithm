from collections import Counter

n = int(input())
nList = list(map(int, input().split()))

m = int(input())
mList = list(map(int, input().split()))

# Counter는 각 숫자를 키로, 해당 숫자의 등장 횟수를 갖음
nCounter = Counter(nList)

# 반복문을 통해 M 리스트의 각 숫자에 대해 다음을 수행.
for number in mList:
    # nCounter에서 현재 숫자(number)의 등장 횟수를 조회
    # 해당 숫자가 없으면 기본값으로 0을 반환
    print(nCounter[number], end=' ')
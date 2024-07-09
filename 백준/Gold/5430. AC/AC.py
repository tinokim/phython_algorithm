import sys

input = sys.stdin.readline
key = ['R', 'D']
T = int(input())

for _ in range(T):
	p = input().rstrip()
	n = int(input())
	temp = input().rstrip().replace("[", "").replace("]", "").split(",")
	x = []
	if temp[0] != "":
		x = list(map(int, temp))
	# p = input()
	# n = int(input())
	# x = list(map(int, input().replace("[", "").replace("]", "").split(",")))
	rCheck = False

	for command in p:
		if command == key[0]:
			rCheck = not rCheck
		else:
			if not x:
				print("error")
				break
			if rCheck:
				x.pop()
			else:
				x.pop(0)
	else:
		if rCheck:
			x.reverse()
		print('[' + ','.join(map(str, x)) + ']')
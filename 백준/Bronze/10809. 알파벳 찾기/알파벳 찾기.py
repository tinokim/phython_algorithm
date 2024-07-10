eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = [-1] * len(eng)
s = input()

for i, char in enumerate(s):
    idx = eng.index(char)
    if result[idx] == -1:
        result[idx] = i

print(*result)

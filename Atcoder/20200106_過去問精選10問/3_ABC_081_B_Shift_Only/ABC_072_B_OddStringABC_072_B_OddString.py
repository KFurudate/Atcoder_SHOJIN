s = input()
n = len(s)
S = ''

for i in range(0, n, 2):
    S += s[i]
print(S)
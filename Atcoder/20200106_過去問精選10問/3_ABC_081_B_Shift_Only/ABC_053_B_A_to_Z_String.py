s = input()
n = len(s)

x = []

for i in range(n):
    if 'A' not in x and s[i] is 'A':
        x.append(i)
        x.append('A')
    elif 'A' in x and s[i] is 'Z':
        x.append(i)

print(x[-1] - x[0] + 1)

n, m = map(int, input().split())

ac = [0]*n
wa = [0]*n

for _ in range(m):
    p, s = map(str, input().split())
    p = int(p)

    if ac[p-1]:
        continue
    else:
        if s == 'AC':
            ac[p-1] = 1
        else:
            wa[p-1] += 1

AC = 0
WA = 0
for i in range(n):
    AC += ac[i]
    if ac[i]:
        WA += wa[i]

print(AC, WA)
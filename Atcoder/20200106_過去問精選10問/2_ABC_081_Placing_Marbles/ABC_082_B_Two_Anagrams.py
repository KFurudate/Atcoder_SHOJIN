s = input()
t = input()

S = sorted(s)
T = sorted(t, reverse=True)

if S < T:
    print('Yes')
else:
    print('No')

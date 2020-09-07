s = input()

lst = ['dream', 'dreamer', 'erase', 'eraser']

for l in lst:
    s = s.replace(l, '')

if len(s) == 0:
    print('YES')
else:
    print('NO')
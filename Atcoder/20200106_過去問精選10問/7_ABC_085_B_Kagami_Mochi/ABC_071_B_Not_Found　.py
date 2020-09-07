S = input()

X = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
     'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
     's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

ans = ''
for x in X:
    if x not in S:
        ans = x
        break

if ans == '':
    ans = 'None'
print(ans)

＃＃＃＃＃＃＃＃＃＃

S = input()
X = [chr(i) for i in range(ord('a'), ord('z')+1)]

ans = ''
for x in X:
    if x not in S:
        ans = x
        break
if ans:
    print(ans)
else:
    print('None')
#回文判定 文字列リバース
s1 = input()
n = len(s1)
s2 = s1[:(n-1)//2]
s3 = s1[(n+3)//2:]

def St_Pal(str): return 1 if str == str[::-1] else 0

ans = 0
ans += St_Pal(s1)
ans += St_Pal(s2)
ans += St_Pal(s3)

if ans == 3:
    print('Yes')
else:
    print('No')

#######
s = input()
ans = True

def isP(s):
    return s == s[::-1]

if not isP(s):
    ans = False
if not isP(s[:len(s)//2]):
    ans = False

if ans:
    print('Yes')
else:
    print('No')
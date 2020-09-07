S = input()

ans = []
for s in S:
    if s ==",":
        s = " "
    ans.append(s)
print(''.join(ans))

n = int(input())
S = input()

x = 0
ans = 0
for s in S:
    if s == 'I':
        x += 1
    if s == 'D':
        x -= 1
    ans = max(x, ans)

print(ans)
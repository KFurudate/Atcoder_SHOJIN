n = int(input())
ans = ''
s, t = input().split()

for i in range(n):
    ans += s[i]+t[i]

print(ans)